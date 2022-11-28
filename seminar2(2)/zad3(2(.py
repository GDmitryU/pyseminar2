from random import randint
print("enter the number of items")
n=int(input())
massElements = [0]*(n+1)
for index in range(1,n+1):
    massElements[index] = index
print (massElements)
for index in range(1,n+1):
    index1 = randint(1, n)
    massElements[index],massElements[index1] = massElements[index1],massElements[index]
print (massElements)
