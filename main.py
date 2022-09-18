name = input("add your name:")

if name.isdigit() or name ==" ":
    print(" inter true information!")
    exit()

age = input("add your age:")
if age.isdigit():
    age = int(age)
else:
    print("inter true information!")
    exit()

address = input("add your address:")

if type(name) is str and type(age) is int and type(address) is str:
    print(f" Hello {name} age {age} located in {address} wlecome to our community, Enjoy!")
