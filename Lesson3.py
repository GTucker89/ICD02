import math

def hypo(a,b):
    if isinstance(a,int) or isinstance(a,float):
        if isinstance(b,int) or isinstance(b,float):
            a_sqr = a**2
            b_sqr = b**2
            total_sqr = b_sqr+a_sqr
            return math.sqrt(total_sqr)
        else:
            print("Error: second input is not an int or float")
    else:
        print("Error first input is not an int or float")

print(hypo(4,"ther"))