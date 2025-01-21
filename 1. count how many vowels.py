# count vowels
sentence = input("ente a string:")
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
count = 0
for char in sentence:
    if char in vowels:
        count = count + 1
print("number of vowels in a given string is:", count)
