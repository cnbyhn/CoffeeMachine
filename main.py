from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
is_on = True
coffeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()

while is_on:
  choice = input(f"Please choose your dirnk: {menu.get_items()}")

  if choice == "off":
    is_on = False
  elif choice == "report":
    coffeMaker.report()
    moneyMachine.report()
  elif  not menu.find_drink(choice):
    print("Please re enter your order")
  else:
    drink = menu.find_drink(choice)

    if coffeMaker.is_resource_sufficient(drink):
      cost = drink.cost
      if moneyMachine.make_payment(cost):
        coffeMaker.make_coffee(drink)




