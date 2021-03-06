"""
Доповніть програму-банкомат з попереднього завдання таким функціоналом, як використання банкнот.
   Отже, у банкомата повинен бути такий режим як "інкассація", за допомогою якого в нього можна "загрузити" деяку кількість банкнот 
   (вибирається номінал і кількість).
   Зняття грошей з банкомату повинно відбуватись в межах наявних банкнот за наступним алгоритмом - видається мінімальна кількість банкнот наявного номіналу. 
   P.S. Будьте обережні з використанням "жадібного" алгоритму (коли вибирається спочатку найбільша банкнота, 
   а потім - наступна за розміром і т.д.) - в деяких випадках він працює неправильно або не працює взагалі. Наприклад, якщо треба видати 160 грн., 
   а в наявності є банкноти номіналом 20, 50, 100, 500,  банкомат не зможе видати суму (бо спробує видати 100 + 50 + (невідомо), а потрібно було 100 + 20 + 20 + 20 ).
   Особливості реалізації:
   - перелік купюр: 10, 20, 50, 100, 200, 500, 1000;
   - у одного користувача повинні бути права "інкасатора". Відповідно і у нього буде своє власне меню із пунктами:
     - переглянути наявні купюри;
     - змінити кількість купюр;
   - видача грошей для користувачів відбувається в межах наявних купюр;
   - якщо гроші вносяться на рахунок - НЕ ТРЕБА їх розбивати і вносити в банкомат - не ускладнюйте собі життя, та й, наскільки я розумію, 
   банкомати все, що в нього входить, відкладає в окрему касету.
"""


import json
import sys


class BankException(Exception):
    pass


def validate(user_name, user_password):
    valid = False
    is_admin = False
    with open("users_data.json", "r") as users_data:
        data = json.load(users_data)
        for user in data:
            if user_name == user["name"] and user_password == user["password"]:
                valid = True
                if user["role"] == "admin":
                    is_admin = True
                break
    return valid, is_admin


def check_balance(user_name):
    with open(f"{user_name}_balance.txt", "r") as user_balance:
        balance = int(user_balance.readline())
        return f"Current balance: {balance}"


def add_transaction(user_name, old_bal, new_bal):
    if new_bal > old_bal:
        transaction = "deposit"
    else:
        transaction = "withdraw"
    data = {"transaction": transaction, "before": old_bal, "after": new_bal}
    with open(f"{user_name}_transactions.json", "a") as transactions:
        json.dump(data, transactions)
        transactions.write("\n")


def replenish(user_name):
    dep = int(input("How much money do you want to deposit?\n: "))
    with open(f"{user_name}_balance.txt", "r") as user_balance:
        balance = int(user_balance.readline())
    if dep > 0:
        new_balance = balance + dep
        with open(f"{user_name}_balance.txt", "w") as user_balance:
            user_balance.write(str(new_balance))
            add_transaction(user_name, balance, new_balance)
    else:
        print("Wrong input")


def withdraw_balance(num):
    with open("banknotes.json", "r+") as banknotes_change:
        banknotes_load = json.load(banknotes_change)
        keys = list(map(int, banknotes_load.keys()))
    wit_banknotes = []
    counter = 0
    while sum(wit_banknotes) < num:
        skip = False
        if counter + 1 > len(keys):
            raise BankException
        for key in keys:
            if skip:
                break
            elif key + sum(wit_banknotes) <= num and banknotes_load[str(key)] > 0:
                for k in keys:
                    if (num - sum(wit_banknotes) - key) % k == 0 and banknotes_load[str(k)] > 0:
                        wit_banknotes.append(key)
                        banknotes_load[str(key)] -= 1
                        skip = True
                        break
        counter += 1

    a = list(set(wit_banknotes))
    a.sort()
    with open("banknotes.json", "w") as banknotes_change:
        json.dump(banknotes_load, banknotes_change)
    return f"Given banknotes: {wit_banknotes}"


def withdraw(user_name):
    bank_sum = 0
    with open("banknotes.json", "r+") as banknotes, open(f"{user_name}_balance.txt", "r") as balance:
        currency = int(balance.readline())
        load = json.load(banknotes)
        for key, value in zip(load.keys(), load.values()):
            bank_sum += int(key) * value
    wit = int(input(f"Now in stock: {bank_sum}\nHow much money do you want to withdraw?\n: "))
    if wit > 0 and wit % 10 == 0:
        if wit <= bank_sum:
            balance_new = currency - wit
            with open(f"{user_name}_balance.txt", "w") as balance:
                balance.write(str(balance_new))
            add_transaction(user_name, currency, balance_new)
            try:
                print(withdraw_balance(wit))
            except BankException:
                w = int(input("Not enough banknotes in ATM. Please, enter another value\n: "))
                print(withdraw_balance(w))
        else:
            print(f"Not enough money in the ATM. Now in stock: {bank_sum}")
    else:
        print("Please enter positive amount which is multiple by zero")
        withdraw(user_name)


def register():
    reg_name = input("Enter username: ")
    reg_password = input("Enter password: ")
    not_occupied = True
    with open("users_data.json", "r+") as users_data:
        data = json.load(users_data)
        reg_data = {"name": reg_name, "password": reg_password, "role": "user"}
        for user in data:
            if user["name"] == reg_name:
                not_occupied = False
                break
        if not_occupied:
            data.append(reg_data)
            with open("users_data.json", "w") as write_data:
                json.dump(data, write_data)
            with open(f"{reg_name}_balance.txt", "w") as balance, open(f"{reg_name}_transactions.json", "w") as transactions:
                balance.write("0")
        else:
            print("Username is already occupied")


def user_menu(user_name):
    action = int(input("Choose operation:\n1. Check balance\n2. Replenish balance\n3. Withdraw money\n4. Exit\n: "))
    if action == 1:
        print(check_balance(user_name))
    elif action == 2:
        replenish(user_name)
    elif action == 3:
        withdraw(user_name)
    elif action == 4:
        sys.exit()
    else:
        print("Wrong input")


def check_banknotes():
    with open("banknotes.json", "r") as banknotes:
        return json.load(banknotes)


def change_banknotes():
    choice = input("Choose banknote: ")
    with open("banknotes.json", "r+") as banknotes:
        available = json.load(banknotes)
        if choice in available.keys():
            new = int(input("Enter new amount: "))
            if new >= 0:
                available[choice] = new
                with open("banknotes.json", "w+") as changed_banknotes:
                    json.dump(available, changed_banknotes)
            else:
                print("Can't change amount to negative. Please, try again")
                change_banknotes()
        else:
            print("Please, choose from available variants(10, 20, 50, 100, 200, 500, 1000)")
            change_banknotes()


def admin_menu():
    action = int(input("Choose operation:\n1. View available banknotes\n2. Change banknotes\n3. Exit\n: "))
    if action == 1:
        print(check_banknotes())
    elif action == 2:
        change_banknotes()
    elif action == 3:
        sys.exit()
    else:
        print("Wrong input. Please try again")


def start(user_name, user_password):
    if validate(user_name, user_password)[0]:
        if validate(user_name, user_password)[1]:
            admin_menu()
            start(user_name, user_password)
        else:
            user_menu(user_name)
            start(user_name, user_password)
    else:
        reg = int(input("User doesn't exist. Do you want to register?\n1. Yes\n2. No\n: "))
        if reg == 1:
            register()
        else:
            sys.exit()


username = input("Enter username: ")
password = input("Enter password: ")

start(username, password)
