import math

number1 = input(" Enter the first number:")
if number1.isalpha() or number1 == " ":
    print(" you should inter true value")
    exit()

print('_____________________')
print("1. + \n2. - \n3. * \n4. / \n5. ^ \n6. % ")
operation = input(" Enter the operation: \n")

number2 = input(" Enter the second number:\n")

if operation == "1" or operation == '+':
    sum = float(number1) + float(number2)
    print(f"The result is {sum}")

if operation == "2" or operation == "-":
    sum = float(number1) - float(number2)
    print(f"the result is {sum}")

if operation == "3" or operation == "*":
    sum = float(number1) * float(number2)
    print(f"the result is {sum}")

if operation == "4" or operation == "/":
    sum = float(number1) / float(number2)
    print(f"the result is {sum}")

if operation == "5" or operation == "^":
    sum = float(number1) ^ float(number2)
    print(f"the result is {sum}")

if operation == "6" or operation == "%":
    sum = float(number1) % float(number2)
    print(f"the result is {sum}")

print("__________________")
op = input("1.Round \n2.Floor \n3.Ceil \n4.Integer \n5.Exit \nEnter the operation for result:")
if op == "1":
    print(f" the final result is {round(sum)}")
elif op == "2":
    print(f"the final result is {math.floor(sum)} ")
elif op == "3":
    print(f"the final result is {math.ceil(sum)}")
elif op == "4":
    print(f"the final result is {int(sum)}")
elif op == "5":
    print(sum)
    exit()
