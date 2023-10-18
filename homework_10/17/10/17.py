# Function to calculate the area of a rectangle
def area_of_rectangle(length, width):
    if isinstance(length, (int, float)) and isinstance(width, (int, float)):
        return round(length * width,2)
    else:
        return "Invalid input. Please provide numeric values for length and width."

# Function to check if a string contains a specific substring
def contains_substring(string, substring):
    if isinstance(string, str) and isinstance(substring, str):
        return substring in string
    else:
        return "Invalid input. Please provide two strings."

# Function to calculate the average of three floats
def average_of_three_floats(num1, num2, num3):
    if all(isinstance(x, float) for x in [num1, num2, num3]):
        return (num1 + num2 + num3) / 3.0
    else:
        return "Invalid input. Please provide three floating-point numbers."

# Function to concatenate two strings
def concatenate_strings(str1, str2):
    if isinstance(str1, str) and isinstance(str2, str):
        return str1 + str2

# Function to calculate the volume of a cube
def volume_of_cube(side_length):
    if isinstance(side_length, (int, float)):
        return side_length ** 3

# Function to check if a number is positive, negative, or zero
def check_number_status(number):
    if isinstance(number, (int, float)):
        if number > 0:
            return "Positive"
        elif number < 0:
            return "Negative"
        else:
            return "Zero"

# Function to calculate the circumference of a circle
def circumference_of_circle(radius):
    if isinstance(radius, (int, float)):
        return 2 * 3.141592653589793 * radius

# Function to count the number of occurrences of a character in a string
def count_char_occurrences(string, char):
    if isinstance(string, str) and isinstance(char, str) and len(char) == 1:
        return string.count(char)

# Function to calculate the percentage of a number
def calculate_percentage(number, percentage):
    if isinstance(number, (int, float)) and isinstance(percentage, (int, float)):
        return (percentage / 100) * number

# Function to find the absolute difference between two numbers
def absolute_difference(num1, num2):
    if all(isinstance(x, (int, float)) for x in [num1, num2]):
        return abs(num1 - num2)

# Function to capitalize the first letter of a string
def capitalize_first_letter(string):
    if isinstance(string, str):
        return string.capitalize()

# Function to calculate the square of a number
def square(number):
    if isinstance(number, (int, float)):
        return number ** 2

# Function to find the maximum of two numbers
def max_of_two(num1, num2):
    if all(isinstance(x, (int, float)) for x in [num1, num2]):
        if num1 > num2:
            return num1
        else:
            return num2

# Function to calculate the square root of a number
def square_root(number):
    if isinstance(number, (int, float)) and number >= 0:
        return number ** 0.5

# Function to find the length of a string
def length(input_data):
    if isinstance(input_data, str):
        return len(input_data)
    
lengt = float(input("Enter length:"))
width = float(input("Enter width:"))
print(area_of_rectangle(lengt, width))
strin = input("Enter string: ")
substrin = input("Enter substring: ")
print(f"Substring {substrin} is present: {contains_substring(strin,substrin)}")
num1 = float(input("Enter float: "))
num2 = float(input("Enter float: "))
num3 = float(input("Enter float: "))
print(f"The average is {round(average_of_three_floats(num1,num2,num3),2)}")
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")
print(concatenate_strings(string1,string2))
num1 = float(input("Enter length of cube: "))
print(round(volume_of_cube(num1),2))
num1 = float(input("Enter number: "))
print(f"Number status is {check_number_status(num1)}")
num1 = float(input("Enter radius of a circle"))
print(f"The circumfrenece is {round(circumference_of_circle(num1),2)}")
string1 = input("Enter string")
char1 = input("Enter char: ")
print(f"{char1} appears {count_char_occurrences(string1, char1)} in {string1}")
num1 = float(input("Enter number: "))
num2 = float(input("Enter percentage: "))
print(f"{num2} percent of {num1} is {round(calculate_percentage(num1,num2),2)}")
num1 = float(input("Enter number: "))
num2 = float(input("Enter number: "))
print(f"The absolute difference is: {round(absolute_difference(num1,num2),2)}")

