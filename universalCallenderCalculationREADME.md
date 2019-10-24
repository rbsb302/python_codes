# python_codes
day can be calculated by finding the number of odd days/extra days 

take the year and check if it is a leap year: if (year % 4 == 0) -> its leap i.e(a non-century year 220,1980,1856....is completely divisible by 4)
if the year is leap, number of odd days=2 (366 days % 7 days of week = 2)
if the year is an ordinary year, number of odd days= 1 (365 days % 7days of week =1)
for century years(2000,1900,1800,1700...): if(year % 400 == 0)-> its leap i.e(century leap year is completely divisible by 400)
if century is leap, number of odd days= 0 (remember, eg:2000 % 4=0)
if century is not leap, number of odd days= 1(2019 % 4= 3)

when the entered year is leap => february=29days else february=28days
using the above infor mation calculate the odd day for the current year as:
eg : 15 aug 1947
1947 is !leap: ie. feb=28days
jan + feb + mar + apr + may + jun + jul + 15(aug)= 31 + 28 +31 + 30 + 31 + 30 + 31 + 15 = 227 since 227 > 7 days of week
227 % 7 = 3 odd days

cosidering the previous year which has been completed i.e: 1946
we split this year to a centuray year and remaining year => 1900 + 46
1900 is !leap century therefore odd days for this century is 1

odd days for remaining years:
number of leap years in 46 years= 46/4= 11 leap years
ordinary years= 46 - 11= 35 ordinary years
odd days= (35*1) + (11*2)     #non leap year odd day=1, leap year odd day=2
odd days= 35 + 22= 57 >7 therefore odd days= 57 % 7= 1

now, total odd days= previous year century odd day + previous remain years odd days + current year odd days = 1 + 1 + 3 = 5<7
if this total odd day was greater than 7 we would have to use total odd days % 7 to find the odd days

week's days =[sunday, monday, tuesday, wednesday, thursday, friday, saturday]
with incices of this list starting from 0 to 6
we have total odd days= 5 which corresponds to Friday.
Thus it was a Friday on 15th August 1947.

summary:


                                            yes- feb=29 days
                 current year -> is leap <
              /                            no- feb=28 days --> add days of each month till the date of the month required                  
year -split- <
              \                                                      yes -> odd day=0
               \                         century year -->is leap? -<
                  previous year -split-<                             no -> odd day=1
                                          remaining year -->find the number of odinary years in the remaining year by subtracting leap years from remaining years
                                                |
                                                V
                                           calculate the number of leap years in the remaining years by dividing the remaining year by 4    
                                          using leap and ordinary years of remaining years calculate odd days= ordinary years + (leap year * 2)
                *if any of the calculated odd days are greater than 7 perform a modulo division of that odd day with 7 to get the proper odd day
                
                using day table [sun,mon,tue,wed,thu,fri,sat] find out the day for the date.
                                          
