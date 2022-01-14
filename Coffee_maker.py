class CoffeeMaker:
    def __init__(self):
        self.ingredients = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def resource_report(self):
        print(f"Water: {self.ingredients['water']}ml")
        print(f"Milk: {self.ingredients['milk']}ml")
        print(f"coffee: {self.ingredients['coffee']}g")


    answer=''

    def is_sufficient(self, choice_coffee):
        test= True
        for key in self.ingredients:
            if choice_coffee.ingredients[key] > self.ingredients[key]:
                print(f"We are low on {key}")
                print(f"Please check back later")
                test= False
                quit()
        return test

    def coffee_processing(self, choice_coffee):
        for item in self.ingredients:
            self.ingredients[item] -= choice_coffee.ingredients[item]





            # if self.ingredients[key] >= choice_coffee.ingredients[key]:
            #     self.ingredients[key] -= choice_coffee.ingredients[key]
            # else:
            #     return "Resource is insufficient"
