import arrow
import pandas as pd
from sqlalchemy import create_engine
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

company_ids = [192,193]
now = arrow.now()
start_date = now.shift(days=-7).format("YYYY-MM-DD")
end_date = now.shift(days=-1).format("YYYY-MM-DD")

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
def date_parser(str_date):
    g_date = arrow.get(str_date)
    return f"{g_date.format('MMM')} {g_date.format('DD')}, {g_date.format('YYYY')}"

for company_id in company_ids:
    sDate = date_parser(start_date)
    eDate = date_parser(end_date)

    file_name= ("EBL" if company_id==192 else "MTB") + f" Payment Receivables [{sDate} - {eDate}].xlsx"
    engine = create_engine("mssql+pyodbc://GIFTY/gifty.asia?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes")
    query = """
    select oa.Id as [Reference Id], oa.PhoneNumber as [Receiver]
        , c.Name as [Merchant]
        , o.OfferPrice as [Gift Amount]
        , case c.Id
            when 174 then 1.5
            when 228 then 1.0
            when 234 then 1.0
            when 236 then 1.0
            when 248 then 1.0
            when 251 then 1.0
            when 259 then 1.0 else 3.0 end as [Commission %]
        , case c.Id
            when 174 then o.OfferPrice * 0.015
            when 228 then o.OfferPrice * 0.01
            when 234 then o.OfferPrice * 0.01
            when 236 then o.OfferPrice * 0.01
            when 248 then o.OfferPrice * 0.01
            when 251 then o.OfferPrice * 0.01
            when 259 then o.OfferPrice * 0.01 else o.OfferPrice * 0.03 end as Commission
        , FORMAT (aot.CreatedDate, 'MMM dd yyyy hh:mm:ss ') as [Redeem Date]
        , FORMAT (oa.CreatedDate, 'MMM dd yyyy hh:mm:ss ') as [Created Date]
        --, aot.PurchaseAmount
    from OfferAssignments as oa
        inner join Offers as o on oa.OfferId = o.Id
        inner join AvailOfferTransactions as aot on oa.Id = aot.OfferAssignmentId
        inner join Companies as c on oa.MerchantId = c.Id
    where o.OfferProviderId = """+str(company_id)+"""
        and oa.HasConsumed = 1
        and cast(aot.CreatedDate as date) between '"""+start_date+"""' and '"""+end_date+"""'
    order by aot.CreatedDate
    """
    df = pd.read_sql(query, engine)
    sub_total = round(df['Gift Amount'].sum(),2)
    total_commission = round(df['Commission'].sum(),2)
    total_receivable = sub_total - total_commission
    data = {
        'Sub Total': [sub_total],
        'Total Commission': [total_commission],
        'Total Receivable': [total_receivable],
    }
    df2 = pd.DataFrame(data).transpose()
    with pd.ExcelWriter(file_name, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="Sheet1", startrow=0, startcol=0, index=False)
        df2.to_excel(writer, sheet_name="Sheet1", startrow=0, startcol=len(df.columns) + 2, index=True)
    engine.dispose()