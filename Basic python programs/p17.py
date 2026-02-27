def is_weekend(day):
    match day:
        case "Sunday":
            return True
        case "Saturday":
            return True
        case _:
            return False
        
print(is_weekend("Saturday"))