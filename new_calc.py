def num_program():
    pass
    #Список для збереження результатів
    results: list = []

    #Запитуємо скільки ітерацій хоче зробити користувач
    num_iteration: int = int(input("How many times you want to calculate? Enter a number from 1 to 10:"))

    #Якщо користувач введе число ітерацій більше 10, то запросить ввести значення повторно від 1 до 10
    while num_iteration > 10:
            print('Please, enter correct number from 1 to 10:')

    #Якщо ввести від 1 до 10, то запросить введення 1 числа
    chosen_iteration = 0
    while chosen_iteration <= num_iteration:
        print(f'Current iteration: {chosen_iteration}')
        num_1: int = int(input("Enter the 1st number up to 1000: "))
    #Якщо більше 1000, то запросить ввід 1 числа ще раз
        if num_1 > 1000:
            print("Try again with another number less than 1000")
            continue

    #Якщо ввести 666, то закінчить програму
        elif num_1 == 666:
            print("You are on the highway to hell")
            break

    #Після 1 числа запрошує ввід 2
        num_2: int = int(input("Enter the 2nd number up to 1000: "))

    # Якщо більше 1000, то запросить ввід 1 числа ще раз
        if num_2 > 1000:
            print("Try again with another number less than 1000")
            continue

    # Якщо ввести 666, то закінчить програму
        elif num_2 == 666:
            print("You are on the highway to hell")
            break

    # Якщо ввели 2 валідних числа запитує знак для рахування
        while True:
            symbol = input("Enter the character +, -, *, /, %, **: ")
            if symbol == "+":
                result = num_1 + num_2
            elif symbol == '-':
                result = num_1 - num_2
            elif symbol == '*':
                result = num_1 * num_2
            elif symbol == '/':
                result = num_1 / num_2
            elif symbol == '%':
                result = num_1 % num_2
            elif symbol == '**':
                result = num_1 ** num_2

    #Результат рахунків більше 500 виводяться як десяткові дроби
            if result > 500:
                print(f"The answer is: {float(result)}")
                break

    # Результат рахунків до 500 виводяться як цілі числа
            else:
                print(f"The answer is: {int(result)}")
                break

    #Після заданої кількості ітерацій виводиться список всіх проведених розрахунків під час ітерацій
        results.append(result)
        for result in results:
            chosen_iteration += 1
            print(f'Your iteration is: {chosen_iteration}. You have chosen symbol: {symbol}. Your result is {result}.')
num_program()

def string_program():
    #Список для даних з літерою f
    f_list: list = []
    #Загальний список
    results: list = []

    #Запитуємо скільки ітерацій хоче зробити користувач
    num_iteration = int(input("How many times you want to run a program? Enter a number from 2 to 6: "))

    #Якщо користувач введе число ітерацій менше 2 і більше 6, то запросить ввести значення повторно від 2 до 6
    while num_iteration < 2 or num_iteration > 6:
        print('You have entered an invalid value. Please try again.')
        num_iteration = int(input("How many times you want to run a program? Enter a number from 2 to 6: "))

    # Якщо ввести від 1 до 10, то запросить введення 1 числа
    chosen_iteration = 0
    while chosen_iteration <= num_iteration:
        print(f'Current iteration: {chosen_iteration}')
        user_input: str = input("Please, enter your text without numbers: ")

    #Входимо в цикл виконання вимог
        while True:

    #Обираємо додавання чи множення рядків
            operation = input("Choose concatenation (+) or multiplication (*): ")

    #Якщо вибираємо +, то наші значення додадуться разом
            if operation == '+':
                new_string = input("Enter your text: ")
                result = user_input + new_string
                print(f'You have chosen concatenation. Your result is {result}')
                break
    #Якщо вибираємо *б то наше значення помножиться на те число, яке ми введемо
            if operation == '*':
                multiplier = int(input("Enter the multiplier: "))  # Змінна для зберігання множника
                result = user_input * multiplier
                print(f'You have chosen multiplication. Your result is {result}')
            break
    #Розширюємо список з результатами кількості ітерацій
        results.append(result)
        for result in results:
            chosen_iteration += 1
            print(f'Your iteration is: {chosen_iteration}. You have chosen symbol{operation}. Your result is {result}.')
    #Виводимо в окремий список ті значення, які мали букву f
        if 'f' in user_input:
            f_list.append(user_input)
            chosen_iteration += 1
    #Виводимо обидва списки наприкінці програми
    print(f'The list is {f_list}, the results are {results}')
string_program()

def string_program():
    f_list: list = []
    results: list = []

    num_iteration = int(input("How many times you want to run a program? Enter a number from 2 to 6: "))
    while num_iteration < 2 or num_iteration > 6:
        print('You have entered an invalid value. Please try again.')
        num_iteration = int(input("How many times you want to run a program? Enter a number from 2 to 6: "))
        # Якщо ввести від 1 до 10, то запросить введення 1 числа
    chosen_iteration = 0

    while chosen_iteration <= num_iteration:
        print(f'Current iteration: {chosen_iteration}')
        user_input: str = input("Please, enter your text without numbers: ")

        while True:
            operation = input("Choose concatenation (+) or multiplication (*): ")
            if operation == '+':
                new_string = input("Enter your text: ")
                result = user_input + new_string
                print(f'You have chosen concatenation. Your result is {result}')
                break
            if operation == '*':
                multiplier = int(input("Enter the multiplier: "))  # Змінна для зберігання множника
                result = user_input * multiplier
                print(f'You have chosen multiplication. Your result is {result}')
            break

        results.append(result)
        for result in results:
            chosen_iteration += 1
            print(f'Your iteration is: {chosen_iteration}. You have chosen symbol{operation}. Your result is {result}.')
        if 'f' in user_input:
            f_list.append(user_input)
            chosen_iteration += 1
    print(f'The list is {f_list}, the results are {results}')
string_program()

def list_program():
    my_list: list = []

    while True:
        data = input("Enter your elements: ")
        new_string = ",".join(data)
        my_list.append(new_string)
        if data == "50" or data == "Python":
            my_list.remove(new_string)
        print(f'This is your list: {my_list}')
        break
    my_cortege = tuple(my_list)
    print(f"This is your cortege:{my_cortege}")
    while True:
        symbol = input("Select your symbol to perform the action (1 - delete, 2 - add, 3 - clear, 4 - copy:")
        if symbol == "1":
            element = input("Enter the element to delete:")
            if element in my_cortege:
                my_cortege.remove(element)
                print(f"The element is deleted. Your cortege is: {my_cortege}")
            else:
                print("Element is not found")


list_program()

def main():
    while True:
        print("Choose the program: 1 - numbers/strings, 2 - lists/corteges:")
        choose: int = int(input("Enter your choice: "))
        if choose == 1:
            print("Clarify your choice: 1 - numbers, 2 - strings: ")
            while True:
                choice_1: int = int(input("Enter:"))
                if choice_1 == 1:
                    num_program()
                elif choice_1 == 2:
                    string_program()
                    continue
        if choose == 2:
            list_program()
            continue
        else:
            print("Invalid input. Please try again.")
            continue
main()


