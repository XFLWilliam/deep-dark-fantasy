a = int(input("input student score: "))
if(a > 100 or a < 0):
    print("error")
elif(89<a<101):
    print('A')
elif(a > 59 and a < 90):
    print('B')
else:
    print('C')
