# You are given the following information, but you may prefer to do some research for yourself.
# 1 Jan 1900 was a Monday.
# Thirty days has September,April, June and November.
# All the rest have thirty-one,
# Saving February alone,Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?



# week={"Monday":1,"Tuesday":2," Wednesday":3," Thursday":4," Friday":5," Saturday":6,"Sunday":7}

# thirty={"April":4,"June":6,"September":9,"November":11}

# thirtyone={"January":1,"March":3,"May":5,"July":7,"August":8,"October":10}


# yearly 365 days 12 months 52 weeks 


# weekly 52 weeks 7days



# monthly 12 months

# daily 30 31 28 or 29

# total_years=years[1] - years[0]
# total_days=365*total_years


def day_finder(day):
    if day%7==0:
        return "Sunday"
    elif day%7==1:
        return "Monday"
    elif day%7==2:
        return "Tuesday"
    elif day%7==3:
        return "Wednesday"
    elif day%7==4:
        return "Thursday"
    elif day%7==5:
        return "Friday"            
    elif day%7==6:
        return "Saturday"           

# print(day_finder(366))    Tuesday

week={"Monday":1,"Tuesday":2," Wednesday":3," Thursday":4," Friday":5," Saturday":6,"Sunday":7}

thirty={"April":4,"June":6,"September":9,"November":11}

thirtyone={"January":1,"March":3,"May":5,"July":7,"August":8,"October":10,"December":12}

febs={"feb28":2,"feb29":2}

def sunday_counter(day,firstsun):
    if day<=7 and day_finder(day)=="Sunday":
        firstsun+=1
    return firstsun

def fundaytion(final_year):
    year=1901
    totaldays=366
    month=1
    firstsun=0
    
    while year<final_year+1:
        # print(list(thirtyone.values()))
        print(day_finder(totaldays),totaldays,year,month)

        if month in list(thirtyone.values()):
            # print(thirtyone.values())
            for day in range(1,32):
                totaldays+=1
                if day<=7 and day_finder(totaldays)=="Sunday":
                    firstsun+=1
            month+=1
        elif month in list(thirty.values()):
            # print(thirty.values())
            for day in range(1,31):
                totaldays+=1
                if day<=7 and day_finder(totaldays)=="Sunday":
                    firstsun+=1  
            month+=1
        elif month==2:
            # print("February")
            if year%4==0:
                for day in range(1,30):
                    totaldays+=1
                    if day<=7 and day_finder(totaldays)=="Sunday":
                       firstsun+=1    
            else:
                for day in range(1,29):
                    totaldays+=1
                    if day<=7 and day_finder(totaldays)=="Sunday":
                       firstsun+=1    
            month+=1     
        elif month==13:
            year+=1
            month=1
            print(month,year)
    return firstsun


# print(fundaytion(2000)) #1200