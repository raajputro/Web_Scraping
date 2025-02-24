# import arrow
#
# now = arrow.now()
# today = now.format("YYYY-MM-DD")
# print(f"Today is : {today}")
# yesterday = now.shift(days=-1).format("YYYY-MM-DD")
# print(f"Yesterday is : {yesterday}")
# last_week = now.shift(days=-7).format("YYYY-MM-DD")
# print(f"Start of Last Week : {last_week}")
# this_month = now.format('MMM')
#
# print(f"This month is : {this_month}")
#
# def parse_dates(str_date):
#     given_date = arrow.get(str_date)
#     str_year = given_date.format('YYYY')
#     str_month = given_date.format('MMM')
#     str_day = given_date.format('DD')
#     print(f"Given Date: Year = {str_year}, Month = {str_month}, Day = {str_day}")
#
# parse_dates(yesterday)

sum_of_generators = sum(x**10 for x in range(10))
print(f"Generators value: {sum_of_generators}")