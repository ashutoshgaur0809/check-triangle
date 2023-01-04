T = int(input("Enter how many test cases you want = "))
for i in range(T):
    x = int(input("X=  "))
    y = int(input("y=  "))
    z = int(input("Z=  "))
    A = x+y+z
    if (A == 180):
        print("Right triangle")
    else:
        print("Not right")
