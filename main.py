first = (input("inter the first number:"))
if first.isdigit():
    first = int(first)
else:
    print(" inter true values!")
    exit()

second = (input("inter the second number:"))
if second.isdigit():
    second= int(second)
else:
    print(" inter true values!")
    exit()

third = (input("inter the third number:"))
if third.isdigit():
    third = int(third)
else:
    print(" inter true values!")
    exit()

fourth = (input("inter the fourth number:"))
if fourth.isdigit():
    fourth = int(fourth)
else:
    print(" inter true values!")
    exit()

fifth = (input("inter the fifth number:"))
if fifth.isdigit():
    fifth = int(fifth)
else:
    print(" inter true values!")
    exit()


list = [first, second , third , fourth , fifth]
print(max(list))
print(min(list))

