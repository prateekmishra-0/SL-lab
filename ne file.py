
print("Water jug Problem")
x=0
y=0
while True:
    rule = int(input("enter the no."));
    if rule == 2:
        if y<3:
            y = 3
            print(x,y)
    if rule == 9:
        if x+y<=4 and y>0:
            x= x+y
            y= 0
            print(x,y)
    if rule == 7:
        if x+y>=4 and y>0:
            y= y-(4-x)
            x = 4
            print(x,y)
    if rule == 5:
        if x>0:
            x=0
            print(x,y)
    if x == 2:
        print("the problem is solved")
        break