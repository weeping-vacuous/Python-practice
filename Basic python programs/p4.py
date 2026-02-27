#format spicfiers
price1 = 3014.14159
price2 = -987.65
price3 = 128734.23

print(f"price 1 is ${price1}")
print(f"price 2 is ${price2}")
print(f"price 3 is ${price3}")

print(f"price 1 is ${price1:.1f}")
print(f"price 2 is ${price2:.1f}")
print(f"price 3 is ${price3:.1f}")

print(f"price 1 is ${price1:10}")
print(f"price 2 is ${price2:10}")
print(f"price 3 is ${price3:10}")

print(f"price 1 is ${price1:<10}")
print(f"price 2 is ${price2:<10}")
print(f"price 3 is ${price3:<10}")

print(f"price 1 is ${price1:^10}")
print(f"price 2 is ${price2:^10}")
print(f"price 3 is ${price3:^10}")

print(f"price 1 is ${price1: }")
print(f"price 2 is ${price2: }")
print(f"price 3 is ${price3: }")

print(f"price 1 is ${price1:,}")
print(f"price 2 is ${price2:,.2f}")
print(f"price 3 is ${price3:+,.1f}")