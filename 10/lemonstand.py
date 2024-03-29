import random
def visiting_customers(weather_value,signs,price,foottraffic):
    if signs == 0:
        customers = weather_value*1*foottraffic
    else:
        customers = weather_value*signs*foottraffic
    if price <= 10:
        value = 1
    elif price <= 20:
        value = .8
    elif price <= 30:
        value = .7
    elif price <= 40:
        value = .5
    elif price <= 50:
        value = .3
    elif price <= 100:
        value = .05
    elif price >=500:
        value = 0
    customers = round((customers * value)/moneyvalue,0)
    if rain == True:
        customers = 0

    return customers
def foot_traffic():
    foottraffic = random.randint(50,2000)
    foottraffic = round(foottraffic/100,1)
    return foottraffic
def weather_generator():
    #50 being colder and rainier and 100 being hotter
    weather_value = random.randint(50,100)
    weather_value = round(weather_value/100,2)
    return weather_value
def rain_chance():
    rain_chance = random.randint(30,90)
    return rain_chance
def rainy_chance_check(RainChance):
    if random.randint(0,100)/2 <= RainChance:
        return True
    else:
        return False

lemonprice = 2
adprice = 15
sellingvalue = 0
lemonaidmade = 0
currentads = 0
day = 0
total = 200
totalspent = 0
moneyvalue = 2
counter = 0
rain = False
print("Welcome to lemonade stand! Today is day one and the current price to make one lemonaid is 2 cents. You have 2 dollars and your stand is located in the middle of nowhere, so you need to market your stand. Goodluck! ")
while True:
    day += 1
    print(f"Today is day {day}")
    if counter == 3:
        moneyvalue += .1
        counter = 0
        print(f"Lemonade got Harder to Sell!")
    weather = weather_generator()
    if weather < 0.6:
        chanceOfRain = rain_chance()
        print(f"It is cold with a {chanceOfRain}% chance of rain!")
        rain = rainy_chance_check(chanceOfRain)
    elif weather < 0.75:
        print("It is cool and cloudy today!")
    else:
        print("It is a warm and sunny day!")
    people = foot_traffic()
    if people <0:
        print("There are few people on the streets today")
    elif people <=10:
        print("There are a moderate amount of people on the streets today")
    elif people > 10:
        print("There is a massive amount of people on the street today")
    x = True
    while x == True:
        lemonaidmade = round(abs(int(input(f"Enter how much lemonade you want to make for {lemonprice} cents each: "))),0)
        if lemonaidmade * lemonprice > total:
            print("You dont have enough money")
        else:
            x = False
    x = True
    total = total - (lemonaidmade*lemonprice)
    while x == True:
        currentads = int(input(f"How many ads do you want to make for {adprice} cents each: "))
        if adprice * currentads > total:
            print("You dont have enough money")
            x = True
        else:
            x = False
    total = total - (currentads*adprice)
    totalspent += (currentads *adprice)
    sellingvalue = int(input(f"How much do you want to sell your lemonade for: "))
    totalbought = visiting_customers(weather,currentads,sellingvalue,people)
    if totalbought > lemonaidmade:
        totalbought = lemonaidmade
    total += totalbought * sellingvalue
    if rain == True:
        print("\nIt rained!")
    print(f"\nYou sold {totalbought} lemonades and your total assets is {int(total)} cents!\n")
    counter += 1
    choice_x = True
    choice = None
    while choice_x:
        choice == input("Would you like to continue? Yes or No: ")
        if choice.lower() == "yes":
            choice_x = False
            break
        elif choice.lower() == "no":
            choice_x = False
        else:
            print("Invalid, try again.")
'''My pricing strategy works is a random value from 50 to 2000, this number is the amount of people on the streets meaning that the more people there are the more people come to your stand. Then depending on your price more or less people will come to your stand, then that is multiplied by the number of ads you have, the random number or customers, and the weather value. The weather value is randomly decided from .5 to 1. If I had time I would have liked to make it so I could use different recipes for lemonade to add complexety to my game. The pricing input takes the absolute value of the input.'''