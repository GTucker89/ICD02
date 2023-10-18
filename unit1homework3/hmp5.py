def area_of_rectangle(length,width):
    if isinstance (length, (int,float)) and isinstance(width, (int,float)):
        return length * width
    else:
        return "invalid input. please input numeric values for length and width."
    
def contains_substring(string, substring):
    if isinstance(string, str) and isinstance(substring, str):
        return substring in string
    else:
        return "invalid"
def average_of_three_floats(num1,num2,num3):
    if all(isinstance(x,float) for x in [num1,num2,num3]):
        return (num1+num2+num3)/3.0
    else:
        return "invalid"
def concatenate_strings(str1,str2):
    if isinstance(str1, str) and isinstance(str2,str):
        return str1+str2
    else:
        return "invalid"
def volume_of_cube(side_len):
    if isinstance(side_len, (int,float)):
        return side_len**3
    else:
        return "invalid"
def number_status(number):
    if isinstance(number, (int, float)):
        if number > 0:
            return "Positive"
        elif number <0:
            return "Negative"
        else:
            "zero"
def circumference_of_circle(radius):
    if isinstance(radius, (int,float)):
        return 2*3.1415926 * radius
    else:
        "invalid"
def 