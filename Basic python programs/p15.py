word = "APPLE"

letter=input("Guess a letter in the secret word: ")

if letter in word:
    print(f"There is {letter} in word")
else:
    print(f"There is no {letter} in word")