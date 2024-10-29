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
    choice = int(input("Please select a number option (1-4)\n"))
    if choice not in [1, 2, 3, 4]:
        print("Invalid choice, please try again")
    
    


    # Super Calc
    
    
    if choice == 1:
        print('Welcome to the Super-Calc option. Here you can do combination number programming!    ')

        # finish logic

    
    
    
    # Normal Calculator
    
    if choice == 2:
        print('Welcome to the Normal-Calc option. Here you can do normal calculations!\n')
        while True:
            num_1_str = input("Please select an integer number\n")
            try:
                num_1 = int(num_1_str)
            except:
                print('ERROR --- Type a valid int!!! --- ERROR  ')
                continue
            
            num_2_str = input("Please select an integer number\n")
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
            print(f"""Your answer is:\n
                        {num_1_str}   {operator_choice}   {num_2_str}   =   {answer}\n""")
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
                    Binary-Cal 4\n""")
                    break
                case 'Quit':
                    exit(0)
    



    # Roman Calc

    if choice == 3:
        print('Welcome to the Roman-Calc option. Here you can do calculations with Roman Numerals!\n')
        while True:
            roman_1_str = input('Please type a valid Roman Numeral\n')
            try: 
                roman_int = roman_to_int(roman_1_str)
            except:
                print('ERROR --- Invalid Roman Numeral --- ERROR')
                continue
            roman_2_str = input('Please type a valid Roman Numeral\n')
            try:
                roman_int_2 = roman_to_int(roman_2_str)
            except:
                print('ERROR --- Invalid Roman Numeral --- ERROR')
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
                    answer = add(roman_int, roman_int_2)
                case '-':
                    answer = subtract(roman_int, roman_int_2)
                case '*': 
                    answer = multiply(roman_int, roman_int_2)
                case '/':
                    answer = divide(roman_int, roman_int_2) 
            print(f"""Your answer is:\n
                        {roman_1_str}   {operator_choice}   {roman_2_str}   =    {int_to_roman(answer)}\n""")
            
            user_choice = input("""You can continue using Roman Calculator, Go Back to Menu, or Fully Quit\n
            Enter: to continue using Roman Calculator\n
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
                    Binary-Cal 4\n""")
                    break
                case 'Quit':
                    exit(0)




    # Binary Calc

    if choice == 4:
        print('Welcome to the Binary-Calc option. Here you can do calculations with Binary Numbers!\n')  
        while True:
            binary_1 = input('Please type a valid Binary Number\n')
            try:
                binary_1_int = int(binary_1)
                binary_number_1 = binary_to_int(binary_1_int)
            except:
                print('ERROR --- Invalid Binary Number --- ERROR')
                continue
            
            binary_2 = input('Please type a valid Binary Number\n')
            try:
                binary_2_int = int(binary_2)
                binary_number_2 = binary_to_int(binary_2_int)
            except:
                print('ERROR --- Invalid Binary Number --- ERROR')
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
                    answer = add(binary_number_1, binary_number_2)
                case '-':
                    answer = subtract(binary_number_1, binary_number_2)
                case '*': 
                    answer = multiply(binary_number_1, binary_number_2)
                case '/':
                    answer = divide(binary_number_1, binary_number_2) 
            print(f"""Your answer is:\n
                        {binary_1}   {operator_choice}   {binary_2}   =    {int_to_binary(answer)}\n""")
            
            user_choice = input("""You can continue using Binary Calculator, Go Back to Menu, or Fully Quit\n
            Enter: to continue using Roman Calculator\n
            1: to go back to menu\n
            'Quit': to fully quit\n""")
            