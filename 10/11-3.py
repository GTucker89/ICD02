def wins():
    Match1 = input ("Enter First Match")
    Match2 = input ("Enter Second Match")
    Match3 = input ("Enter Third Match")
    Match4 = input ("Enter Fourth Match")
    Match5 = input ("Enter Fifth Match")
    Match6 = input ("Enter Sixth Match")
    Total_win = 0
    if Match1 == "W":
        Total_win += 1
    if Match2 == "W":
        Total_win += 1
    if Match3 == "W":
        Total_win += 1
    if Match4 == "W":
        Total_win += 1
    if Match5 == "W":
        Total_win += 1
    if Match6 == "W":
        Total_win += 1
    if Total_win == 0:
        return -1
    if Total_win == 1 or Total_win ==2:
        return 1
    if Total_win == 3 or Total_win ==4:
        return 2
    if Total_win == 5 or Total_win ==6:
        return 3
print(wins())