months = ["January","February","March","April","May","June","July","August","September","October","November","December"]

# validate and type user input
def set_month(year,month):
    value = input(f"Enter average rainfall for year {year}:{month} as X.XX: ")
    try:
        value = float(value)
    except:
        print(f"Invalid Type: cannot convert {value} to float")
        set_month(month)
    return value
#validate and type user input 
def set_years():
    years = input("Enter the how many years to calculate: ")
    try:
        years = int(years)
    except:
        print(f"Invalid Type: cannot convert {years} to int")
        set_years()
    return years



years = set_years()
yearly_rainfall = {"total" : 0, "average" : 0, "month_count" : 0}
for y in range(0,years):
    for month in months:
        total = set_month(y,month)
        yearly_rainfall["total"] += total
        yearly_rainfall["month_count"] += 1

yearly_rainfall["average"] = yearly_rainfall["total"] / yearly_rainfall["month_count"]
print(f"total rainfall {yearly_rainfall['total']} inches over {yearly_rainfall['month_count']} months \n average inches of rainfall per month: {yearly_rainfall['average']} \n ")
