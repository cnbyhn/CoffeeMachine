# CoffeeMachine
The Coffee Project simulates a coffee machine where users can choose from a menu of drinks (e.g., latte, espresso, cappuccino), insert coins to pay for their drinks, and check available resources like water, milk, and coffee. The program manages the menu, processes payments, and makes coffee, ensuring that the machine has enough ingredients before preparing the chosen drink.

# Coffee Project

## Description
The Coffee Project is a simulation of a coffee machine that allows users to order drinks from a menu, pay for them, and check available resources (water, milk, coffee). It handles order processing, payment, and ensures sufficient ingredients are available to prepare the drink.

## Features
- **Menu**: Users can select from different drinks like latte, espresso, and cappuccino.
- **Payment System**: Users insert coins (quarters, dimes, nickels, pennies) to pay for their drinks.
- **Resource Management**: Tracks available resources (water, milk, coffee) and ensures that ingredients are sufficient before preparing the drink.
- **Report Generation**: Users can view the current status of resources and profit.

## Requirements
- Python 3.x

## Files
- `menu.py`: Defines the menu and available drink items.
- `coffee_maker.py`: Models the coffee machine and handles drink preparation.
- `money_machine.py`: Handles coin processing and payment.
- `main.py`: The main file that runs the program and interacts with the user.

## Usage
1. Run the `main.py` file.
2. Select a drink from the menu.
3. Insert coins when prompted.
4. The machine will check if it has sufficient resources to make the drink, process the payment, and then make the coffee.
5. You can also check the machine's resources and profit by typing `report`.

To run the project:
```bash
python main.py
