from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

def main():
    prompt_m = "What would you like? (espresso/latte/cappuccino/): "
    machine_working = True

    while machine_working:
        user_input = input(prompt_m).lower()
        if user_input == "off":
            machine_working = False
        elif user_input == "report":
            coffee_maker.report()
            money_machine.report()
        elif user_input in ["espresso", "latte", "cappuccino"]:
            drink = menu.find_drink(user_input)
            if coffee_maker.is_resource_sufficient(drink):
                # cost = float(menu.get_cost(user_input))
                # 이 부분을 menu.get_cost(user_input).cost로 처리했음
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
        else:
            print("Check Your Spelling.")

if __name__ == '__main__':
    main()

