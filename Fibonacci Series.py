import pyinputplus as pyip
import time

def particular_num(previous_result1, previous_result2):
    n, sum1 = 0, 0
    n = pyip.inputInt("\nWhich Fibonacci number do you want: ")

    if n == 0:
        print(0), exit()
    elif n == 1:
        print(1), exit()

    for num in range(n - 1):
        sum1 = previous_result1 + previous_result2
        previous_result1 = previous_result2
        previous_result2 = sum1
    print(sum1)


def next_num(previous_result1, previous_result2):
    end, num = False, 0
    print("\nFirst Fib-Number: 0")
    while not end:
        num = previous_result1 + previous_result2
        previous_result1 = previous_result2
        previous_result2 = num
        print(f"The Next Fib-Number: {num}")
        ask = pyip.inputStr("Do you want to end the program?\n(Y)es! | (N)o!\n> ", allowRegexes=r'y|n|Y|N')
        if ask.lower() == "y":
            print("Hoping you liked the program :)")
            break
        time.sleep(0.5)


print("Hello! This Program will give you Fibonacci Series!")
previous_result1, previous_result2 = 1, 0
decision = pyip.inputInt("\nWhich way do you want to find your Fibonacci number?\n"
                         "(1) I've a specific number. Find which fibonacci number is at that number's position\n(2)"
                         " Keep giving me the next Fibonacci Number. I'll say when to end (annoying)"
                         "\nDecision: ", allowRegexes=r'1|2')
if decision == 1:
    particular_num(previous_result1, previous_result2)
elif decision == 2:
    next_num(previous_result1, previous_result2)
