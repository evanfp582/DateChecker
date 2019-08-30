days=['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
import math
cent=20
yr=19
yr=yr-1
dayNumber =(1 +math.floor(2.6*11 - 0.2) - 2*int(cent) + int(yr) + math.floor(int(yr)/4) + math.floor(int(cent)/4)) % 7
int(dayNumber)
print(dayNumber)
print(days[int(dayNumber)])



#Weird ass formula i got from a weird website that destroys the whole point of this program but shhhh, ima use this  formula just
#to find the first day of any year
#W = (1 +(2.6*11 - 0.2) - 2C + Y + (Y/4) + (C/4)) mod 7

#where floor() denotes the integer floor function,
#k is day (1 to 31)
#m is month (1 = March, ..., 10 = December, 11 = Jan, 12 = Feb) Treat Jan & Feb as months of the preceding year
#C is century (1987 has C = 19)
#Y is year (1987 has Y = 87 except Y = 86 for Jan & Feb)
#W is week day (0 = Sunday, ..., 6 = Saturday)


#W = (k + floor(2.6m - 0.2) - 2C + Y + floor(Y/4) + floor(C/4)) mod 7

#where floor() denotes the integer floor function,
#k is day (1 to 31)
#m is month (1 = March, ..., 10 = December, 11 = Jan, 12 = Feb) Treat Jan & Feb as months of the preceding year
#C is century (1987 has C = 19)
#Y is year (1987 has Y = 87 except Y = 86 for Jan & Feb)
#W is week day (0 = Sunday, ..., 6 = Saturday)
