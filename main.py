from resources import espresso, cappuccino, latte
from Coffee_maker import CoffeeMaker
from MoneyMachine import Sales
coffee_maker= CoffeeMaker()
sales_machine= Sales()
while True:
    option = str(input("What would you like”? (espresso/latte/cappuccino): ")).lower()
    if option == 'off':
        print('Turning Off')
        print("Thank you")
        quit()
    elif option == 'report':
        coffee_maker.resource_report()
        sales_machine.profit_report()
    elif option == "latte":
        option = latte()
        sufficient_resource= coffee_maker.is_sufficient(option)
        sufficient_money= sales_machine.is_sufficient_money(option)
        if sufficient_resource:
            if sufficient_money:
                print("Here's your Hot Latte")
                coffee_maker.coffee_processing(option)
    elif option=='espresso':
        option= espresso()
        sufficient_resource = coffee_maker.is_sufficient(option)
        sufficient_money = sales_machine.is_sufficient_money(option)
        if sufficient_resource:
            if sufficient_money:
                print("Here's your Hot Espresso")
                coffee_maker.coffee_processing(option)
    elif option == "cappuccino":
        option= cappuccino()
        sufficient_resource = coffee_maker.is_sufficient(option)
        sufficient_money = sales_machine.is_sufficient_money(option)
        if sufficient_resource:
            if sufficient_money:
                print("Here's your Hot Cappuccino")
                coffee_maker.coffee_processing(option)
    else:
        print("Invalid Coffee type")










