######################
####### IMPORTS ######
######################
import sys
import math

############################################
#######Dictionaries, lists, variables#######
############################################
year={'january':31, 'february':28, 'march': 31, 'april':30, 'may':31, 'june':30, 'july':31,'august':31, 'september':30, 'october':31, 'november':30, 'december':31}
leapYearDict={'january':31, 'february':29, 'march': 31, 'april':30, 'may':31, 'june':30, 'july':31,'august':31, 'september':30, 'october':31, 'november':30, 'december':31}
days=['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
totalDays={'january':0, 'february':31, 'march': 59, 'april':90, 'may':120, 'june':151, 'july':181,'august':212, 'september':243, 'october':274, 'november':304, 'december':334}
totalDaysLeap={'january':0, 'february':31, 'march': 60, 'april':91, 'may':121, 'june':152, 'july':182,'august':213, 'september':244, 'october':275, 'november':305, 'december':335}
yearNumber=[]
day='day'
month='month'
leapYear='leapYear'
yr=0
cent=00
dayMath=5
##############################################

#Weird ass formula i got from a weird website that
#destroys the whole point of this program but shhhh,
#ima use this  formula just to find the first day of any year
#W = (1 +(2.6*11 - 0.2) - 2C + Y + (Y/4) + (C/4)) mod 7

#where floor() denotes the integer floor function,
#k is day (1 to 31)
#m is month (1 = March, ..., 10 = December, 11 = Jan, 12 = Feb) Treat Jan & Feb as months of the preceding year
#C is century (1987 has C = 19)
#Y is year (1987 has Y = 87 except Y = 86 for Jan & Feb)
#W is week day (0 = Sunday, ..., 6 = Saturday)


#############################
######### FUNCTIONS #########
#############################


#takes the previously declared firstDay and assign a number to it based on
#position in the week 
def firstDayFunction():
    global firstDay
    firstDay=days.index(firstDay)
    firstDay=firstDay-1

#tests if the given year is a leap year
def leapYearTest():
    global leapYear 
    if ((int(yearInput) % 4) == 0):
        if((int (yearInput) % 100) == 0):
            if ((int(yearInput)% 400) == 0 ):
                leapYear='yes'
            else:
                leapYear='no'
        else:
            leapYear='yes'
    else:
        leapYear='no'
def yearSplit():
    yearNumber.append(year)
    century=yearNumber[0][0:2]



#Used for Leap Years

#executed for every leap year    
def leapYearFunction():
    firstDayFunction()
    desiredDateLeap()


#uses input to get a month and day and making sure all the numbers are legit
def desiredDateLeap():
    while True:
        print('what month would you like to know')
        global month
        month=input().lower()
        if (month in leapYearDict.keys())==True:
            break
    while True:
        print('what day of that month would you like to know')
        daysInMonth=leapYearDict.get(month)
        global day
        day=input().lower()
        try:
            if (int(day) <= daysInMonth)& (int(day)>0):
                break
        except ValueError:
            pass
        print('That day doesnt fit within the month')


#finding the specific day, the end result of this program
def dateFinderLeap():
    dayMath=(totalDaysLeap.get(month)+ int(day)+int(firstDay))%7
    global x
    x=(days[dayMath])
    

#Used for regular years


#executed for all non leap years    
def noLeapYearFunction():
    print('this is a year that begins on ' + str(firstDay))
    desiredDate()
    firstDayFunction()


#gets month and day and makes sure the values are legit
def desiredDate():
    while True:
        print('what month would you like to know')
        global month
        month=input().lower()
        if (month in year.keys())==True:
            break
        else:
            print('That is not a month')
    while True:
        print('what day of that month would you like to know')
        daysInMonth=year.get(month)
        global day
        day=input().lower()
        try:
            if (int(day) <= daysInMonth)& (int(day)>0):
                break
        except ValueError:
            pass
        print('That day doesnt fit within the month')



#end result of program, finds the day of the week given first day, month , and day
def dateFinder():
    dayMath=(totalDays.get(month)+int(day)+ int(firstDay))%7
    global x
    x=(days[dayMath])

#################################
######### END OF FUNCTIONS ######
#################################

#Executing starts here
print('Hello welcome to date checker bot')
print('Select what you want to execute')
print('1. Select the year')
print('2. Select the first day of the year')
while True:
    option=input()
#choosing to input the first day of the year, idk why you'd do this but it's what
#I made first
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
        if leapYear=='yes':
            leapYearFunction()
            dateFinderLeap()
    
        if leapYear=='no':
            noLeapYearFunction()
            dateFinder()
        print ('On ' + month+ ' ' + day + ' it is a ' + x )
        break

#Selecting the year input option gets you here. AKA option 1
    elif (int(option)==1):
        print('what year less than 9999, but more than 0?')
        while True:
            yearInput=input()
            #taking the year, putting it into a 4 digit list, separating it into
            #two digits, one for the first two, one for the last 2
            if yearInput.isdigit():
                yearNumber=([int(d) for d in str(yearInput)])
                while (len(yearNumber)) < 4:
                    yearNumber.insert(0,0)
                centList=([int(f) for f in yearNumber])
                centList=(centList[0:2])
                cent = str("".join(map(str, centList)))

                yrList=([int(e) for e in yearNumber])
                yrList=(yrList[2:4])
                yr = str("".join(map(str, yrList)))
                yr=int(yr)-1
                break
            else:
                print('hol up, that aint a year')
        #math that gives the user the first day to the year they inputted
        global dayNumber
        dayNumber =(1 +math.floor(2.6*11 - 0.2) - 2*int(cent) + int(yr) + math.floor(int(yr)/4) + math.floor(int(cent)/4)) % 7
        int(dayNumber)
        firstDay=(days[int(dayNumber)])
        str (firstDay)
        leapYearTest()
        if leapYear=='yes':
            leapYearFunction()
            dateFinderLeap()
    
        if leapYear=='no':
            noLeapYearFunction()
            dateFinder()
        print ('in the year ' + yearInput + ' on ' + month+ ' ' + day + ' it is a ' + x )
        break
    else:
        print("that was not an option")

print('done')








