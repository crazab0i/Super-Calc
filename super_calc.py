from roman_calc import roman_to_int, int_to_roman
from normal_calc import add, subtract, multiply, divide
from binary_calc import int_to_binary, binary_to_int

print("""\n
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
      \n""")
print('Welcome to Super Calc V 1.0 - stable release!')
print("""\nThere are multiple options for your calculating needs:\n
      Super-Calc: 1 \n
      Normal-Calc: 2 \n
      Roman-Calc 3 \n
      Binary-Cal 4\n""")

valid_selection_exit = ['Quit', '', '1']
while True:
    choice = int(input("\nPlease select a number option (1-4)\n\n"))
    if choice not in [1, 2, 3, 4]:
        print("\nInvalid choice, please try again\n")
    
    


    # Super Calc
    
    
    if choice == 1:
        print('\nWelcome to the Super-Calc option. Here you can do combination number programming!\n')
        while True:
            valid_selection = ['1', '2', '3']
            input_selection_1 = input("""\nSelect a input type:\n
            1 - Normal\n
            2 - Roman Numeral\n
            3 - Binary\n\n""")
            if input_selection_1 not in valid_selection:
                print("\nERROR --- Invalid Selection!!! --- EEROR\n")
                continue
            number_input_1 = input("\nEnter a value corresponding to your selection\n\n")

            match input_selection_1:
                case '1':
                    try:
                        number_input_int_1 = int(number_input_1)
                    except:
                        print('\nERROR --- Invalid Input!!! --- ERROR\n')
                        continue
                case '2':
                    try:
                        number_input_int_1 = roman_to_int(number_input_1)
                    except:
                        print('\nERROR --- Invalid Input!!! --- ERROR\n')
                        continue
                case '3':
                    try:
                        number_input_int_1 = binary_to_int(number_input_1)
                    except:
                        print('\nERROR --- Invalid Input!!! -- ERROR\n')
                        continue
            
            input_selection_2 = input("""\nSelect a input type:\n
            1 - Normal\n
            2 - Roman Numeral\n
            3 - Binary\n\n""")
            if input_selection_2 not in valid_selection:
                print("\nERROR --- Invalid Selection!!! --- EEROR\n")
                continue
            number_input_2 = input("\nEnter a value corresponding to your selection\n\n")
            
            match input_selection_2:
                case '1':
                    try:
                        number_input_int_2 = int(number_input_2)
                    except:
                        print('\nERROR --- Invalid Input!!! --- ERROR\n')
                        continue
                case '2':
                    try:
                        number_input_int_2 = roman_to_int(number_input_2)
                    except:
                        print('\nERROR --- Invalid Input!!! --- ERROR\n')
                        continue
                case '3':
                    try:
                        number_input_int_2 = binary_to_int(int(number_input_2))
                    except:
                        print('\nERROR --- Invalid Input!!! -- ERROR\n')
                        continue
            
            operator_list = ['+', '-', "/", "*"]

            operator_choice = input("""\nPlease select an operator: \n
            '+' for addition \n
            '-' for subtraction \n
            '*' for multiplication \n
            '/' for division \n\n""")
            if operator_choice not in operator_list:
                print('\nERROR --- Operator Is Invalid!!! --- ERROR\n')
                continue

            match operator_choice:
                case '+':
                    answer = add(number_input_int_1, number_input_int_2)
                case '-':
                    answer = subtract(number_input_int_1, number_input_int_2)
                case '*': 
                    answer = multiply(number_input_int_1, number_input_int_2)
                case '/':
                    answer = divide(number_input_int_1, number_input_int_2)
            
            answer_selection = input("""\nPlease select an answer format:\n
            1 - Normal\n
            2 - Roman Numeral\n
            3 - Binary\n\n""")

            if not answer_selection in valid_selection:
                print('\nERROR --- Invalid Selection!!! --- ERROR\n')
                continue
            
            match answer_selection:
                case '1':
                    print(f"""\nYour result:\n
                    {number_input_1}   {operator_choice}   {number_input_2}   =   {answer}\n""")
                case '2':
                    print(f"""\nYour result:\n
                    {number_input_1}   {operator_choice}   {number_input_2}   =   {int_to_roman(answer)}\n""")
                case '3':
                    print(f"""\nYour result:\n
                    {number_input_1}   {operator_choice}   {number_input_2}   =   {int_to_binary(answer)}\n""")
            
            user_choice = input("""\nYou can continue using Normal Calculator, Go Back to Menu, or Fully Quit\n
            Enter: to continue using Normal Calculator\n
            1: to go back to menu\n
            'Quit': to fully quit\n\n""")
            
            if user_choice not in valid_selection_exit:
                print("\nERROR --- Invalid Selection!!! --- ERROR\n")
                continue
            match user_choice:
                case '':
                    continue
                case '1':
                    print("""\nThere are multiple options for your calculating needs:\n
                    Super-Calc: 1 \n
                    Normal-Calc: 2 \n
                    Roman-Calc 3 \n
                    Binary-Cal 4\n""")
                    break
                case 'Quit':
                    exit(0)



                    
    # Normal Calculator
    
    if choice == 2:
        print('\nWelcome to the Normal-Calc option. Here you can do normal calculations!\n')
        while True:
            num_1_str = input("\nPlease select an integer number\n\n")
            try:
                num_1 = int(num_1_str)
            except:
                print('\nERROR --- Type A Valid Int!!! --- ERROR\n')
                continue
            
            num_2_str = input("\nPlease select an integer number\n\n")
            try: 
                num_2 = int(num_2_str)
            except:
                print('\nERROR --- Type A Valid Int!!! --- ERROR\n')
                continue
            operator_list = ['+', '-', "/", "*"]

            operator_choice = input("""\nPlease select an operator: \n
            '+' for addition \n
            '-' for subtraction \n
            '*' for multiplication \n
            '/' for division \n\n""")
            if operator_choice not in operator_list:
                print('\nERROR --- Operator Is Invalid!!! --- ERROR\n')
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
            print(f"""\nYour answer is:\n
                        {num_1_str}   {operator_choice}   {num_2_str}   =   {answer}\n""")
            user_choice = input("""\nYou can continue using Normal Calculator, Go Back to Menu, or Fully Quit\n
            Enter: to continue using Normal Calculator\n
            1: to go back to menu\n
            'Quit': to fully quit\n\n""")
            
            if user_choice not in valid_selection_exit:
                print("\nERROR --- Invalid Selection!!! --- ERROR\n")
                continue
            match user_choice:
                case '':
                    continue
                case '1':
                    print("""\nThere are multiple options for your calculating needs:\n
                    Super-Calc: 1 \n
                    Normal-Calc: 2 \n
                    Roman-Calc 3 \n
                    Binary-Cal 4\n""")
                    break
                case 'Quit':
                    exit(0)
    



    # Roman Calc

    if choice == 3:
        print('\nWelcome to the Roman-Calc option. Here you can do calculations with Roman Numerals!\n')
        while True:
            roman_1_str = input('\nPlease type a valid Roman Numeral\n\n')
            try: 
                roman_int = roman_to_int(roman_1_str)
            except:
                print('\nERROR --- Invalid Roman Numeral!!! --- ERROR\n')
                continue
            roman_2_str = input('\nPlease type a valid Roman Numeral\n\n')
            try:
                roman_int_2 = roman_to_int(roman_2_str)
            except:
                print('\nERROR --- Invalid Roman Numeral!!! --- ERROR\n')
                continue
            
            operator_list = ['+', '-', "/", "*"]

            operator_choice = input("""\nPlease select an operator: \n
            '+' for addition \n
            '-' for subtraction \n
            '*' for multiplication \n
            '/' for division \n\n""")
            if operator_choice not in operator_list:
                print('\nERROR --- Operator is invalid!!! --- ERROR\n')
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
            print(f"""\nYour answer is:\n
                        {roman_1_str}   {operator_choice}   {roman_2_str}   =    {int_to_roman(answer)}\n""")
            
            user_choice = input("""\nYou can continue using Roman Calculator, Go Back to Menu, or Fully Quit\n
            Enter: to continue using Roman Calculator\n
            1: to go back to menu\n
            'Quit': to fully quit\n\n""")

            if user_choice not in valid_selection_exit:
                print('\nERROR --- Invalid Selection!!! ---ERROR\n')
                continue
        
            match user_choice:
                case '':
                    continue
                case '1':
                    print("""\nThere are multiple options for your calculating needs:\n
                    Super-Calc: 1 \n
                    Normal-Calc: 2 \n
                    Roman-Calc 3 \n
                    Binary-Cal 4\n""")
                    break
                case 'Quit':
                    exit(0)




    # Binary Calc

    if choice == 4:
        print('\nWelcome to the Binary-Calc option. Here you can do calculations with Binary Numbers!\n')  
        while True:
            binary_1 = input('\nPlease type a valid Binary Number\n\n')
            try:
                binary_1_int = int(binary_1)
                binary_number_1 = binary_to_int(binary_1_int)
            except:
                print('\nERROR --- Invalid Binary Number --- ERROR')
                continue
            
            binary_2 = input('\nPlease type a valid Binary Number\n\n')
            try:
                binary_2_int = int(binary_2)
                binary_number_2 = binary_to_int(binary_2_int)
            except:
                print('\nERROR --- Invalid Binary Number --- ERROR')
                continue

            operator_list = ['+', '-', "/", "*"]

            operator_choice = input("""\nPlease select an operator: \n
            '+' for addition \n
            '-' for subtraction \n
            '*' for multiplication \n
            '/' for division \n\n""")
            if operator_choice not in operator_list:
                print('\nERROR --- Operator is invalid --- ERROR')
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
            print(f"""\nYour answer is:\n
                        {binary_1}   {operator_choice}   {binary_2}   =    {int_to_binary(answer)}\n""")
            
            user_choice = input("""\nYou can continue using Binary Calculator, Go Back to Menu, or Fully Quit\n
            Enter: to continue using Roman Calculator\n
            1: to go back to menu\n
            'Quit': to fully quit\n\n""")
            
            if user_choice not in valid_selection_exit:
                print('\nERROR --- Invalid Selection!!! ---ERROR\n')
                continue

            match user_choice:
                case '':
                    continue
                case '1':
                    print("""\nThere are multiple options for your calculating needs:\n
                    Super-Calc: 1 \n
                    Normal-Calc: 2 \n
                    Roman-Calc 3 \n
                    Binary-Cal 4\n""")
                    break
                case 'Quit':
                    exit(0)