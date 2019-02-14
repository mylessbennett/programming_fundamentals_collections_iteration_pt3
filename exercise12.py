#--------------------------------------------------------------------------------------------------------------
# PizzaMaker wants to handle bulk orders of pizzas, with varying amounts of toppings on each.
# Ask the user for a number of pizzas - call it quantity.
# We then want to ask the user for quantity more numbers - the number of toppings on that pizza - and print them out as in the following example.
#--------------------------------------------------------------------------------------------------------------
quantity = int(input("How many pizzas do you want to order? "))

def get_pizza_order(quantity):
    for i in range (1, quantity + 1):
        toppings = int(input("How many toppings do you want on pizza {}? ".format(i)))
        print("You have ordered a pizza with {} toppings.".format(toppings))
    return

get_pizza_order(quantity)
