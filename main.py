numbers = [12 , 75 , 150 , 180 , 145 , 525 , 50 ]


result_numbers = []
for item in numbers:
    if item > 500:
        break

    if item % 5 ==0 and item <= 150:
        result_numbers.append(item)

print(result_numbers)