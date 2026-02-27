size=int(input("Enter the size: "))

symbols= input("Enter the symbol: ")

for x in range(1,size+1):
    for y in range(1,x+1):
        print(symbols,end="")
    print()
   