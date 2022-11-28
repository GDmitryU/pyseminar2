print("Enter the coordinates of the first point (x1,y1)")
x1,y1 =map(float,input().split())
print("Enter the coordinates of the second point (x2,y2)")
x2,y2 =map(float,input().split())
deltaX=abs(x1-x2)
deltaY=abs(y1-y2)
gipotenuza= (deltaX*deltaX+deltaY*deltaY)**0.5
print(gipotenuza)
