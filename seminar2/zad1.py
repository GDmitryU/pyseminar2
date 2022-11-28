print("Enter number")
number=float(input())
stringOfNumber=str(number)
stringOfNumber=stringOfNumber.replace(".","")
number=int(stringOfNumber)
summa=0
while number>0:
    mod=number%10
    summa+=mod
    number//=10
print (summa)