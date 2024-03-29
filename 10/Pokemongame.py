import random
#Need to be seperate functions
blaze = "come back"
torrent = "come back"
overgrow = "come back"
Volt_absorb = "come back"
gluttony = "come back"
#creates the moves
# #1 = power, #2 = type #3 Attack type # accuarcy
water_gun = ["Water Gun", 40, "Water", "Special", 100, None, None]
magical_leaf = ["Magical Leaf", 60, "Grass", "Special", 100, None, None]
growl = ["Growl", 0, "Normal", "Status", 100, None, None]
tackle = ["Tackle", 40, "Normal", "Physical", 100, None, None]
scratch = ["Scratch", 40, "Normal", "Physical", 100, None, None]
quick_attack = ["Quick Attack", 40, "Normal", "Physical", 100, 1, None]
headbutt = ["Headbutt", 70, "Normal", "Physical", 100, None, (30, "paralysis")]
body_slam = ["Body Slam", 85, "Normal", "Physical", 100, None, (30, "paralysis")]
hyper_voice = ["Hyper Voice", 90, "Normal", "Special", 100, None, None]
double_slap = ["Double Slap", 15, "Normal", "Physical", 85, None, (2, 5)]
explosion = ["Explosion", 250, "Normal", "Physical", 100, None, None]
protect = ["Protect", 0, "Normal", "Status", 100, 4, None]
supersonic = ["Supersonic", 0, "Normal", "Status", 55, None, "confusion"]
leer = ["Leer", 0, "Normal", "Status", 100, None, None]
pound = ["Pound", 40, "Normal", "Physical", 100, None, None]
uproar = ["Uproar", 90, "Normal", "Special", 100, None, "trapped"]
detect = ["Detect", 0, "Fighting", "Status", 100, 4, None]
rock_smash = ["Rock Smash", 40, "Fighting", "Physical", 100, None, (50, 1, "lower_defense")]
quickguard = ["Quick Guard", 0, "Fighting", "Status", 100, None, None]
rock_throw = ["Rock Throw", 50, "Rock", "Physical", 90, None, None]
ember = ["Ember", 40, "Fire", "Special", 100, None, (10, "burn")]
flamethrower = ["Flamethrower", 90, "Fire", "Special", 100, None, (10, "burn")]
fire_blast = ["Fire Blast", 110, "Fire", "Special", 85, None, (30, "burn")]
fire_punch = ["Fire Punch", 75, "Fire", "Physical", 100, None, (10, "burn")]
flame_charge = ["Flame Charge", 50, "Fire", "Physical", 100, None, (1, "raise_speed")]
will_o_wisp = ["Will-o-Wisp", 0, "Fire", "Status", 100, None, "burn"]
fire_spin = ["Fire Spin", 35, "Fire", "Special", 85, None, (1, "trapped")]
heat_wave = ["Heat Wave", 95, "Fire", "Special", 90, None, (10, "burn")]
leafage = ["Leafage", 40, "Grass", "Physical", 100, None, None]
megadrain = ["Mega Drain", 40, "Grass", "Special", 100, None, (100,"heal")]
peck = ["Peck", 35, "Flying", "Physical", 100, None, None]
pluck = ["Pluck", 60, "Flying", "Physical", 100, None, None]
thundershock = ["Thunder Shock", 40, "Electric", "Special", 100, None, (10, "paralysis")]
spark = ["Spark", 65, "Electric", "Physical", 100, None, (30, "paralysis")]
sandattack = ["Sand Attack", 0, "Ground", "Status", 100, None, None]
tail_whip = ["Tailwhip", 0, "Normal", "Status", 0, 100, None]
baby_doll_eyes = ["Baby Doll Eyes", 0, "Fairy", "Status", 100, None, (100,"lower_attack")]
covet = ["Covet", 60, "Normal", "Physical", 100, None, None]
bestow = ["Bestow", 15, "Normal", "Status", 0, 100, None]
defense_curl = ["Defense Curl", 0, "Normal", "Status", 100, None, None]
mud_slap = ["Mud Slap", 20, "Ground", "Special", 100, None, (100, 1, "lower_accuracy")]
rock_polish = ["Rock Polish", 0, "Rock", "Status", 100, None, None]
rock_tomb = ["Rock Tomb", 60, "Rock", "Physical", 95, None, (100, 1, "lower_speed")]
smack_down = ["Smack Down", 50, "Rock", "Physical", 100, None, None]




#0 Type 1 #1 Type 2# Base HP #3 Base Attack #4 Base Defense #5 Base Special Attack #6 Base Special Defense #7 Base Speed #8 evolution level #9 Ability 1 #10 Ability 2 #11 Hidden Ability #12 Pokemon Name #13 Move Learned at level 1 #14 Move learned at level 1 #15 Move Learned at level 3 #16 Move Learned at level 6 #17 Move Learned at Level 9 #18 Move Level 12 #19 Move learned at Level 15
torchic = ["Fire","None",45,60,40,70,50,45,16,"Blaze","None","Speed Boost","Torchic",growl,scratch,ember,quick_attack,flame_charge,detect,sandattack]
mudkip = ["Water","None",50,70,50,50,50,40,16,"Torrent", "None", "Damp","Mudkip",growl, tackle, water_gun, rock_smash, rock_throw, protect, supersonic]
treeko = ["Fire","None",40,45,35,65,55,70,16,"Overgrow", "None", "None","Treeko",leer,pound,leafage,quick_attack,megadrain,detect,quickguard]
wattrel = ["Electric","Flying",40,40,35,55,40,70,16,"Wind Power","Volt absorb","Competitive","Watteral",growl,peck,thundershock,quick_attack,pluck,spark,uproar]
zigzagoon = ["Normal","None",38,30,41,30,41,60,20,"Pickup","Gluttony","Quick Feet","Zigzagoon",tackle,growl,tail_whip,headbutt,baby_doll_eyes,covet,bestow]
geodude = ["Rock","Ground",40,80,100,30,30,20,25,"Rock Head","Sturdy","Sand Veil","Geodude",tackle,defense_curl,mud_slap,rock_polish,rock_throw,rock_tomb,smack_down]
first_route_pokemon = [wattrel,zigzagoon,geodude]
xp_levels = [8, 19, 37, 61, 91, 127, 169, 217, 271, 331, 397, 469, 547, 631, 721]

# starters = [torchic,mudkip,treeko]
# beginner_trainers_and_routes = [wattrel, zigzagoon]
#This information makes a 2D array when combined with Team
xp_values_first = "None"
health_value_first = "None"
movesets_first = ["None","None","None","None"]

need_xp_first = "None"
abililty = "None"
current_stats = ["None","None","None","None","None","None"]
EVs = ["None","None","None","None","None","None"]
IVs = ["None","None","None","None","None","None"]
#0 current xp #1 Healthbar #2 Move 1 #3 Move 2 #4 Move 3 #5 Move 4 #6 XP to next level #7 Ability #8 HP IV #9 attack IV #10 defense IV #11 special attack IV #12 special defense IV #13 speed IV #14 Health EV #15 Attack EV #16 Defense EV #17 Special Attack EV #18 Special Defense EV #19 Speed EV #20 Current Health #21 Current Attack #22 Current Defense #23 Current Special Attack #24 Current Special Defense #25 Current Speed #26 Pokemon Name #27 pokemon level #28 Status #29 Type 1 #30 Type 2 #31 Entire base list
stats_and_movesets_first_player = ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None"]
stats_and_movesets_second_player = ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None"]
stats_and_movesets_third_player = ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None"]
stats_and_movesets_fourth_player = ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None"]
stats_and_movesets_fifth_player = ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None"]
stats_and_movesets_sixth_player = ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None"]

stats_and_movesets_wild_pokemon = ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None"]
#0 pokeballs #1 potions #2 Paralize heal #3 Burn Heal
item_list = [10,5,2,2]

def first_route():
    choice = int(input("You approuch your first route, before you lies three paths: The first path is guarded by a young trainer, the second is a clear path, the third goes through a bushy path. Which will you choose? Enter 1, 2, or 3: "))
def learn_move(new_move,pokemon):
    xyz = True
    while xyz:
        print(f"Which move do you want to replace with {new_move[0]}? If you don't want to learn this move enter 'No'.")
        print(f"{new_move}")
        print(f"{pokemon[2]}")
        print(f"{pokemon[3]}")
        print(f"{pokemon[4]}")
        print(f"{pokemon[5]}")
        choice = input("Enter your choice: ")
        if choice.lower() == pokemon[2][0].lower():
            pokemon[2] = new_move
            xyz = False
        if choice.lower() == pokemon[3][0].lower():
            pokemon[3] = new_move
            xyz = False
        if choice.lower() == pokemon[4][0].lower():
            pokemon[4] = new_move
            xyz = False
        elif choice.lower() == pokemon[5][0].lower():
            pokemon[5] = new_move
            xyz = False
    return pokemon
def oppenent_defeated(deafeated_pokemon, victorious_pokemon):
    xp_x = True
    base_xp = round(deafeated_pokemon[27] * 1.1)
    total_xp = base_xp**3
    victorious_pokemon[0] += total_xp
    while xp_x:
        if victorious_pokemon[0] >= victorious_pokemon[6]:
            victorious_pokemon[27] += 1
            victorious_pokemon[0] = victorious_pokemon[0] - victorious_pokemon[6]
            new_current_level = xp_levels.index(victorious_pokemon[6])
            victorious_pokemon[6] = xp_levels[new_current_level+1]
            if victorious_pokemon[6] == 37:
                victorious_pokemon = learn_move(victorious_pokemon[31][15],victorious_pokemon)
        else:
            xp_x = False
def grass(value, oppenent):
    if oppenent[29] == "Fire" or oppenent[30] == "Fire":
        value = value/2
    if oppenent[29] == "Grass" or oppenent[30] == "Grass":
        value = value/2
    if oppenent[29] == "Poison" or oppenent[30] == "Poison":
        value = value/2
    if oppenent[29] == "Flying" or oppenent[30] == "Flying":
        value = value/2
    if oppenent[29] == "Bug" or oppenent[30] == "Bug":
        value = value/2
    if oppenent[29] == "Dragon" or oppenent[30] == "Dragon":
        value = value/2
    if oppenent[29] == "Steel" or oppenent[30] == "Steel":
        value = value/2
    if oppenent[29] == "Water" or oppenent[30] == "Water":
        value = value*2
    if oppenent[29] == "Ground" or oppenent[30] == "Ground":
        value = value*2
    if oppenent[29] == "Rock" or oppenent[30] == "Rock":
        value = value*2
    return value

def fire(value, oppenent):
    if oppenent[29] == "Fire" or oppenent[30] == "Fire":
        value = value/2
    if oppenent[29] == "Water" or oppenent[30] == "Water":
        value = value/2
    if oppenent[29] == "Rock" or oppenent[30] == "Rock":
        value = value/2
    if oppenent[29] == "Dragon" or oppenent[30] == "Dragon":
        value = value/2
    if oppenent[29] == "Grass" or oppenent[30] == "Grass":
        value = value*2
    if oppenent[29] == "Ice" or oppenent[30] == "Ice":
        value = value*2
    if oppenent[29] == "Bug" or oppenent[30] == "Bug":
        value = value*2
    if oppenent[29] == "Steel" or oppenent[30] == "Steel":
        value = value*2
    return value

def water(value, oppenent):
    if oppenent[29] == "Grass" or oppenent[30] == "Grass":
        value = value/2
    if oppenent[30] == "Water" or oppenent[29] == "Water":
        value = value/2
    if oppenent[30] == "Grass" or oppenent[29] == "Grass":
        value = value/2
    if oppenent[30] == "Dragon" or oppenent[29] == "Dragon":
        value = value/2
    if oppenent[30] == "Ground" or oppenent[29] == "Ground":
        value = value*2
    if oppenent[30] == "Rock" or oppenent[29] == "Rock":
        value = value*2
    if oppenent[30] == "Fire" or oppenent[29] == "Fire":
        value = value*2
    return value

def flying(value, oppenent):
    if oppenent[29] == "Fighting" or oppenent[30] == "Fighting":
        value = value*2
    if oppenent[29] == "Bug" or oppenent[30] == "Bug":
        value = value*2
    if oppenent[29] == "Grass" or oppenent[30] == "Grass":
        value = value*2
    if oppenent[29] == "Rock" or oppenent[30] == "Rock":
        value = value/2
    if oppenent[29] == "Steel" or oppenent[30] == "Steel":
        value = value/2
    if oppenent[29] == "Electric" or oppenent[30] == "Electric":
        value = value/2
    return value

def fighting(value, oppenent):
    if oppenent[29] == "Normal" or oppenent[30] == "Normal":
        value = value*2
    if oppenent[29] == "Ice" or oppenent[30] == "Ice":
        value = value*2
    if oppenent[29] == "Rock" or oppenent[30] == "Rock":
        value = value*2
    if oppenent[29] == "Dark" or oppenent[30] == "Dark":
        value = value*2
    if oppenent[29] == "Steel" or oppenent[30] == "Steel":
        value = value*2
    if oppenent[29] == "Poison" or oppenent[30] == "Poison":
        value = value/2
    if oppenent[29] == "Flying" or oppenent[30] == "Flying":
        value = value/2
    if oppenent[29] == "Psychic" or oppenent[30] == "Psychic":
        value = value/2
    if oppenent[29] == "Bug" or oppenent[30] == "Bug":
        value = value/2
    if oppenent[29] == "Fairy" or oppenent[30] == "Fairy":
        value = value/2
    return value

def fairy(value, oppenent):
    if oppenent[29] == "Fighting" or oppenent[30] == "Fighting":
        value = value*2
    if oppenent[29] == "Dragon" or oppenent[30] == "Dragon":
        value = value*2
    if oppenent[29] == "Dark" or oppenent[30] == "Dark":
        value = value*2
    if oppenent[29] == "Poison" or oppenent[30] == "Poison":
        value = value/2
    if oppenent[29] == "Steel" or oppenent[30] == "Steel":
        value = value/2
    if oppenent[29] == "Fire" or oppenent[30] == "Fire":
        value = value/2
    return value

def electric(value, oppenent):
    if oppenent[29] == "Water" or oppenent[30] == "Water":
        value = value*2
    if oppenent[29] == "Flying" or oppenent[30] == "Flying":
        value = value*2
    if oppenent[29] == "Electric" or oppenent[30] == "Electric":
        value = value/2
    if oppenent[29] == "Ground" or oppenent[30] == "Ground":
        value = 0
    return value

def steel(value, oppenent):
    if oppenent[29] == "Ice" or oppenent[30] == "Ice":
        value = value*2
    if oppenent[29] == "Rock" or oppenent[30] == "Rock":
        value = value*2
    if oppenent[29] == "Fairy" or oppenent[30] == "Fairy":
        value = value*2
    if oppenent[29] == "Steel" or oppenent[30] == "Steel":
        value = value/2
    if oppenent[29] == "Fire" or oppenent[30] == "Fire":
        value = value/2
    if oppenent[29] == "Water" or oppenent[30] == "Water":
        value = value/2
    if oppenent[29] == "Electric" or oppenent[30] == "Electric":
        value = value/2
    return value

def dragon(value, oppenent):
    if oppenent[29] == "Dragon" or oppenent[30] == "Dragon":
        value = value*2
    if oppenent[29] == "Steel" or oppenent[30] == "Steel":
        value = value/2
    if oppenent[29] == "Fairy" or oppenent[30] == "Fairy":
        value = 0
    return value

def rock(value, oppenent):
    if oppenent[29] == "Flying" or oppenent[30] == "Flying":
        value = value*2
    if oppenent[29] == "Bug" or oppenent[30] == "Bug":
        value = value*2
    if oppenent[29] == "Fire" or oppenent[30] == "Fire":
        value = value*2
    if oppenent[29] == "Ice" or oppenent[30] == "Ice":
        value = value*2
    if oppenent[29] == "Fighting" or oppenent[30] == "Fighting":
        value = value/2
    if oppenent[29] == "Ground" or oppenent[30] == "Ground":
        value = value/2
    if oppenent[29] == "Steel" or oppenent[30] == "Steel":
        value = value/2
    return value

def ground(value, oppenent):
    if oppenent[29] == "Poison" or oppenent[30] == "Poison":
        value = value*2
    if oppenent[29] == "Rock" or oppenent[30] == "Rock":
        value = value*2
    if oppenent[29] == "Steel" or oppenent[30] == "Steel":
        value = value*2
    if oppenent[29] == "Fire" or oppenent[30] == "Fire":
        value = value*2
    if oppenent[29] == "Electric" or oppenent[30] == "Electric":
        value = value*2
    if oppenent[29] == "Grass" or oppenent[30] == "Grass":
        value = value/2
    if oppenent[29] == "Ice" or oppenent[30] == "Ice":
        value = value/2
    if oppenent[29] == "Flying" or oppenent[30] == "Flying":
        value = 0
    return value

def dark(value, oppenent):
    if oppenent[29] == "Ghost" or oppenent[30] == "Ghost":
        value = value*2
    if oppenent[29] == "Psychic" or oppenent[30] == "Psychic":
        value = value*2
    if oppenent[29] == "Fighting" or oppenent[30] == "Fighting":
        value = value/2
    if oppenent[29] == "Dark" or oppenent[30] == "Dark":
        value = value/2
    if oppenent[29] == "Fairy" or oppenent[30] == "Fairy":
        value = value/2
    return value

def psychic(value, oppenent):
    if oppenent[29] == "Fighting" or oppenent[30] == "Fighting":
        value = value*2
    if oppenent[29] == "Poison" or oppenent[30] == "Poison":
        value = value*2
    if oppenent[29] == "Steel" or oppenent[30] == "Steel":
        value = value/2
    if oppenent[29] == "Psychic" or oppenent[30] == "Psychic":
        value = value/2
    if oppenent[29] == "Dark" or oppenent[30] == "Dark":
        value = 0
    return value

def bug(value, oppenent):
    if oppenent[29] == "Grass" or oppenent[30] == "Grass":
        value = value*2
    if oppenent[29] == "Psychic" or oppenent[30] == "Psychic":
        value = value*2
    if oppenent[29] == "Dark" or oppenent[30] == "Dark":
        value = value*2
    if oppenent[29] == "Fighting" or oppenent[30] == "Fighting":
        value = value/2
    if oppenent[29] == "Flying" or oppenent[30] == "Flying":
        value = value/2
    if oppenent[29] == "Poison" or oppenent[30] == "Poison":
        value = value/2
    if oppenent[29] == "Ghost" or oppenent[30] == "Ghost":
        value = value/2
    if oppenent[29] == "Steel" or oppenent[30] == "Steel":
        value = value/2
    if oppenent[29] == "Fire" or oppenent[30] == "Fire":
        value = value/2
    if oppenent[29] == "Fairy" or oppenent[30] == "Fairy":
        value = value/2
    return value

def ice(value, oppenent):
    if oppenent[29] == "Flying" or oppenent[30] == "Flying":
        value = value*2
    if oppenent[29] == "Ground" or oppenent[30] == "Ground":
        value = value*2
    if oppenent[29] == "Grass" or oppenent[30] == "Grass":
        value = value*2
    if oppenent[29] == "Dragon" or oppenent[30] == "Dragon":
        value = value*2
    if oppenent[29] == "Steel" or oppenent[30] == "Steel":
        value = value/2
    if oppenent[29] == "Fire" or oppenent[30] == "Fire":
        value = value/2
    if oppenent[29] == "Water" or oppenent[30] == "Water":
        value = value/2
    if oppenent[29] == "Ice" or oppenent[30] == "Ice":
        value = value/2
    return value

def normal(value, oppenent):
    if oppenent[29] == "Rock" or oppenent[30] == "Rock":
        value = value/2
    if oppenent[29] == "Steel" or oppenent[30] == "Steel":
        value = value/2
    if oppenent[29] == "Ghost" or oppenent[30] == "Ghost":
        value = 0
    return value

def poison(value, oppenent):
    if oppenent[29] == "Grass" or oppenent[30] == "Grass":
        value = value*2
    if oppenent[29] == "Fairy" or oppenent[30] == "Fairy":
        value = value*2
    if oppenent[29] == "Poison" or oppenent[30] == "Poison":
        value = value/2
    if oppenent[29] == "Ground" or oppenent[30] == "Ground":
        value = value/2
    if oppenent[29] == "Rock" or oppenent[30] == "Rock":
        value = value/2
    if oppenent[29] == "Ghost" or oppenent[30] == "Ghost":
        value = value/2
    return value

def ghost(value, oppenent):
    if oppenent[29] == "Ghost" or oppenent[30] == "Ghost":
        value = value*2
    if oppenent[29] == "Psychic" or oppenent[30] == "Psychic":
        value = value*2
    if oppenent[29] == "Dark" or oppenent[30] == "Dark":
        value = value/2
    if oppenent[29] == "Normal" or oppenent[30] == "Normal":
        value = 0
    return value



#Status changers
def parachance(chance,affect_pokemon):
    decision = random.randint(0,100)
    if affect_pokemon[28] != "None":
        if decision <= chance:
            affect_pokemon[28] = "paralysis"
def paralysis():
    decision = random.randint(1,4)
    if decision == 4:
        return True
    else:
        return False


def move_finder(pokemon_type,oppenent):
    value = 1
    if pokemon_type == "Fire":
        value = fire(value,oppenent)
    elif pokemon_type == "Water":
        value = water(value,oppenent)
    elif pokemon_type == "Grass":
        value = grass(value,oppenent)
    elif pokemon_type == "Flying":
        value = flying(value,oppenent)
    elif pokemon_type == "Figthing":
        value = fighting(value,oppenent)
    elif pokemon_type == "Fairy":
        value = fairy(value,oppenent)
    elif pokemon_type == "Electric":
        value = electric(value,oppenent)
    elif pokemon_type == "Steel":
        value = steel(value,oppenent)
    elif pokemon_type == "Dragon":
        value = dragon(value,oppenent)
    elif pokemon_type == "Rock":
        value = rock(value,oppenent)
    elif pokemon_type == "Ground":
        value = ground(value,oppenent)
    elif pokemon_type == "Dark":
        value = dark(value,oppenent)
    elif pokemon_type == "Psychic":
        value = psychic(value,oppenent)
    elif pokemon_type == "Bug":
        value = bug(value,oppenent)
    elif pokemon_type == "Ice":
        value = ice(value,oppenent)
    elif pokemon_type == "Normal":
        value = normal(value,oppenent)
    elif pokemon_type == "Poison":
        value = poison(value,oppenent)
    elif pokemon_type == "Ghost":
        value = ghost(value,oppenent)
    else:
        print("What? How?")
    return value

def damage_calculater(attacking_pokemon, move, defending_pokemon):
    effectiviness = 0
    if move[2] == attacking_pokemon[29] or move[2] == attacking_pokemon[30]:
        stab = True
    else:
        stab = False
    critchance = random.randint(1,20)
    crit = False
    if critchance == 20:
        crit = True
    if move[3] == "Physical":
        defense = defending_pokemon[22]
    elif move[3] == "Special":
        defense = defending_pokemon[24]
    if move[3] == "Physical":
        attack_stat = attacking_pokemon[21]
    elif move[3] == "Special":
        attack_stat = attacking_pokemon[23]
    randomval = random.randint(85,100)/100
    value = move_finder(move[2],defending_pokemon)
    if value > 1:
        effectiviness = 1
    if value < 1:
        effectiviness = -1
        print("Its not very effective!")
    damage = (((((attacking_pokemon[27]*2)/5)+2)*move[1]*(attack_stat/defense)/50)+2)*randomval*value
    if stab == True:
        damage = damage*1.5
    if crit == True:
        damage = damage*1.5
    damage = round(damage,0)
    return damage, crit, effectiviness, move[0]
def oppennet_AI(friendly_pokemon,enemy_pokemon):

    if friendly_pokemon[4] =="None":
        friendly_pokemon[4] == -1
    if friendly_pokemon[5] =="None":
        friendly_pokemon[5] == -1
    if friendly_pokemon[2] != "None":
        if friendly_pokemon[2][3] != "Status":
            value_1 = move_finder(friendly_pokemon[2][2],enemy_pokemon)
        else:
           value_1 = 0
    else:
        value_1 = 0
    if friendly_pokemon[3] != "None":
        if friendly_pokemon[3][3] != "Status":
            value_2 = move_finder(friendly_pokemon[3][2],enemy_pokemon)
        else:
           value_2 = 0
    else:
        value_2 = 0
    if friendly_pokemon[4] != "None":
        if friendly_pokemon[4][3] != "Status":
            value_3 = move_finder(friendly_pokemon[4][2],enemy_pokemon)
        else:
           value_3 = 0
    else:
        value_3 = 0
    if friendly_pokemon[5] != "None":
        if friendly_pokemon[5][3] != "Status":
            value_4 = move_finder(friendly_pokemon[5][2],enemy_pokemon)
        else:
           value_4 = 0
    else:
        value_4 = 0
    if value_1 > 1 and value_1 != value_2 and value_1 != value_3 and value_1 != value_4:
        return friendly_pokemon[2]
    if value_2 > 1 and value_2 != value_3 and value_2 != value_4:
        return friendly_pokemon[3]
    if value_3 > 1 and value_3 != value_4:
        return friendly_pokemon[4]
    if value_4 > 1:
        return friendly_pokemon[5]
    if value_1 > 1 and value_1 == value_2:
        if friendly_pokemon[2][1] > friendly_pokemon[3][1]:
            return friendly_pokemon[2]
        else:
            return friendly_pokemon[3]
    if value_1 > 1 and value_1 == value_3:
        if friendly_pokemon[2][1] > friendly_pokemon[4][1]:
            return friendly_pokemon[2]
        else:
            return friendly_pokemon[4]
    if value_1 > 1 and value_1 == value_2:
        if friendly_pokemon[2][1] > friendly_pokemon[5][1]:
            return friendly_pokemon[2]
        else:
            return friendly_pokemon[5]
    if value_2 > 1 and value_2 == value_3:
        if friendly_pokemon[3][1] > friendly_pokemon[4][1]:
            return friendly_pokemon[2]
        else:
            return friendly_pokemon[4]
    if value_2 > 1 and value_2 == value_4:
        if friendly_pokemon[3][1] > friendly_pokemon[5][1]:
            return friendly_pokemon[3]
        else:
            return friendly_pokemon[5]
    if value_3 > 1 and value_3 == value_4:
        if friendly_pokemon[4][1] > friendly_pokemon[5][1]:
            return friendly_pokemon[4]
        else:
            return friendly_pokemon[5]
    #Neutral effective moves# GET WORKING COME BACK AND FINISH
    if value_1 == 1 and value_2 < 1 and value_3 < 1 and value_4 < 1:
        return friendly_pokemon[2]
    if value_2 == 2 and value_1 < 1 and value_3 < 1 and value_4 < 1:
        return friendly_pokemon[3]
    if value_3 == 2 and value_1 < 1 and value_2 < 1 and value_4 < 1:
        return friendly_pokemon[4]
    if value_4 == 2 and value_1 < 1 and value_3 < 1 and value_2 < 1:
        return friendly_pokemon[5]
    if value_1 == 1 and value_2 == 1 and value_3 == 1 and value_4 == 1:
        if friendly_pokemon[2][1] >= friendly_pokemon[3][1] and friendly_pokemon[2][1] >= friendly_pokemon[4][1] and friendly_pokemon[2][1] >= friendly_pokemon[5][1]:
            return friendly_pokemon[2]
        if friendly_pokemon[3][1] >= friendly_pokemon[2][1] and friendly_pokemon[3][1] >= friendly_pokemon[4][1] and friendly_pokemon[3][1] >= friendly_pokemon[5][1]:
            return friendly_pokemon[3]
        if friendly_pokemon[4][1] >= friendly_pokemon[2][1] and friendly_pokemon[4][1] >= friendly_pokemon[3][1] and friendly_pokemon[4][1] >= friendly_pokemon[5][1]:
            return friendly_pokemon[4]
        if friendly_pokemon[5][1] >= friendly_pokemon[2][1] and friendly_pokemon[5][1] >= friendly_pokemon[3][1] and friendly_pokemon[5][1] >= friendly_pokemon[4][1]:
            return friendly_pokemon[5]
    if value_1 == 1 and value_2 == 1:
        if friendly_pokemon[2][1] >= friendly_pokemon[3][1]:
            return friendly_pokemon[2]
        else:
            return friendly_pokemon[3]
    if value_1 == 1:
        return friendly_pokemon[2]
    if value_2 == 1:
        return friendly_pokemon[3]
    if value_3 == 1:
        return friendly_pokemon[4]
    if value_4 == 1:
        return friendly_pokemon[5]
def choose_pokemon(): 
    check = False
    while check == False:
        starter = input("Chose your starter: Mudkip, the water type, Treeko, the grass type, or torchic the fire type: ")
        if starter.lower() == "treeko":
            return treeko
        if starter.lower() == "mudkip":
            return mudkip
        if starter.lower() == "torchic":
            return torchic
        print("Invalid, please try again")
def health_calculator(who, level,pokemon):

    who[20] = round((2*pokemon[3] + who[8] + level / 4 * level)/100 + 10,0)
def stat_generator(who, level, pokemon):

    who[21] = round((2*pokemon[4] + who[9] + who[15] / 4 * level)/100 + 5,0)

    who[22] = round((2*pokemon[5] + who[10] + who[16] / 4 * level)/100 + 5,0)

    who[23] = round((2*pokemon[6] + who[11] + who[17] / 4 * level)/100 + 5,0)

    who[24] = round((2*pokemon[7] + who[12] + who[18] / 4 * level)/100 + 5,0)

    who[25] = round((2*pokemon[8] + who[13] + who[19] / 4 * level)/100 + 5,0)


def iv_generator(who):

    who[8] = random.randint(0,32)

    who[9] = random.randint(0,32)

    who[10] = random.randint(0,32)

    who[11] = random.randint(0,32)

    who[12] = random.randint(0,32)

    who[13] = random.randint(0,32)
def replace_pokemon(old,new):
    old[0] = new[0]
    old[1] = new[1]
    old[2] = new[2]
    old[3] = new[3]
    old[4] = new[4]
    old[5] = new[5]
    old[6] = new[6]
    old[7] = new[7]
    old[8] = new[8]
    old[9] = new[9]
    old[10] = new[10]
    old[11] = new[11]
    old[12] = new[12]
    old[13] = new[13]
    old[14] = new[14]
    old[15] = new[15]
    old[16] = new[16]
    old[17] = new[17]
    old[18] = new[18]
    old[19] = new[19]
    old[20] = new[20]
    old[21] = new[21]
    old[22] = new[22]
    old[23] = new[23]
    old[24] = new[24]
    old[25] = new[25]
    old[26] = new[26]
def ability_generator(who,pokemon):
    x = True
    while x:
        h = random.randint(1,10)
        if h == 4:
            who[7] = pokemon[11]
            x = False
        else:
            h = random.randint(1,2)
            if h == 1:
                x = False
                who[7] = pokemon[9]
            else:
                who[7] = pokemon[10]
                x = False
        if who[7] == "None":
                pass
#Must be wild or trainer pokemon
#2-5 moves
def move_generator(who, pokemon):
    x = True
    if who[27] < 3:
        who[2] = pokemon[13]
        who[3] = pokemon[14]
    elif who[27] < 6:
        who[2] = pokemon[13]
        who[3] = pokemon[14]
        who[4] = pokemon[15]
    elif who[27] < 9:
        who[2] = pokemon[13]
        who[3] = pokemon[14]
        who[4] = pokemon[15]
        who[5] = pokemon[16]
    elif who[27] < 12:
        while x == True:
            who[2] = pokemon[random.randint(13,17)]
            who[3] = pokemon[random.randint(13,17)]
            who[4] = pokemon[random.randint(13,17)]
            who[5] = pokemon[random.randint(13,17)]
            if who[2] == who[3] or who[2] == who[4] or who[2] == who[5] or who[3] == who[4] or who[3] == who[5] or who[4] == who[5]:
                x = True
            else: 
                x = False
    else:
        who[2] = pokemon[random.randint(13,18)]
        who[3] = pokemon[random.randint(13,18)]
        who[4] = pokemon[random.randint(13,18)]
        who[5] = pokemon[random.randint(13,18)]
        if who[2] == who[3] or who[2] == who[4] or who[2] == who[5] or who[3] == who[4] or who[3] == who[5] or who[4] == who[5]:
            x = True
        else:
            x = False
def level_generator(route):
    x = 1
    if route == 1:
        x = random.randint(1,4)
    elif route == 2:
        x = random.randint(4,8)
    elif route == 3:
        x = random.randint(8,12)
    return x
# Wild pokemon, newly given pokemon, trainers, or gym trainers, GYM LEADER EXCEPTED
def give_stats(who, pokemon):
    who[31] = pokemon
    who[27] = level_generator(route)
    who[0] = 0
    move_generator(who,pokemon)
    who[6] = xp_levels[1+who[27]]
    ability_generator(who, pokemon)
    iv_generator(who) 
    # 8-13 IVs
    # 14-19 EVs (start at zero)
    who[14] = 0
    who[15] = 0
    who[16] = 0
    who[17] = 0
    who[18] = 0
    who[19] = 0
    who[26] = pokemon[12]
    who[29] = pokemon[0]
    who[30] = pokemon[1]
    health_calculator(who,who[27],pokemon)
    # Real Health
    stat_generator(who,who[27],pokemon)
    who[1] = who[20]
    # Health calculated last
def display_info(player_current,oppenent_current):
    print(f"{str(player_current[26])} is at {str(player_current[1])} HP! {str(oppenent_current[26])} is at {str(oppenent_current[1])} HP!")
    while True:
        answer = input("Will you Battle, Swap Pokemon, Use Item, or Run: ")
        if answer.lower() == "battle":
            return "battle"
        if answer.lower() == "swap pokemon":
            return "swap pokemon"
        if answer.lower() == "use item":
            return "use item"
        if answer.lower() == "run":
             return "run"
        else:
            print("Invalid, try again.")
def display_moves(pokemon):
    yxz = True
    while yxz:
        print(f"Your moves are:")
        if pokemon[2] != "None":
            print(pokemon[2])
        if pokemon[3] != "None":
            print(pokemon[3])
        if pokemon[4] != "None":
            print(pokemon[4])
        if pokemon[5] != "None":
            print(pokemon[5])
        move_selection = int(input("Select 1, 2, 3, 4 to select a move or if you want to go back to the selection screen enter 'Back'!"))
        if move_selection == 1 or move_selection == 2 or move_selection == 3 or move_selection == 4:
            return move_selection
def swap_team(team_current):
    swap_x = True
    pokemon_list_counter = 0
    swap_choice = None
    options = ["None","None","None","None","None"]
    print(f"Your choices are: ")
    if team[0] != team_current and team[0][26] != "None" and team[0][1] != 0:
                    print(f"{team[0][26]}: {int(team[0][1])}HP")
                    options[pokemon_list_counter] = team[0]
                    pokemon_list_counter += 1
    if team[1] != team_current and team[1][26] != "None" and team[1][1] != 0:
                    print(f"{team[1][26]}: {int(team[1][1])}HP")
                    options[pokemon_list_counter]= team[1]
                    pokemon_list_counter += 1
    if team[2] != team_current and team[2][26] != "None" and team[2][1] != 0:
                    print(f"{team[2][26]}: {int(team[2][1])}HP")
                    options[pokemon_list_counter] = team[2]
                    pokemon_list_counter += 1
    if team[3] != team_current and team[3][26] != "None" and team[3][1] != 0:
                    print(f"{team[3][26]}: {int(team[3][1])}HP")
                    options[pokemon_list_counter] = team[3]
                    pokemon_list_counter += 1
    if team[4] != team_current and team[4][26] != "None" and team[4][1] != 0:
                    print(f"{team[4][26]}: {int(team[4][1])}HP")
                    options[pokemon_list_counter] = team[4]
                    pokemon_list_counter += 1
    if team[5] != team_current and team[5][26] != "None" and team[5][1] != 0:
                    print(f"{team[5][26]}: {int(team[5][1])}HP")
                    options[pokemon_list_counter] = team[5]
                    pokemon_list_counter += 1
    while swap_x:
        swap_choice = input(f"Enter one of the following to swap to it or back to go back: ")
        if options[0] != "None":
            if swap_choice.lower() == options[0][26].lower():
                team_current = options[0]
                print(team_current[26])
                break
        if options[1] != "None":
            if swap_choice.lower() == options[1][26].lower():
                team_current = options[1]
                swap_x = False
        if options[2] != "None":
            if swap_choice.lower() == options[2][26].lower():
                team_current = options[2]
                swap_x = False
        if options[3] != "None":
            if swap_choice.lower() == options[3][26].lower():
                team_current = options[3]
                swap_x = False
        if options[4] != "None":
            if swap_choice.lower() == options[4][26].lower():
                team_current = options[4]
                swap_x = False
        if swap_choice.lower() == "back":
            swap_x = False
        if swap_choice == True:
            print("Invalid")
    return team_current
def faint_swap(team_current):
    swap_x = True
    pokemon_list_counter = 0
    swap_choice = None
    run_choice = False
    options = ["None","None","None","None","None"]
    print(f"{team_current[26]} Fainted!")
    print(f"Your choices are: ")
    if team[0] != team_current and team[0][26] != "None" and team[0][1] != 0:
                    print(f"{team[0][26]}: {int(team[0][1])}HP")
                    options[pokemon_list_counter] = team[0]
                    pokemon_list_counter += 1
    if team[1] != team_current and team[1][26] != "None" and team[1][1] != 0:
                    print(f"{team[1][26]}: {int(team[1][1])}HP")
                    options[pokemon_list_counter]= team[1]
                    pokemon_list_counter += 1
    if team[2] != team_current and team[2][26] != "None" and team[2][1] != 0:
                    print(f"{team[2][26]}: {int(team[2][1])}HP")
                    options[pokemon_list_counter] = team[2]
                    pokemon_list_counter += 1
    if team[3] != team_current and team[3][26] != "None" and team[3][1] != 0:
                    print(f"{team[3][26]}: {int(team[3][1])}HP")
                    options[pokemon_list_counter] = team[3]
                    pokemon_list_counter += 1
    if team[4] != team_current and team[4][26] != "None" and team[4][1] != 0:
                    print(f"{team[4][26]}: {int(team[4][1])}HP")
                    options[pokemon_list_counter] = team[4]
                    pokemon_list_counter += 1
    if team[5] != team_current and team[5][26] != "None" and team[5][1] != 0:
                    print(f"{team[5][26]}: {int(team[5][1])}HP")
                    options[pokemon_list_counter] = team[5]
                    pokemon_list_counter += 1
    if options[0] != "None":
        pass
    else:
        print("You Fainted!")
    while swap_x:
        swap_choice = input(f"Enter one of the following to swap to or run to run: ")
        if options[0] != "None":
            if swap_choice.lower() == options[0][26].lower():
                team_current = options[0]
                break
        if options[1] != "None":
            if swap_choice.lower() == options[1][26].lower():
                team_current = options[1]
                swap_x = False
        if options[2] != "None":
            if swap_choice.lower() == options[2][26].lower():
                team_current = options[2]
                swap_x = False
        if options[3] != "None":
            if swap_choice.lower() == options[3][26].lower():
                team_current = options[3]
                swap_x = False
        if options[4] != "None":
            if swap_choice.lower() == options[4][26].lower():
                team_current = options[4]
                swap_x = False
        if swap_choice == True:
            print("Invalid")
        if swap_choice == str:
            if swap_choice.lower() == "run":
                run_chance()
                if run_chance == True:
                    print("You got away!")
                    return team_current, True
    return team_current, False
def run_chance():
    run_chance = random.randint(1,100)
    if run_chance >= 50:
        return True
    else:
        return False
def new_wild(route):
    if route == 1:
        give_stats(stats_and_movesets_wild_pokemon,random.choice(first_route_pokemon))
        return stats_and_movesets_wild_pokemon
def battle_wild(team,enemy):
    run = False
    turnused = False
    x = True
    y = True
    team_current = team[0]
    move_select = None
    print("A wild", enemy[26], "appeared!")
    while x:
        while y:
            move_select = None
            oppenent_move = oppennet_AI(enemy,team_current)
            choice = display_info(team_current,enemy)
            if choice == "battle":
                move_select =  display_moves(team_current)
                turnused = True
            elif choice ==  "swap pokemon":
                team_current = swap_team(team_current)
                turnused = True
            elif choice == "use item":
                pass
            #Damage counters:
            if turnused == True:
                oppenent_damage, enemy_crit, enemy_effectiviness, move_name_oppenenent = damage_calculater(enemy,oppenent_move,team_current)
                if move_select == 1 or move_select == 2 or move_select == 3 or move_select == 4:
                    if move_select == 1:
                        player_damage, player_crit, player_effectiviness, move_name = damage_calculater(team_current,team_current[2],enemy)
                    elif move_select == 2:
                        player_damage, player_crit, player_effectiviness, move_name = damage_calculater(team_current,team_current[3],enemy)
                    elif move_select == 3:
                        player_damage, player_crit, player_effectiviness, move_name = damage_calculater(team_current,team_current[4],enemy)
                    elif move_select == 4:
                        player_damage, player_crit, player_effectiviness, move_name = damage_calculater(team_current,team_current[5],enemy)
                    if team_current[25] >= enemy[25]:
                        enemy[1] -= player_damage
                        print(f"{team_current[26]} used {move_name}")
                        if player_crit == True:
                            print("It is a critical hit!")
                        if player_effectiviness > 0:
                            print("Its super effective!")
                        elif player_effectiviness < 0:
                            print("Its not very effective!")
                        else:
                            pass
                        if enemy[1] <= 0:
                            x = False
                            y = False
                            print(enemy[26] + " Fainted!")
                            oppenent_defeated(enemy,team_current)
                        else:
                            team_current[1] -= oppenent_damage
                            print(f"{enemy[26]} used {move_name_oppenenent}")
                            if enemy_crit == True:
                                    print("It is a critical hit!")
                            if enemy_effectiviness > 0:
                                    print("Its super effective!")
                            elif enemy_effectiviness < 0:
                                    print("Its not very effective!")
                            else:
                                    pass
                        if team_current[1] <= 0:
                            team_current, run = faint_swap(team_current)
                            if run == True:
                                return "Battle Finished"
                    else:
                            team_current[1] -= oppenent_damage
                            print(f"{enemy[26]} used {move_name_oppenenent}")
                            if enemy_crit == True:
                                print("It is a critical hit!")
                            if enemy_effectiviness > 0:
                                print("Its super effective!")
                            elif enemy_effectiviness < 0:
                                print("Its not very effective!")
                            else:
                                pass
                            if team_current[1] <= 0:
                                team_current, run = faint_swap(team_current)
                                if run == True:
                                    return "Battle Finished"
                            else:
                                enemy[1] -= player_damage
                                print(f"{team_current[26]} used {move_name}")
                                if player_crit == True:
                                    print("It is a critical hit!")
                                if player_effectiviness > 0:
                                    print("Its super effective!")
                                elif player_effectiviness < 0:
                                    print("Its not very effective!")
                                else:
                                    pass
                                if enemy[1] <= 0:
                                    print(enemy[26] + " Fainted!")
                                    oppenent_defeated(enemy,team_current)
            turnused = False
                

#Starts the game
team = [stats_and_movesets_first_player,stats_and_movesets_second_player,stats_and_movesets_third_player,stats_and_movesets_fourth_player,stats_and_movesets_fifth_player,stats_and_movesets_sixth_player]
selected = choose_pokemon()
route = 1
give_stats(stats_and_movesets_first_player,selected)
give_stats(stats_and_movesets_second_player,mudkip)
give_stats(stats_and_movesets_third_player,treeko)
give_stats(stats_and_movesets_fourth_player,wattrel)
battle_wild(team,new_wild(route))
# print(battle_wild(team,new_wild(route)))
# first_route()

