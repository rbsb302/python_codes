def isLeap(year):
    month=[31,28,31,30,31,30,31,31,30,31,30,31]
    if(year%4==0):
        month[1]=29
    return month

def century(year):
    cent=year-year%100
    if cent%400==0:  #if its a leap century odd days=0
        return 0
    elif cent%400!=0:  #if its a non-leap century odd days=1
        return 1

def previousYear(year):
    previous=(year-1)%100
    leap=previous//4
    ordinary= previous-leap
    return ordinary+(leap*2)   #odd days for previous completed year

def currentYear(day,month,year):
    updatedMonths=isLeap(year)[:]
    #print(updatedMonths)
    sum=0
    for i in range(month-1):
        
        sum += updatedMonths[i]
    sum += day
    #print("sum%7 of months of current year=",sum%7)

    odday3= sum%7         #odd days for current years
    odday1=century(year)
    odday2=previousYear(year)
    totalodd_day(odday1,odday2,odday3)

def totalodd_day(odd1,odd2,odd3):
    total=odd1+odd2+odd3
    if(total>7):
        total %= 7
    Day(total)    
    

def Day(odd_day):
    day=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    print("According to the entered date your day is:",day[odd_day])  
    

print("enter the date to find day:")    
currentYear(int(input("enter day:")),int(input("enter month(mm):")),int(input("enter year:")))

