print("Enter number of the quarter")
quarter=int(input())
if quarter == 1:
    print("x>0 and y>0")
elif quarter == 2:
    print("x<0 and y>0")
elif quarter == 3:
    print("x<0 and y<0")
elif quarter == 4:
    print("x>0 and y<0")
else:
    print("wrong number entered")