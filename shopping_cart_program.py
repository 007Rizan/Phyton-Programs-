foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit) :   ")
    if food.lower() == 'q':
        break

    else:
        price = float(input(f"Enter a price of the {food} :$"))
        foods.append(food)
        prices.append(price)


print (" ------- your shopping cart ------")

for food in foods:
    print(food,end=" ")

for price in prices:
    total = total + price
print( f"\n your shopping cost {total}$")