import sys

def leapYearFunction():
    print('this is a leap year that begins on ' + str(firstDay))
    desiredDateLeap()

    
def noLeapYearFunction():
    print('this is a year that begins on ' + str(firstDay))
    desiredDate()


def desiredDate():
    while 1==1:
        print('what month would you like to know')
        month=input().lower()
        if (month in year.keys())==True:
            print('one morestep done of nonleap year')
            break
    while 1==1:
        print('what day of that month would you like to know')
        daysInMonth=year.get(month)
        day=input().lower()
        if (int(day) <= daysInMonth)& (int(day)>0):
            print('great!')
            break
        print('That day doesnt fit within the month')
    print('you picked a date number within the month')
        
        
            
#This is also broken for a reason im not sure of   
def desiredDateLeap():
    while 1==1:
        print('what month would you like to know')
        leapMonth=input().lower()
        if (leapMonth in leapYear.keys())==True:
            print('one morestep done')
            break
#


#Dictionary of months and the number of days
year={'january':31, 'february':28, 'march': 31, 'april':30, 'may':31, 'june':30, 'july':31,'august':31, 'september':30, 'october':31, 'november':30, 'december':31}
leapYear={'january':31, 'february':29, 'march': 31, 'april':30, 'may':31, 'june':30, 'july':31,'august':31, 'september':30, 'october':31, 'november':30, 'december':31}

days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
##############################################




#actual code
print('Hello welcome to date checker bot')
print('what is the first day of the week of the year')
while 1==1:
    firstDay=input().lower()
    if (firstDay in days) == True:
        break
    else:
        print('try again bucko')
print('please input weather the year is a leap year or not as y or n')
while 1==1:
    leapYear=input().lower()
    if leapYear == 'n':
        leapYear='no'
        break
        
    elif leapYear == 'y':
        leapYear='yes'
        break
    else:
        print('try again bucko')

if leapYear=='yes':
    leapYearFunction()
if leapYear=='no':
    noLeapYearFunction()


