import sys


#Dictionary  and lists of months and the number of days
year={'january':31, 'february':28, 'march': 31, 'april':30, 'may':31, 'june':30, 'july':31,'august':31, 'september':30, 'october':31, 'november':30, 'december':31}
leapYearDict={'january':31, 'february':29, 'march': 31, 'april':30, 'may':31, 'june':30, 'july':31,'august':31, 'september':30, 'october':31, 'november':30, 'december':31}
days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
totalDays={'january':0, 'february':31, 'march': 59, 'april':90, 'may':120, 'june':151, 'july':181,'august':212, 'september':243, 'october':274, 'november':304, 'december':334}
totalDaysLeap={'january':0, 'february':31, 'march': 60, 'april':91, 'may':121, 'june':152, 'july':182,'august':213, 'september':244, 'october':275, 'november':305, 'december':335}
day='day'
month='month'
##############################################


#### FUNCTIONS ######
#Used for Leap Years
def leapYearFunction():
    print('this is a leap year that begins on ' + str(firstDay))
    desiredDateLeap()

def desiredDateLeap():
    while True:
        print('what month would you like to know')
        global month
        month=input().lower()
        if (month in leapYearDict.keys())==True:
            print('one morestep done')
            break
    while True:
        print('what day of that month would you like to know')
        daysInMonth=leapYearDict.get(month)
        global day
        day=input().lower()
        try:
            if (int(day) <= daysInMonth)& (int(day)>0):
                print('great!')
                break
        except ValueError:
            pass
        print('That day doesnt fit within the month')
    print('you picked a date number within the month')

def dateFinderLeap():
    print(totalDaysLeap.get(month)+int(day))
    dayMath=(totalDaysLeap.get(month)+int(day))%7
    print(dayMath)

    
##

#Used for regular years
    
def noLeapYearFunction():
    print('this is a year that begins on ' + str(firstDay))
    desiredDate()

    
def desiredDate():
    while True:
        print('what month would you like to know')
        global month
        month=input().lower()
        if (month in year.keys())==True:
            print('one morestep done of nonleap year')
            break
    while True:
        print('what day of that month would you like to know')
        daysInMonth=year.get(month)
        global day
        day=input().lower()
        try:
            if (int(day) <= daysInMonth)& (int(day)>0):
                print('great!')
                break
        except ValueError:
            pass
        print('That day doesnt fit within the month')
    print('you picked a date number within the month')



        
def dateFinder():
    print(totalDays.get(month)+int(day))
    dayMath=(totalDays.get(month)+int(day))%7
    print(dayMath)
    print(days[dayMath])

#END OF FUNCTIONS ####


#actual code
print('Hello welcome to date checker bot')
while True:
    print('what is the first day of the week of the year')
    firstDay=input().lower()
    if (firstDay in days) == True:
        break
    else:
        print('try again bucko')
print('please input weather the year is a leap year or not as y or n')
while True:
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
    print(month,day)
    dateFinderLeap()
if leapYear=='no':
    noLeapYearFunction()
    print(month,day)
    dateFinder()
