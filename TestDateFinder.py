import sys


#Dictionary  and lists of months and the number of days
year={'january':31, 'february':28, 'march': 31, 'april':30, 'may':31, 'june':30, 'july':31,'august':31, 'september':30, 'october':31, 'november':30, 'december':31}
leapYearDict={'january':31, 'february':29, 'march': 31, 'april':30, 'may':31, 'june':30, 'july':31,'august':31, 'september':30, 'october':31, 'november':30, 'december':31}
days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
totalDays={'january':0, 'february':31, 'march': 59, 'april':90, 'may':120, 'june':151, 'july':181,'august':212, 'september':243, 'october':274, 'november':304, 'december':334}
totalDaysLeap={'january':0, 'february':31, 'march': 60, 'april':91, 'may':121, 'june':152, 'july':182,'august':213, 'september':244, 'october':275, 'november':305, 'december':335}
yearNumber=[]
day='day'
month='month'
leapYear='leapYear'
dayNumber=0
yr=0
cent=00
##############################################

#Weird ass formula i got from a weird website that destroys the whole point of this program but shhhh, ima use this  formula just
#to find the first day of any year
#W = (1 +(2.6*11 - 0.2) - 2C + Y + (Y/4) + (C/4)) mod 7

#where floor() denotes the integer floor function,
#k is day (1 to 31)
#m is month (1 = March, ..., 10 = December, 11 = Jan, 12 = Feb) Treat Jan & Feb as months of the preceding year
#C is century (1987 has C = 19)
#Y is year (1987 has Y = 87 except Y = 86 for Jan & Feb)
#W is week day (0 = Sunday, ..., 6 = Saturday)



#### FUNCTIONS ######

def yearSplit():
    yearNumber.append(year)
    century=yearNumber[0][0:2]



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
    print(days[dayMath])
    print(month,day)

    
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
    print(month,day)

#END OF FUNCTIONS ####


#actual code
print('Hello welcome to date checker bot')
print('Select what you want to execute')
print('1. Select the year')
print('2. Select the first day of the year')
option=input()
if (int(option) == 2):
    while True:
        print('what first day of year ')
        firstDay=input().lower()
        if (firstDay in days) == True:
            break
        else:
            print('try again bucko')
    print('please input weather the year is a leap year or not as y or n')
    while True:
        leapYear
        leapYear=input().lower()
        if leapYear == 'n':
            leapYear='no'
            break
            
        elif leapYear == 'y':
            leapYear='yes'
            break
        else:
            print('try again bucko')
elif (int(option)==1):
    print('You have chosen Year slection')
    print('what year?')
    while True:
        year=input()
        if year.isdigit():
            yearNumber=([int(d) for d in str(year)])
            print(yearNumber)
            while (len(yearNumber)) < 4:
                yearNumber.insert(0,0)
                print(yearNumber)
            centList=([int(f) for f in yearNumber])
            centList=(centList[0:2])
            cent = str("".join(map(str, centList)))
            print(cent)

            yrList=([int(e) for e in yearNumber])
            yrList=(yrList[2:4])
            yr = str("".join(map(str, yrList)))
            print(yr)
            break
        else:
            print('hol up, that aint a year')

    int(dayNumber)
    dayNumber = (1 +(2.6*11 - 0.2) - 2* int(cent) + int(yr) + (int(yr)//4) + (int(cent)//4) % 7)
    print(days[dayNumber])
print(day)
if leapYear=='yes':
    leapYearFunction()
    dateFinderLeap()
    
if leapYear=='no':
    noLeapYearFunction()
    dateFinder()







