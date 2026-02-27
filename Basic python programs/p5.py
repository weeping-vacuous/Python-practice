#compund interest calculator

principle=float(input("Enter principle: "))
rate=float(input("Enter rate: "))
time=float(input("Enter time: "))

while principle<=0:
    print("Please type in valid principle")
    principle=float(input("Enter principle: "))

while rate<=0:
    print("Please type in valid rate")
    rate=float(input("Enter rate: "))
    
while time<=0:
    print("Please type in valid time")
    time=float(input("Enter time: "))

result = principle*((1+rate/100)**time)
print(f"Balance after {time} year/s: ${result:.2f}")