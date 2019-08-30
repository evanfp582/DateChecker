#yearNumber=[]

#while True:
#    year=input()
 #   if year.isdigit():
#            yearNumber.append(year)
 #           print((yearNumber[0][0:2]))
#            while (len(yearNumber) < 4):
#                #print(len(yearNumber))
#                yearNumber.insert(0,0)
#            print((yearNumber[0]))
#            break

#mf set up



yearNumber=[]
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
        print (cent)


        century=("first two digits are done")

        yrList=([int(e) for e in yearNumber])
        yrList=(yrList[2:4])
        yr = str("".join(map(str, yrList)))
        print(yr)
        break
    else:
        print('hol up, that aint a year')
             


        
