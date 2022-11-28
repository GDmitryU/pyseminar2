print("enter the number of items")
n=int(input())
massElements=[0]*(n+1)
summa=0
for i in range(1,n+1):
    massElements[i]= (1 + 1/i)**i
    summa+=massElements[i]
print (massElements)
print (summa)
