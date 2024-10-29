from roman_calc import roman_to_int, int_to_roman
from normal_calc import add, subtract, multiply, divide
from binary_calc import int_to_binary, binary_to_int

print("""
+========================================================================+
|                                                                        |
|  ____                           ____      _       __     __  _   ___   |
| / ___| _   _ _ __   ___ _ __   / ___|__ _| | ___  \ \   / / / | / _ \  |
| \___ \| | | | '_ \ / _ \ '__| | |   / _` | |/ __|  \ \ / /  | || | | | |
|  ___) | |_| | |_) |  __/ |    | |__| (_| | | (__    \ V /   | || |_| | |
| |____/ \__,_| .__/ \___|_|     \____\__,_|_|\___|    \_/    |_(_)___/  |
|             |_|                                                        |
|                                                                        |
+========================================================================+
      """)
print('Welcome to Super Calc V 1.0 - stable release!')
print("""There are multiple options for your calculating needs:\n
      Super-Calc: 1 \n
      Normal-Calc: 2 \n
      Roman-Calc 3 \n
      Binary-Cal 4""")

quit = False
current_choice = None
while not quit:
    choice = int(input("Please select a number option (1-4)  "))
    if choice not in [1, 2, 3, 4]:
        print("Invalid choice, please try again")
    
    if choice == 1:
        print('Welcome to the Super-Calc option. Here you can do combination number programming!    ')

        # finish logic

    if choice == 2:
        current_choice = 2
        print('Welcome to the Normal-Calc option. Here you can do normal calculations!  ')
        print('')
        while current_choice == 2:

            num_1_str = input("Please select an integer number  ")
            try:
                num_1 = int(num_1_str)
            except:
                print('ERROR --- Type a valid int!!! --- ERROR  ')
                continue
            
            num_2_str = input("Please select an integer number  ")
            try: 
                num_2 = int(num_2_str)
            except:
                print('ERROR --- Type a valid int!!! --- ERROR  ')
                continue
            operator_list = ['+', '-', "/", "*"]

            operator_choice = input("""Please select an operator: \n
            '+' for addition \n
            '-' for subtraction \n
            '*' for multiplication \n
            '/' for division \n""")
            if operator_choice not in operator_list:
                print('ERROR --- Operator is invalid --- ERROR')
                continue

            match operator_choice:
                case '+':
                    answer = add(num_1, num_2)
                case '-':
                    answer = subtract(num_1, num_2)
                case '*': 
                    answer = multiply(num_1, num_2)
                case '/':
                    answer = divide(num_1, num_2) 
            print(f'Your answer is: {answer}')
            user_choice = input("""You can continue using Normal Calculator, Go Back to Menu, or Fully Quit\n
            Enter: to continue using Normal Calculator\n
            1: to go back to menu\n
            'Quit': to fully quit\n""")

            match user_choice:
                case '':
                    continue
                case '1':
                    print("""There are multiple options for your calculating needs:\n
                    Super-Calc: 1 \n
                    Normal-Calc: 2 \n
                    Roman-Calc 3 \n
                    Binary-Cal 4""")
                    break
                case 'Quit':
                    exit(0)
            