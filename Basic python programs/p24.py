#Exception

try:
    number = int(input("Enter a number: "))
    print(1/number)

except ZeroDivisionError:
    print("You cant divide by zero idiot")

except ValueError:
    print("Invalid Input")

except Exception:
    print("Something went wrong")

finally:
    print("This always runs")