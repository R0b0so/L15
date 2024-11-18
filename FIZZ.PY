num= int(input("Enter any number"))
i = 1
for i in range(num):
    if(i % 10 == 0):
        pass
    elif(i % 15 == 0):
        print("twist")
    elif(i % 3 == 0):
        print("fizz")
    elif(i % 5 == 0):
        print("buzz")
    
        
    else:
        print(i)