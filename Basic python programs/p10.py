#concession stand
menu={"pizza":3.00,
      "burger":1.59,
      "cold drink":.19,
      "popcorn":1.50,
      "French Fries":2.00}

cart=[]
total=0
print("--------Menu-------")
for key,value in menu.items():
    print(f"{key:12}: ${value:.2f}")
print("----------------------")

while True:
    food=input("Select an item(q to quit): ").lower()
    if food=="q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
    elif menu.get(food) is None:
        print("This item is not on our menu,  please select again.")

print("-----------YOUR ORDER---------")
for food in cart:
    total += menu.get(food) 
    print(f"{food} : ${menu.get(food)}",end="     ")
print()
print(f"The total price is: {total:.2f}")