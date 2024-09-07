# 1. 
length = len("Jenny Balasta")
print("1. Length of the string:", length)

# 2. 
count = len("Hi, I'm Jenny!")
print("2. Number of characters in the string:", count)

# 3.
s = "banana"
result = s[0] + s[1:].replace(s[0], '$')
print("3. Replaced String:", result)

# 4. 
s1, s2 = "Jenny", "Balasta"
swapped = s2[:2] + s1[2:] + " " + s1[:2] + s2[2:]
print("4. Swapped String", swapped)

# 5. 
a, b, c, d = "I", "am", "Jenny", "Balasta!"
concatenated = a + " " + b + " " + c + " " + d
print("5. Concatenated string:", concatenated)

# 6.
str1 = input("6. Enter the first string: ")
str2 = input("6. Enter the second string: ")
concatenated_input = str1 + " " + str2
print("6. Concatenated user input strings:", concatenated_input)

# 7.
name, age = "Jenny", 23
paragraph = f"My name is {name} and I am {age} years old."
print("7. Paragraph:", paragraph)
