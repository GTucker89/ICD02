length = float(input("Enter the length of the walls in meters: "))
width = float(input("Enter the width of the walls in meters: "))
height = float(input("Enter the height of the house in meters: "))
costpbrick = float(input("Enter cost per brick in meters: "))
bheight = float(input("Enter the height of the brick in meters: "))
blength = float(input("Enter the length of the brick in meters: "))
bwidth = float(input("Enter the width of the brick in meters: "))

warea = length*width
barea = blength*bheight
totalwarea = warea * 4
totalbricks = round(totalwarea/height, 0)
cost = totalbricks*costpbrick

print(f"The total surface area of the house is {totalwarea}, number of bricks you need is {totalbricks}, and that will cost {cost}.")


