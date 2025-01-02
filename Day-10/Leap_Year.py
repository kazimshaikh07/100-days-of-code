def is_leap_year(year):
    if year%4==0:
        return (f"{year} is a leap year".title())
    if year%4!=0:
        return (f"{year} is not a leap year".title())
    if year%100!=0:
        return (f"{year} is leap year".title())
    if year%100==0:
        return (f"{year} is not a leap year".title())
    if year%400!=0:
        return (f"{year} is not a leap year".title())
    if year%400==0:
        return (f"{year} is a leap year".title())
    if type(year)!=int:
        print("Invalid Entry")
year = is_leap_year(1999)
print(year)