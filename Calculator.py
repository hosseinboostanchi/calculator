def calculate():
    number1 = int(input("enter your number1: "))

    number2 = int(input("enter your number2: "))

    operation = input('''
    Please type in the math operation you would like to complete:                  
    + for addition
    - for menha
    * for zarb
    / for taqsim              
    ''')   

    if operation == '+':
        print(number1 + number2)

    elif operation == '-':
        print(number1 - number2)

    elif operation == '*':
        print(number1 * number2)

    elif operation == '/':
        print(number1 / number2)

    else:
        print("You have not typed a valid operator, please run the program again.")

    again()

def again():
    cal_again = input('''Do you want to calculate again?
     Please type Y for YES or N for NO.
     ''')
    if cal_again == 'Y':
        calculate()
    elif cal_again == 'N':
        print('see you later.')
    else:
        again()

calculate()


