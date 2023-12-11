#Imports random function
import random
#creates the moves
# #1 name #2 power #3 type #4 catigory #5 accuarcy #6Priority #7 Status
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
dragon_pulse = ["Dragon Pulse", 85, "Dragon", "Special", 100, None]
dark_pulse = ["Dark Pulse", 80, "Dark", "Special", 100, None]
shadow_ball = ["Shadow Ball", 80, "Ghost", "Special", 100]
power_gem = ["Power Gem", 80, "Rock", "Special", 100]
zen_headbutt = ["Zen Headbutt", 80, "Psychic", "Physical", 90]
foul_play = ["Foul Play", 95, "Dark", "Physical", 100]
ice_beam = ["Ice Beam", 90, "Ice", "Special", 100]
discharge = ["Discharge", 80, "Electric", "Special", 100]
psychic_move = ["Psychic", 90, "Psychic", "Special", 100]

#Creates the base sets for all pokemon, raid pokemon only have 4 moves
#0 Type 1 #1 Type 2# Base HP #3 Base Attack #4 Base Defense #5 Base Special Attack #6 Base Special Defense #7 Base Speed #8 evolution level #9 Ability 1 #10 Ability 2 #11 Hidden Ability #12 Pokemon Name #13 Move Learned at level 1 #14 Move learned at level 1 #15 Move Learned at level 3 #16 Move Learned at level 6 #17 Move Learned at Level 9 #18 Move Level 12 #19 Move learned at Level 15
torchic = ["Fire","None",45,60,40,70,50,45,16,"Blaze","None","Speed Boost","Torchic",fire_punch,scratch,ember,quick_attack,flame_charge,detect,sandattack]
mudkip = ["Water","None",50,70,50,50,50,40,16,"Torrent", "None", "Damp","Mudkip",rock_smash, tackle, water_gun, rock_smash, rock_throw, protect, supersonic]
treeko = ["Grass","None",40,45,35,65,55,70,16,"Overgrow", "None", "None","Treeko",tackle,pound,leafage,quick_attack,megadrain,detect,quickguard]
wattrel = ["Electric","Flying",40,40,35,55,40,70,16,"Wind Power","Volt absorb","Competitive","Wattrel",body_slam,peck,thundershock,quick_attack,pluck,spark,uproar]
zigzagoon = ["Normal","None",38,30,41,30,41,60,20,"Pickup","Gluttony","Quick Feet","Zigzagoon",tackle,rock_throw,pound,headbutt,baby_doll_eyes,covet,bestow]
geodude = ["Rock","Ground",40,80,100,30,30,20,25,"Rock Head","Sturdy","Sand Veil","Geodude",tackle,scratch,mud_slap,rock_polish,rock_throw,rock_tomb,smack_down]
hydreigon = ["Dark","Dragon",92,105,90,125,90,1,None,"Levitate","None","None","Hydreigon",dark_pulse,dragon_pulse,headbutt,hyper_voice]
sableye = ["Dark", "Ghost", 50, 75, 75, 65, 65, 1, None, "Keen Eye", "Stall", "Prankster", "Sableye",shadow_ball,power_gem,zen_headbutt,foul_play]
porygon_z = ["Normal", "None", 85, 80, 70, 135, 75, 1, None, "Adaptability", "Download", "Analytic", "Porygon-Z",psychic_move,discharge,ice_beam,shadow_ball]

#Gives the list of pokemon that can be encountered on the first route
first_route_pokemon = [wattrel,zigzagoon,geodude]
#Gives the list of pokemon that can be encountered in raids
raid_pokemon = [hydreigon,sableye,porygon_z]
#Gives the amount of xp required for level up
xp_levels = [8, 19, 37, 61, 91, 127, 169, 217, 271, 331, 397, 469, 547, 631, 721]

#creates the arrays that hold player information
#0 current xp #1 Healthbar #2 Move 1 #3 Move 2 #4 Move 3 #5 Move 4 #6 XP to next level #7 Ability #8 HP IV #9 attack IV #10 defense IV #11 special attack IV #12 special defense IV #13 speed IV #14 Health EV #15 Attack EV #16 Defense EV #17 Special Attack EV #18 Special Defense EV #19 Speed EV #20 Current Health #21 Current Attack #22 Current Defense #23 Current Special Attack #24 Current Special Defense #25 Current Speed #26 Pokemon Name #27 pokemon level #28 Status #29 Type 1 #30 Type 2 #31 Entire base list
stats_and_movesets_first_player = ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None"]
stats_and_movesets_second_player = ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None"]
stats_and_movesets_third_player = ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None"]
stats_and_movesets_fourth_player = ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None"]
stats_and_movesets_fifth_player = ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None"]
stats_and_movesets_sixth_player = ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None"]

#creates arrays that hold wild and raid pokemon information
stats_and_movesets_wild_pokemon = ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None"]
stats_and_movesets_raid_pokemon = ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None"]


#This code allows pokemon to learn moves when they level up
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
#This code gives xp to the player when a pokemon is defeated
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
#The following functions(grass-ghost) create a typing chart, which allows for super effective and not very effective moves
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

#This code checks what type the move is and runs it through a function
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
    elif pokemon_type == "Fighting":
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

#this code calculates damage from one pokemon to another based on type, defense, attack, EVs, IVs, critical hits, and Same Type effectiviness(STAB)
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
#This code allows the enemy to chose a move based on the type of the opposing pokemon
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
#This code gives the user the option to choose their starting pokemon
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
#this code calculates health based on EVs, IVs, and base health
def health_calculator(who, level,pokemon):
    who[20] = round(((2*pokemon[2] + who[8] + (who[14] / 4)) * level)/100 + level + 10,0)
    return who[20]
#This code calculates all other stats based on EVs, IVs, and base stats
def stat_generator(who, level, pokemon):

    who[21] = round((((2*pokemon[3]) + who[9] + (who[15] / 4)) * level)/100 + 5,0)

    who[22] = round((((2*pokemon[4]) + who[10] + (who[16] / 4)) * level)/100 + 5,0)

    who[23] = round((((2*pokemon[5]) + who[11] + (who[17] / 4) * level))/100 + 5,0)

    who[24] = round((((2*pokemon[6]) + who[12] + (who[18] / 4) * level))/100 + 5,0)

    who[25] = round((((2*pokemon[7]) + who[13] + (who[19] / 4) * level))/100 + 5,0)

#This code generates IVs thatare random values from 0-31 which influnce the stats of the pokemon
def iv_generator(who):

    who[8] = random.randint(0,31)

    who[9] = random.randint(0,31)

    who[10] = random.randint(0,31)

    who[11] = random.randint(0,31)

    who[12] = random.randint(0,31)

    who[13] = random.randint(0,31)
#This code generates IVs thatare random values from 15-31 which influnce the stats of the pokemon, the values are higher to ensure that your starter is strong
def iv_generator_starter(who):

    who[8] = random.randint(15,32)

    who[9] = random.randint(15,32)

    who[10] = random.randint(15,32)

    who[11] = random.randint(15,32)

    who[12] = random.randint(15,32)

    who[13] = random.randint(15,32)
#This code generates a random ability for pokemon
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
#Generates moves for any non-raid pokemon
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
#This generates moves for raid pokemon, different because raid pokemon only have 4 moves
def move_generator_raid(who, pokemon):
    who[2] = pokemon[13]
    who[3] = pokemon[14]
    who[4] = pokemon[15]
    who[5] = pokemon[16]
#This code generates a random level for other pokemon based on the current route
def level_generator(route):
    x = 1
    if route == 1:
        x = random.randint(1,4)
    elif route == 2:
        x = random.randint(4,8)
    elif route == 3:
        x = random.randint(8,12)
    return x
# This code generates stats for any wild pokemon, it uses the functions: level generator, move_generator, iv_generator, health_calculator, stat_generator
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
# This code generates stats for any starter, it uses the functions: move_generator, iv_generator, health_calculator, stat_generator, gives base level 5
def give_stats_starter(who, pokemon):
    who[31] = pokemon
    who[27] = 5
    who[0] = 0
    move_generator_raid(who,pokemon)
    who[6] = xp_levels[1+who[27]]
    ability_generator(who, pokemon)
    iv_generator_starter(who) 
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
# This code generates stats for any raid pokemon, it uses the functions: move_generator, iv_generator, health_calculator, stat_generator, gives base level 10
def give_stats_raid(who, pokemon):
    who[31] = pokemon
    who[27] = 10
    who[0] = 0
    move_generator_raid(who,pokemon)
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
    who[20] = health_calculator(who,who[27],pokemon)
    # Real Health
    stat_generator(who,who[27],pokemon)
    who[1] = who[20]
    # Health calculated last
# Displays infomation about the current wild battle and allows the player to chose their actions
def display_info(player_current,oppenent_current):
    print(f"{str(player_current[26])} is at {str(player_current[1])} HP! {str(oppenent_current[26])} is at {str(oppenent_current[1])} HP!")
    while True:
        answer = input("Will you 'Battle', 'Swap Pokemon', or 'Use Pokeball': ")
        if answer.lower() == "battle":
            return "battle"
        if answer.lower() == "swap pokemon":
            return "swap pokemon"
        if answer.lower() == "use pokeball":
            return "use pokeball"
        else:
            print("Invalid, try again.")
# Displays infomation about the current raid battle and allows the player to chose their actions, not able to throw pokeball
def display_info_raid(player_current,oppenent_current):
    print(f"{str(player_current[26])} is at {str(player_current[1])} HP! {str(oppenent_current[26])} is at {str(oppenent_current[1])} HP!")
    while True:
        answer = input("Will you 'Battle' or 'Swap Pokemon': ")
        if answer.lower() == "battle":
            return "battle"
        if answer.lower() == "swap pokemon":
            return "swap pokemon"
        else:
            print("Invalid, try again.")
# Displays the players current moves and allows them to chose one or go back
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
        move_selection = int(input("Select 1, 2, 3, 4 to select a move or 0 to go back: "))
        if move_selection == 1 or move_selection == 2 or move_selection == 3 or move_selection == 4 or move_selection == 0:
            return move_selection
# displays the playey's swap choices and allows them to swap to one or to go back
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
                break
        if options[1] != "None":
            if swap_choice.lower() == options[1][26].lower():
                team_current = options[1]
                break
        if options[2] != "None":
            if swap_choice.lower() == options[2][26].lower():
                team_current = options[2]
                break
        if options[3] != "None":
            if swap_choice.lower() == options[3][26].lower():
                team_current = options[3]
                break
        if options[4] != "None":
            if swap_choice.lower() == options[4][26].lower():
                team_current = options[4]
                break
        if swap_choice.lower() == "back":
            break
        if swap_choice == True:
            print("Invalid")
    return team_current
# displays the player's swap choices when their current pokemon faints, ends the game if the player is out of options
def faint_swap(team_current):
    swap_x = True
    pokemon_list_counter = 0
    swap_choice = None
    options = ["None","None","None","None","None"]
    print(f"{team_current[26]} Fainted!")
    if team[0] != team_current and team[0][26] != "None" and team[0][1] > 0:
                    print(f"{team[0][26]}: {int(team[0][1])}HP")
                    options[pokemon_list_counter] = team[0]
                    pokemon_list_counter += 1
    if team[1] != team_current and team[1][26] != "None" and team[1][1] > 0:
                    print(f"{team[1][26]}: {int(team[1][1])}HP")
                    options[pokemon_list_counter]= team[1]
                    pokemon_list_counter += 1
    if team[2] != team_current and team[2][26] != "None" and team[2][1] > 0:
                    print(f"{team[2][26]}: {int(team[2][1])}HP")
                    options[pokemon_list_counter] = team[2]
                    pokemon_list_counter += 1
    if team[3] != team_current and team[3][26] != "None" and team[3][1] > 0:
                    print(f"{team[3][26]}: {int(team[3][1])}HP")
                    options[pokemon_list_counter] = team[3]
                    pokemon_list_counter += 1
    if team[4] != team_current and team[4][26] != "None" and team[4][1] > 0:
                    print(f"{team[4][26]}: {int(team[4][1])}HP")
                    options[pokemon_list_counter] = team[4]
                    pokemon_list_counter += 1
    if team[5] != team_current and team[5][26] != "None" and team[5][1]> 0:
                    print(f"{team[5][26]}: {int(team[5][1])}HP")
                    options[pokemon_list_counter] = team[5]
                    pokemon_list_counter += 1
    if options[0] != "None":
        pass
    else:
        print("You Fainted! Game Over!")
        exit()
    while swap_x:
        swap_choice = input(f"Enter one of the following to swap to: ")
        if options[0] != "None":
            if swap_choice.lower() == options[0][26].lower():
                team_current = options[0]
                swap_x = False
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
    return team_current, False
# makes a random new wild pokemon
def new_wild(route):
    if route == 1:
        give_stats(stats_and_movesets_wild_pokemon,random.choice(first_route_pokemon))
        return stats_and_movesets_wild_pokemon
# makes a rand new raid pokemon
def new_raid():
        give_stats_raid(stats_and_movesets_raid_pokemon,random.choice(raid_pokemon))
        return stats_and_movesets_raid_pokemon
# Calculates if a pokeball catches a wild pokemon
def pokeball_catch_calculator(health,total_health):
    catch_percent = round(health/total_health*100/2)
    if random.randint(1,100) >= catch_percent:
        return True
    else:
        return False
#The code to battle a wild pokemon(Further comments inside)
def battle_wild(team,enemy):
    #Sets beginning varibles
    #Turnused checks to see if the user has used an action
    turnused = False
    #X, y, z are used for loops
    x = True
    y = True
    z = True
    #catch_counter keeps track of the current pokeball successes(3 to catch)
    catch_counter = 0
    #Sets the active pokemon to your first non-fainted pokemon
    if team[0][1] > 0 and team[0] != "None":
        team_current = team[0]
    elif team[1][1] > 0 and team[1] != "None":
        team_current = team[1]
    elif team[2][1] > 0 and team[2] != "None":
        team_current = team[2]
    elif team[3][1] > 0 and team[3] != "None":
        team_current = team[3]
    elif team[4][1] > 0 and team[4] != "None":
        team_current = team[4]
    elif team[5][1] > 0 and team[5] != "None":
        team_current = team[5]
    #Makes it so that you have no selected move and you haven't captured a pokemon
    move_select = None
    captured = False
    print("A wild", enemy[26], "appeared!")
    #begin loops
    while x:
        while y:
            #sets selected move to none
            move_select = None
            #oppennet choses their move based on your current type
            oppenent_move = oppennet_AI(enemy,team_current)
            #you choice what action you want to do
            choice = display_info(team_current,enemy)
            if choice == "battle":
                move_select =  display_moves(team_current)
                if move_select == 0:
                    turnused = False
                else:
                    turnused = True
            
            elif choice ==  "swap pokemon":
                #rn is used to check if the player swaps their pokemon
                rn = team_current
                team_current = swap_team(team_current)
                if rn != team_current:
                    turnused = True
                else:
                    turnused = False
            elif choice == "use pokeball":
                #begins loop
                while z:
                    #catch is True or False if true adds to counter until pokemon is captured
                    catch = pokeball_catch_calculator(enemy[1],enemy[20])
                    if catch == True:
                        catch_counter += 1
                    if catch == False:
                        z = False
                        print("The pokemon broke out of the ball!")
                        captured = False
                    elif catch_counter == 1 and catch == True:
                        print("The ball shoke once!")
                    elif catch_counter == 2 and catch == True:
                        print("The ball shoke twice!")
                    elif catch_counter == 3 and catch == True:
                        print("The Pokemon was captured!")
                        captured = True
                        z = False
                '''if captured == True:
                        if team[1][26] == "None":
                            team[1][0] = enemy
                            print(enemy[26], "Was added to your Party!")
                            x = False
                            y = False
                            break
                        elif team[2][26] == "None":
                            team[2] = enemy
                            print(enemy[26], "Was added to your Party!")
                            x = False
                            y = False
                            break
                        elif team[3][26] == "None":
                            team[3] = enemy
                            print(enemy[26], "Was added to your Party!")
                            x = False
                            y = False
                            break
                        elif team[4][26]== "None":
                            team[4] = enemy
                            print(enemy[26], "Was added to your Party!")
                            x = False
                            y = False
                            break
                        elif team[5][26] == "None":
                            team[5] = enemy
                            print(enemy[26], "Was added to your Party!")
                            x = False
                            y = False
                            break
                        else:'''
                #When captured is True checks to see if user wants to swap pokemon
                if captured == True:
                    while x:
                                #After user makes their choice the program exits the battle_wild()
                                print(team[0][26])
                                print(team[1][26])
                                print(team[2][26])
                                print(team[3][26])
                                print(team[4][26])
                                print(team[5][26])
                                player_swap = int(input("Enter a number from 1 to 6 to choice which pokemon you would like to swap!\nIf you do not want to swap a pokemon enter 0!"))                                
                                if player_swap == 1:
                                    team[0] = enemy
                                    x = False
                                    y = False
                                    turnused = False
                                if player_swap == 2:
                                    team[1] = enemy
                                    x = False
                                    y = False
                                    turnused = False
                                if player_swap == 3:
                                    team[2] = enemy
                                    x = False
                                    y = False
                                    turnused = False
                                if player_swap == 4:
                                    team[3] = enemy
                                    x = False
                                    y = False
                                    turnused = False
                                if player_swap == 5:
                                    team[4] = enemy
                                    x = False
                                    y = False
                                    turnused = False
                                if player_swap == 6:
                                    team[5] = enemy
                                    x = False
                                    y = False
                                    turnused = False
                                if player_swap == 0:
                                    x = False
                                    y = False
                                    turnused = False
                                    print("Batte Successful!")
                                    break
                else:
                        turnused = True
                        z = False
                z = True           
            #This code happens after the user makes an action
            if turnused == True:
                #Checks to see if the user used a move
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
                    #This code calculates damage, who moves first, if player faints or if oppennent faints.
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
                            #allows player to swap
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
            turnused = False
            catch_counter = 0
#This code is the same as battle_wild(), however, you are not able to use pokeballs and have the option to put the raid pokemon on your team after                
def battle_raid(team,enemy):
    run = False
    turnused = False
    x = True
    y = True
    z = True
    x = True
    if team[0][1] > 0 and team[0] != "None":
        team_current = team[0]
    elif team[1][1] > 0 and team[1] != "None":
        team_current = team[1]
    elif team[2][1] > 0 and team[2] != "None":
        team_current = team[2]
    elif team[3][1] > 0 and team[3] != "None":
        team_current = team[3]
    elif team[4][1] > 0 and team[4] != "None":
        team_current = team[4]
    elif team[5][1] > 0 and team[5] != "None":
        team_current = team[5]
    move_select = None
    print("A Strong looking", enemy[26], "appeared!")
    while x:
        while y:
            move_select = None
            oppenent_move = oppennet_AI(enemy,team_current)
            choice = display_info_raid(team_current,enemy)
            if choice == "battle":
                move_select =  display_moves(team_current)
                if move_select == 0:
                    turnused = False
                else:
                    turnused = True
            elif choice ==  "swap pokemon":
                rn = team_current
                team_current = swap_team(team_current)
                if rn != team_current:
                    turnused = True
                else:
                    turnused = False
                z = True           
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
                            enemy[1] = enemy[20]
                            while True:
                                print(team[0][26])
                                print(team[1][26])
                                print(team[2][26])
                                print(team[3][26])
                                print(team[4][26])
                                print(team[5][26])
                                player_swap = int(input("Enter a number from 1 to 6 to choice which pokemon you would like to swap!\nIf you do not want to swap a pokemon enter 0!"))                                
                                if player_swap == 1:
                                    team[0] = enemy
                                    x = False
                                    y = False
                                    turnused = False
                                    break
                                if player_swap == 2:
                                    team[1] = enemy
                                    x = False
                                    y = False
                                    turnused = False
                                    break
                                if player_swap == 3:
                                    team[2] = enemy
                                    x = False
                                    y = False
                                    turnused = False
                                    break
                                if player_swap == 4:
                                    team[3] = enemy
                                    x = False
                                    y = False
                                    turnused = False
                                    break
                                if player_swap == 5:
                                    team[4] = enemy
                                    x = False
                                    y = False
                                    turnused = False
                                    break
                                if player_swap == 6:
                                    team[5] = enemy
                                    x = False
                                    y = False
                                    turnused = False
                                    break
                                if player_swap == 0:
                                    x = False
                                    y = False
                                    turnused = False
                                    break
                                    print("Batte Successful!")
                                    break
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
                                    x = False
                                    y = False
                                    print(enemy[26] + " Fainted!")
                                    enemy[1] = enemy[20]
                                    while True:
                                        print(team[0][26])
                                        print(team[1][26])
                                        print(team[2][26])
                                        print(team[3][26])
                                        print(team[4][26])
                                        print(team[5][26])
                                        player_swap = int(input("Enter a number from 1 to 6 to choice which pokemon you would like to swap!\nIf you do not want to swap a pokemon enter 0!"))                                
                                        if player_swap == 1:
                                            team[0] = enemy
                                            x = False
                                            y = False
                                            turnused = False
                                            break
                                        if player_swap == 2:
                                            team[1] = enemy
                                            x = False
                                            y = False
                                            turnused = False
                                            break
                                        if player_swap == 3:
                                            team[2] = enemy
                                            x = False
                                            y = False
                                            turnused = False
                                            break
                                        if player_swap == 4:
                                            team[3] = enemy
                                            x = False
                                            y = False
                                            turnused = False
                                            break
                                        if player_swap == 5:
                                            team[4] = enemy
                                            x = False
                                            y = False
                                            turnused = False
                                            break
                                        if player_swap == 6:
                                            team[5] = enemy
                                            x = False
                                            y = False
                                            turnused = False
                                            break
                                        if player_swap == 0:
                                            x = False
                                            y = False
                                            turnused = False
                                            print("Batte Successful!")
                                            break
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
            turnused = False
            catch_counter = 0
#Starts the game
#Creates your team.
team = [stats_and_movesets_first_player,stats_and_movesets_second_player,stats_and_movesets_third_player,stats_and_movesets_fourth_player,stats_and_movesets_fifth_player,stats_and_movesets_sixth_player]
#Receives your starter
selected = choose_pokemon()
#sets route to one
route = 1
#sets your choice to one
your_choice = 1
#sets a loop condition to true
gzh = True
#writes game intro
print("Welcome to the world of Pokemon, here you will you enter many pokemon, and work your way through the game as a pokemon trainer! You can win theis game by defeating a very strong raid, pokemon! This oppenent will be slow, but tough, build your team and goodluck!")
#gives stats to your starter
give_stats_starter(stats_and_movesets_first_player,selected)
#Starts main route
while True:
    #sets loop condition True
    gzh = True
    #Takes player choice does action
    #1 battles a wild pokemon
    if your_choice == 1:
        battle_wild(team,new_wild(route))
    #2 battles a raid pokemon
    elif your_choice == 2:
        print("Entered")
        battle_raid(team,new_raid())
    #starts loop where player needs to input an option
    while gzh:
        #asks user for choice until they input a real option
        your_choice = int(input("Enter 1 to continue or 2 to challenge a raid pokemon or 3 to end: "))
        if your_choice == 1 or your_choice == 2 or your_choice == 3:
            gzh = False
        else:
            print("Invalid, try again")
    #3 ends game
    if your_choice == 3:
        print("Your journey was successful!")
        break
# print(battle_wild(team,new_wild(route)))
# first_route()

