from random import randint
print("enter the number of items")
n=int(input())
massElements = [0]*(n)
for index in range(n):
    massElements[index] = randint(1000, 10000)
print (massElements)
print("Enter number: 0..9")
number=int(input())
for index in range(n):
    stringElement= str(massElements[index])
    stringElement = stringElement.replace(str(number),"")
    massElements[index]=int(stringElement)
print (massElements)
for index in range(n):

    while massElements[index]//10>0:
        element = massElements[index]
        digitsSum = 0
        while element > 0:
            mod = element % 10
            digitsSum+=mod
            element//=10
        massElements[index]= digitsSum
print (massElements)
newMassElements = []
for i in massElements:
       if i not in newMassElements:
          newMassElements.append(i)
print (newMassElements)