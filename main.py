MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "Money": 0,
}

# TO DO: 1 Prompt user by asking

coffee = True

while coffee:

    order = input('What would you like? (espresso/latte/cappuccino): ')

# TO DO: 4 Check resources sufficient
    if order in MENU.keys():
        coffee = MENU[order]

        if coffee['ingredients']['water'] > resources['water']:
            print('Sorry there is not enough water.')
        if order != 'espresso':
            if coffee['ingredients']['milk'] > resources['milk']:
                print('Sorry there is not enough milk.')
        if coffee['ingredients']['coffee'] > resources['coffee']:
            print('Sorry there is not enough coffee.')

    if order == 'espresso':

        if resources['water'] >= MENU[order]['ingredients']['water'] and resources["coffee"] >= MENU[order]['ingredients']['coffee']:
            print('Please insert coins : ')
            penny = int(input('penny : '))
            nickel = int(input('nickel : '))
            dime = int(input('dime : '))
            quarter = int(input('quarter : '))
            clientMoney = round(((penny * 0.01) + (dime * 0.10) + (nickel * 0.05) + (quarter * 0.25)), 2)
            if clientMoney < MENU[order]['cost']:
                print("Sorry that's not enough money. Money refunded.")
            else:
                if clientMoney == MENU[order]['cost']:
                    pass
                else:
                    print("Here is {:.2} dollars in change".format(clientMoney - MENU[order]['cost']))
                    clientMoney = MENU[order]['cost']

                resources['Money'] += clientMoney
                resources['water'] -= MENU[order]['ingredients']['water']
                resources["coffee"] -= MENU[order]['ingredients']['coffee']

                print('Here is your espresso. Enjoy!')


    elif order == 'latte':

        if resources['water'] >= MENU[order]['ingredients']['water'] and resources["milk"] >= MENU[order]['ingredients']['milk'] and resources["coffee"] >= MENU[order]['ingredients']['coffee']:
            print('Please insert coins : ')
            penny = int(input('penny : '))
            nickel = int(input('nickel : '))
            dime = int(input('dime : '))
            quarter = int(input('quarter : '))
            clientMoney = round(((penny * 0.01) + (dime * 0.10) + (nickel * 0.05) + (quarter * 0.25)), 2)

            if clientMoney < MENU[order]['cost']:
                print("Sorry that's not enough money. Money refunded.")
            else:
                if clientMoney == MENU[order]['cost']:
                    pass
                else:
                    print("Here is {:.2} dollars in change".format(clientMoney - MENU[order]['cost']))
                    clientMoney = MENU[order]['cost']

                resources['Money'] += clientMoney
                resources['water'] -= MENU[order]['ingredients']['water']
                resources["milk"] -= MENU[order]['ingredients']['milk']
                resources["coffee"] -= MENU[order]['ingredients']['coffee']

                print('“Here is your latte. Enjoy!')



    elif order == 'cappuccino':

        if resources['water'] >= MENU[order]['ingredients']['water'] and resources["milk"] >= MENU[order]['ingredients']['milk'] and resources["coffee"] >= MENU[order]['ingredients']['coffee']:
            print('Please insert coins : ')
            penny = int(input('penny : '))
            nickel = int(input('nickel : '))
            dime = int(input('dime : '))
            quarter = int(input('quarter : '))
            clientMoney = round(((penny * 0.01) + (dime * 0.10) + (nickel * 0.05) + (quarter * 0.25)), 2)
            if clientMoney < MENU[order]['cost']:
                print("Sorry that's not enough money. Money refunded.")
            else:
                if clientMoney == MENU[order]['cost']:
                    pass
                else:
                    print("Here is {:.2} dollars in change".format(clientMoney - MENU[order]['cost']))
                    clientMoney = MENU[order]['cost']

                resources['Money'] += clientMoney
                resources['water'] -= MENU[order]['ingredients']['water']
                resources["milk"] -= MENU[order]['ingredients']['milk']
                resources["coffee"] -= MENU[order]['ingredients']['coffee']

                print('“Here is your cappuccino. Enjoy!')


# TO DO: 2 Turn off
    elif order == 'off':
        print('machine is turning off')
        coffee = False


# TO DO: 3 Print report
    elif order == 'report':
        for (key, value) in resources.items():
            print(key + ' : ' + str(value))


