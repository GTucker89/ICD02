def caught_speeding(speed, is_birthday):
    if speed <= 60:
        return "No Ticket"
    elif is_birthday == True and speed <= 65:
        return "No Ticket"
    elif is_birthday == True and speed <= 85:
        return "Small Ticket"
    elif speed > 60 and speed <= 80:
        return "Small Ticket"
    elif speed >= 81:
        return "Big Ticket"
def notstrings(s):
    if s[0:3] == "not":
        return s
    else:
        return "not"+s
def squirel_play(temp, summer):
    if summer == True:
      if temp >= 60 and temp <= 100:
          return True
      else:
          return False
    else:
        if temp >= 60 or temp <= 100:
            return True
        else:
            return False
def in1020(a,b):
    if (a >= 10 and a <= 20) or (b >= 10 and b <= 20):
        return True
    else:
        return False
def theEnd(s, location):
    if s == "":
       return "empty"
    else:
        length = len(s)
        if location == True:
            return s[0:1]
        else:
           return s[length-1:length]
           




print(notstrings("hello"))
print(caught_speeding(81, True))
print(squirel_play(89,True))
print(in1020(1,20))
print(theEnd("hello", False))