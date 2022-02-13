def particular_num():
    previous_result1, previous_result2, n, sum1 = 0, 1, 0, 0
    try:
        n = int(input("Which Fibonacci number do you want: "))
    except ValueError:
        print("Invalid Input!")
        exit()

    if n == 0:
        print(0)
        exit()
    elif n == 1:
        print(1)
        exit()

    for num in range(n - 1):
        sum1 = previous_result1 + previous_result2
        previous_result1 = previous_result2
        previous_result2 = sum1
    print(sum1)


def next_num():
    end, num, previous_result1, previous_result2 = False, 0, 1, 0
    print("First Number: 0")
    while not end:
        num = previous_result1 + previous_result2
        previous_result1 = previous_result2
        previous_result2 = num
        print(f"The Next Number: {num}")
        ask = input("Do you want to end the program?\n(y)es! | (n)o!\n> ")
        if ask.lower() == "y":
            end = True


print("Hello! This Program will give you Fibonacci Series!")
decision = 0

try:
    decision = int(input("Which way do you want to find your Fibonacci number?\n"
                         "(1) I've a particular number. Find which fibonacci number is at that number's position\n(2) "
                         "Keep giving me the next Fibonacci Number. I'll tell when to end (it's annoying\nDecision: "))
except ValueError:
    print("Invalid Input!"), exit()

if decision == 1:
    particular_num()
elif decision == 2:
    next_num()
