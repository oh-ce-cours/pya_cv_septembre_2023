number = 0
for number in  range(100):
    number += 1
    result = number / 3
    if result.is_integer():
        print("Fizz")
        #print(i)
    else:
        result = number / 5
        if result.is_integer():
            print("Buzz")
            #♣print(i)
        else:
            print(number)
            continue
