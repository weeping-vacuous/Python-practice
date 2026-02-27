# list comprehensions [ expresssions for vlaue in iterable if condition]

grades = [x for x in range(1,11)]
print(grades)

fruits=["orange","Apple","cherry"]
fruits=[fruit.upper() for fruit in fruits]
print(fruits)

nums=[1,-2,3,-4,5,-6]
positive_nums=[num for num in nums if num>=0]
print(positive_nums)