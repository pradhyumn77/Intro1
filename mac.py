# name ="Pradhyumn"
# age = 19.5
# last_name = "Gurjar"
# residnece = "Bhopu"
# print("My Name is :" ,name,last_name,"and my age is",age)
# print(type(name))
# print(type(age))
# print(type(last_name))
# print(not False)
# print(not True)
# a = int(input("enter value of A: "))
# b = int(input("enter value of B: "))
# if(a>=b):
#     print(True)
# else:
#     print(False)

# # math_operations.py

# x = [1,2,2,2,1]
# y = x.copy()
# y.reverse()
# z=[1,2,3,4]
# c=z.copy()
# c.reverse()
# if(x==y):
#     print("palindrome")
# else:
#     print("not palindrome")
# z=[1,2,3,4]
# c=z.copy()
# c.reverse()
# if(z==c):
#     print("palindrome")
# else:
#     print("not palindrome")
#     facto


# def factorial(n):
#     """Calculate the factorial of a number."""
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# def nPr(n, r):
#     """Calculate nPr (permutations)."""
#     return factorial(n) / factorial(n - r)

# def nCr(n, r):
#     """Calculate nCr (combinations)."""
#     return factorial(n) / (factorial(r) * factorial(n - r))

# # Input from the user
# n = int(input("Enter the value of n: "))
# r = int(input("Enter the value of r: "))

# # Calculate and display nPr and nCr
# print(f"{n}P{r} (Permutations) = {nPr(n, r)}")
# print(f"{n}C{r} (Combinations) = {nCr(n, r)}")

# Input string
# x = str(input("Enter string: ")) # You can change this to test other strings

# Determine the midpoint
# midpoint = len(x) // 2

# Split the string into two halves
# if len(x) % 2 == 0:
#     # For even length strings
#     first_half = x[:midpoint]
#     second_half = x[midpoint:]
# else:
#     # For odd length strings, ignore the middle character
#     first_half = x[:midpoint]
#     second_half = x[midpoint+1:]

# # Reverse the second half
# second_half_reversed = second_half[::-1]

# # Check if the first half is equal to the reversed second half
# if first_half == second_half_reversed:
#     print("symmetrical")
# else:
#     print("not symmetrical")

# Input string from the user
# x = input("Enter a string: ")

# # Check symmetry by comparing the first half to the second half
# if x[:len(x)//2] == x[-(len(x)//2):]:
#     print("symmetrical")
# else:
#     print("not symmetrical")
# Function to calculate the length of a string without using len()
# def string_length(s):
#     count = 0
#     for _ in s:
#         count += 1
#     return count

# # Input three strings from the user
# str1 = input("Enter the first string: ")
# str2 = input("Enter the second string: ")
# str3 = input("Enter the third string: ")

# # Calculate lengths of each string
# length1 = string_length(str1)
# length2 = string_length(str2)
# length3 = string_length(str3)

# # Determine the minimum length
# if length1 <= length2 and length1 <= length3:
#     min_length = length1
# elif length2 <= length1 and length2 <= length3:
#     min_length = length2
# else:
#     min_length = length3

# # Display the minimum length
# print("The minimum length of the three strings is:", min_length)

# Function to find GCD using recursion
# def find_gcd(a, b):
#     if b == 0:
#         return a
#     else:
#         return find_gcd(b, a % b)

# # Input two numbers from the user
# x = int(input("Enter the value of x: "))
# y = int(input("Enter the value of y: "))

# # Calculate GCD
# gcd = find_gcd(x, y)

# # Display the result
# print("The GCD of", x, "and", y, "is:", gcd)
# def income_tax(x):
#     if(x==0 or x<=300000):
#         return 0
#     if(x>300000 or x<=700000):
#         return 0.05*x
#     if(x>700000 or x<=1000000):
#         return 0.1*x+15000
#     if(x>1000000 or x<=1200000):
#         return 0.15*x+45000
#     if(x>1200000 or x<=1500000):
#         return 0.2*x+90000
#     else:
#         return 0.3*x+150000
    
# x =float(input("Enter your Salary:"))
# Tax_on_Salary=income_tax(x)
# print("The income tax on your salary is ",Tax_on_Salary)

# def convert_base(number, base_from, base_to):
#     # Step 1: Convert the input number to decimal (base 10)
#     decimal_number = int(number, base_from)
    
#     # Step 2: Convert from decimal to the target base
#     if base_to == 2:
#         return bin(decimal_number)  # Convert to binary and remove the '0b' prefix
#     elif base_to == 8:
#         return oct(decimal_number)  # Convert to octal and remove the '0o' prefix
#     elif base_to == 16:
#         return hex(decimal_number)  # Convert to hexadecimal and remove the '0x' prefix
#     elif base_to == 10:
#         return str(decimal_number)  # If target base is decimal, just return the string version of the number
#     else:
#         return "Unsupported base"  # In case of an unsupported base

# # Input from the user
# number = input("Enter the number to convert: ")
# base_from = int(input("Enter the current base of the number (2 for Binary, 8 for Octal, 10 for Decimal, 16 for Hexadecimal): "))
# base_to = int(input("Enter the base to convert to (2 for Binary, 8 for Octal, 10 for Decimal, 16 for Hexadecimal): "))

# # Perform the conversion
# converted_number = convert_base(number, base_from, base_to)
# print(f"The number {number} is in base {base_from} and in converted base is {converted_number} in base {base_to}.")

# # Two sample lists
# list1 = ["Alice", "Bob", "Charlie", "David"]
# list2 = [24, 30, 22, 27]

# # Print table header
# print("{:<10} {:<10}".format("Name", "Age"))
# print("-" * 20)

# # Combine the lists and print each row
# for name, age in zip(list1, list2):
#     print("{:<10} {:<10}".format(name, age))

# def Fibonacci(n):
#     # Recursive function to calculate Fibonacci number
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return Fibonacci(n-1) + Fibonacci(n-2)

# # Take user input for the position of the Fibonacci term
# n = int(input("Enter the position of the Fibonacci number (e.g., 100 for the 100th term): "))

# # Generate the Fibonacci numbers up to the nth term
# list1 = [x for x in range(n)]

# # Filter out the even Fibonacci numbers
# list2 = [i for i in list1 if Fibonacci(i) % 2 == 0]

# # Display the list of even Fibonacci numbers up to nth term
# print(f"Even Fibonacci numbers up to the {n}th term are: {list2}")
# n=int(input("Enter an integer:"))
# a=[]
# for i in range(2,n+1):
#     if(n%i==0):
#         a.append(i)
# a.sort()
# print("Smallest divisor is:",a[0])

# x=int(input("Enter current year : "))
# y=int(input("Enter your birth year : "))
# z=x-y
# print("Your age is: ",z)
# print("*****")
# print("****")
# def remove_nth_index_char(string, n):
#     """Remove the character at the nth index from the given string."""
#     if n < 0 or n >= len(string):
#         print("Index out of range.")
#         return string
#     # Return the string with the nth character removed
#     return string[:n] + string[n+1:]

# # Input from user
# user_string = input("Enter a non-empty string: ")
# index = int(input("Enter the index of the character to remove: "))

# # Display the result
# result = remove_nth_index_char(user_string, index)
# print("String after removing character at index", index, ":", result)

# Python 3 compatible code
# def count_word_occurrences(sentence):
#     """Count occurrences of each word in a given sentence."""
#     # Convert sentence to lowercase to ensure case-insensitivity
#     sentence = sentence.lower()
    
#     # Split the sentence into words by spaces
#     words = sentence.split()
    
#     # Dictionary to store the count of each word
#     word_counts = {}
    
#     # Count each word's occurrences
#     for word in words:
#         if word in word_counts:
#             word_counts[word] += 1
#         else:
#             word_counts[word] = 1
    
#     return word_counts

# # Input from user
# sentence = input("Enter a sentence: ")

# # Get word occurrences and display the results
# word_occurrences = count_word_occurrences(sentence)
# print("Word occurrences in the sentence:")
# for word, count in word_occurrences.items():
#     print(f"{word}: {count}")
# sentence = input("Enter a sentence: ").lower().split()

# word_counts = {}

# for word in sentence:
#     word_counts[word] = word_counts.get(word, 0) + 1

# print(word_counts)

# class Flower:
#     def __init__(self, price, color):
#         self.price = price
#         self.color = color
    
#     def display(self):
#         print(f"Price: {self.price}, Color: {self.color}")

# # Creating objects of the Flower class
# rose = Flower(100, "Red")
# sunflower = Flower(150, "Yellow")

# # Calling the display method for each object
# print("Rose Details:")
# rose.display()

# print("\nSunflower Details:")
# sunflower.display()
# def check_collinear(x1, y1, x2, y2, x3, y3):
#     # Using the area formula to check if the area is 0
#     area = 0.5 * abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))
    
#     # If the area is 0, then the points are collinear
#     if area == 0:
#         return True
#     else:
#         return False

# Input coordinates of three points
# x1 =  int(input("Enter the value ofx1 :"))
# y1 = int(input("Enter the value of y1 : ")) 
# x2 = int(input("Enter the value of x2 : ")) 
# y2 = int(input("Enter the value of y2 : ")) 
# x3= int(input("Enter the value of x3 : ")) 
# y3 = int(input("Enter the value of y3 : ")) 

# # Check if points are collinear
# if check_collinear(x1, y1, x2, y2, x3, y3):
#     print("The points are collinear.")
# else:
#     print("The points are not collinear.")
# Input the sentence from the user
# sentence = input("Enter a sentence: ")

# # Split the sentence into words
# words = sentence.split()

# # Find the longest word using max with key as length of word
# longest_word = max(words, key=len)

# # Print the length of the longest word
# print("The length of the longest word is:", len(longest_word))
# import re

# # Input password from the user
# password = input("Enter your password: ")

# # Check if the password matches the criteria using a regular expression
# if re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@])[A-Za-z\d$#@]{6,16}$', password):
#     print("Password is valid.")
# else:
    # print("Password is invalid.")

# class Book:
#     # Public Attribute
#     book_title = ""
    
#     # Protected Attribute
#     _book_author = ""
    
#     # Private Attribute
#     __book_isbn = ""
    
#     # Constructor to initialize the book details
#     def __init__(self, title, author, isbn):
#         self.book_title = title
#         self._book_author = author
#         self.__book_isbn = isbn
    
# # Taking input from the user for book details
# title = input("Enter the title of the book: ")
# author = input("Enter the author of the book: ")
# isbn = input("Enter the ISBN number of the book: ")

# # Create the Book object using the inputs
# book = Book(title, author, isbn)

# # Display book details
# print(f"\nTitle: {book.book_title}")
# print(f"Author: {book._book_author}")
# print(f"ISBN: {book._Book__book_isbn}")  # Access private attribute directly

# # Optionally, update the author details using the protected attribute
# new_author = input("\nEnter the new author name: ")
# book._book_author = new_author

# Display updated book details
print(f"\nTitle: {book.book_title}")
print(f"Author: {book._book_author}")
print(f"ISBN: {book._Book__book_isbn}")  # Access private attribute directly










