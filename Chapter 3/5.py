import cmath

def coffeeCost():
    coffee_price = 10.50
    shipping_cost = 0.86
    fixed_cost = 1.50

    each_shipping_cost = shipping_cost + fixed_cost

    total_cost = coffee_price + each_shipping_cost

    print("The cost of an order is ", total_cost)

coffeeCost()
