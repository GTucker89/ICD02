'''
import math
print(f"{math.pi:.3f}")

print(f"${29.99:.2f}")

print(f"{0.075:.2%}")

print(f"{0.25:.1%}")

city = input("Enter City: ")
print(f"{city:<15}")

temp = input("Enter temp: ")
print(f"{temp:^10}")

item = "product"
price = 29.99
quantity = 3
total = price * quantity
print(f"Item    Price  Quantity Total")
print(f"{item:.<7} {price:.>1} {quantity:>9} {total:>1}")
'''

city = "City"
pop = "Population"
area = "Area (sq km)"
c1 = "NY"
c1p = "8,398,748"
c1a = "468.19"
c2 = "LA"
c2p = "3,990,456"
c2a = "503.79"
c3 = "CH"
c3p = "2,639,976"
c3a = "227.63"

print(f"{city:<4} {pop:>15} {area:>17}")
print(f"{c1:>4} {c1p:>15} {c1a:>17}")
print(f"{c2:>4} {c2p:>15} {c2a:>17}")
print(f"{c3:>4} {c3p:>15} {c3a:>17}")
