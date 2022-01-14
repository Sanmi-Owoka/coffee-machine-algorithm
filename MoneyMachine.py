

class Sales:
    coins= {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_recieved=0

    def profit_report(self):
        print(f"profit: {self.profit}")

    # def calculate(self):
    #     for coin in self.coins:
    #         self.money_recieved+= int(input(f"Enter number of {coin}: ")) * self.coins[coin]
    #     print(self.money_recieved)

    def is_sufficient_money(self, type):
        try:
            for coin in self.coins:
                self.money_recieved+= int(input(f"Enter number of {coin}: ")) * self.coins[coin]
                print(f"Amount in Dollars ${self.money_recieved}")
            if type.cost<=self.money_recieved:
                change= self.money_recieved - type.cost
                print(f"Here's Your Change ${round(change, 2)}")
                self.profit += type.cost
                self.money_recieved = 0
                return True
            else:
                print("Number of Coins NOT SUFFICIENT")
                return False
        except ValueError:
            print("Input Number of coins")




