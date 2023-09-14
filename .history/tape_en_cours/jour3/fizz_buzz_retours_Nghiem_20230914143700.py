def handle_number(number):
    restdiv3 = number%3
    restdiv5 = number%5

    res = ""
    if restdiv3 == 0:
        res += "fizz"
    if restdiv5 == 0:
        res += "buzz"
    return res 

    # if restdiv3 == 0 and restdiv5 == 0:
    #     return f"{number} fizzbuzz"
    # elif restdiv3 == 0:
    #     return f"{number} fizz"
    # elif restdiv5 == 0:
    #     return f"{number} buzz"
    # else:
    #     return f"{number}"

for number in range(1,101):
    handle_number(number)

# values = map(handle_number, range(1,101))
# print("\n".join(list(values)))
