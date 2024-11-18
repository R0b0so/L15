a = input("Enter any word or sentence")
i = 1
for i in a:
    if(i == "A" or i == "a"):
        print("A is found")
        break
    else:
        print("A is not found")