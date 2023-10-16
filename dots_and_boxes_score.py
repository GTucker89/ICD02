#Gathers names and game data
name = input("Enter your name: ")
m1 = int(input("Enter your first score: "))
o1 = int(input("Enter your Opponent's first score: "))
oname = input("Enter your first Opponent's name: ")
m2 = int(input("Enter your second score: "))
o2 = int(input("Enter your Opponent's second score: "))
oname2 = input("Enter your second Opponent's name: ")
m3 = int(input("Enter your third score: "))
o3 = int(input("Enter your Opponent's third score: "))
oname3 = input("Enter your third Opponent's name: ")
m4 = int(input("Enter your fourth score: "))
o4 = int(input("Enter your Opponent's fourth score: "))
oname4 = input("Enter your fourth Opponent's name: ")
m5 = int(input("Enter your fifth score: "))
o5 = int(input("Enter your Opponent's fifth score: "))
oname5 = input("Enter your fifth Opponent's name: ")
#Calculates player and oppenent total scores
yts = m1 + m2 + m3 + m4 + m5
ots = o1 + o2 + o3 + o4 + o5
#gathers game percentages
g1p = m1/49*100
g2p = m2/49*100
g3p = m3/49*100
g4p = m4/49*100
g5p = m5/49*100
#gathers your and your opponent's total average percentages
tbp = g5p + g4p + g3p + g2p + g1p
tbpa = round(tbp/5,2)
otbpa = 100-tbpa
#prints game data
print(f"\n{'Name:':<15}")
print(f"{name:<15}")
print(f"{'Oppenent':<8} {'Your Points':>14} {'Oppenent Points':>21} {'Box %':>11}")
print(f"{oname:<8}{m1:>15}{o1:>22}{g1p:>12.2f}")
print(f"{oname2:<8}{m2:>15}{o2:>22}{g2p:>12.2f}")
print(f"{oname3:<8}{m3:>15}{o3:>22}{g3p:>12.2f}")
print(f"{oname4:<8}{m4:>15}{o4:>22}{g4p:>12.2f}")
print(f"{oname5:<8}{m5:>15}{o5:>22}{g5p:>12.2f}")
#prints total games summary
print(f"Total boxes{'Oppenent total Boxes':>26}")
print(f"{yts:>11}{ots:>26}")
print(f"{'Your average box percent':<20}")
print(f"{tbpa:<20}")
print(f"{'Oppenent toal box percent':<20}")
print(f"{otbpa:<20}")



