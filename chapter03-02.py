#divisible number
s_num = input("please enter the integer : ")
num = int(s_num)

if num % 2 == 0:
    print(f"{num} is number divided by 2")
else:
    print(f"{num} is not number divided by 2")
    
if num % 3 == 0:
    print(f"{num} is number divided by 3")
else:
    print(f"{num} is not number divided by 3")
    
if num % 5 == 0:
    print(f"{num} is number divided by 5")
else:
    print(f"{num} is not number divided by 5")
    
if num % 7 == 0:
    print(f"{num} is number divided by 7")
else:
    print(f"{num} is not number divided by 7")
