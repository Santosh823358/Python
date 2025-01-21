#4. removes one string from another string

def remove_substring(string1, string2):
    return string1.replace(string2, '')
string1 = input("Enter a string: ")
string2 = input("Enter string to remove: ")
finalstring = remove_substring(string1, string2)
print(finalstring)
