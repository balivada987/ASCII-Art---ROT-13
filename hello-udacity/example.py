n=0
day=0
monthname={"Jan","Feb","March","April","May","June", "July","Aug","Sep","Oct","Nov","Dec"}
def valid_year(year):
        if (year>1985 and year <2005):return year
        else:return n
def valid_month(month):
        if  month in monthname: return month
        else:return n
def valid_day(day):

        if  ( (day > 0 and day <= 31)):return day
        else:return n
print (valid_day(2))
print(valid_year())
print (valid_month('Dec'))