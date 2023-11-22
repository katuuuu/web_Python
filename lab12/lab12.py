
def get_balance(name,transactions):
    balance = 0
    for elem in transactions:
        if elem["name"] == name:
            balance += elem["amount"]
    return balance

def count_debts(names, amount, transactions):
    my_dict = {}
    for i in range(len(names)):
        for elem in transactions:
            if elem["name"] == names[i] and names[i] not in my_dict:
                balance = get_balance(elem["name"], transactions)
                if balance >= amount:
                    my_dict[names[i]] = 0
                else:
                    my_dict[names[i]] = amount - balance

            if names[i] not in my_dict:
                balance = get_balance(names[i], transactions)
                if balance >= amount:
                    my_dict[names[i]] = 0
                else:
                    my_dict[names[i]] = amount - balance
    return my_dict





transactions = [ {"name": "Василий", "amount": 500}, {"name": "Петя", "amount": 100}, {"name": "Василий", "amount": -300}, ]

get_balance("Василий", transactions)
count_debts(["Василий", "Петя", "Вова"], 150, transactions)