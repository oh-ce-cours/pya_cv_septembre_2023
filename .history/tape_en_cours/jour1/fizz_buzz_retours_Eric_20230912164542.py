number = 0
for number in  range(100):
    number += 1
    result_3 = number / 3
    result_5 = number / 5
    if result_3.is_integer() and result_5.is_integer():
        print("FizzBuzz")
    else:
        result = number / 5
        if result.is_integer():
            print("Buzz")
            #♣print(i)
        else:
            print(number)
            continue
