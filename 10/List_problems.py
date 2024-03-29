def word_average(words):
    y = 0
    for x in range(len(words)):
        y += len(words[x])
    return y / len(words)
def pal_count(words):
    y = 0
    for x in range(len(words)):
        if words[x] == words[x][::-1]:
           y += 1
    return y
def make_str(words):
    total = ""
    for x in range(len(words)):
        if x == 0:
            total += words[x]
        else:
            total += " " + words[x]
    return total
def vowels(words):
    vowels = "aeiuoy"
    y = 0
    for x in range(len(words)):
            y += words[x].count("a")
            y += words[x].count("e")
            y += words[x].count("i")
            y += words[x].count("u")
            y += words[x].count("o")
            y += words[x].count("y")
    return y
def upperlower(words):
    u = 2
    new = []
    for x in range(len(words)):
        if u % 2 == 0:
            new.append(words[x].lower())
        else:
            new.append(words[x].upper())
        u += 1
    return new
def negpos(nums):
    neg = []
    pos = []
    for x in range(len(nums)):
        if nums[x] >= 0:
            pos.append(nums[x])
        else:
            neg.append(nums[x])
    return neg, pos
def fibcheck(nums):
    if nums[0] == 0:
        for x in range(2,len(nums)):
            if nums[1] == 1:
                pass
            else:
                return False
            if nums[x] == nums[x - 1] + nums[x - 2]:
                pass
            else:
                return False
    else:
        for x in range(2,len(nums)):
            if nums[x] == nums[x - 1] + nums[x - 2]:
                pass
            else:
                return False
    return True
import math
def squareroots(nums):
    square = []
    for x in range(len(nums)):
        square.append(round(math.sqrt(nums[x])))
    return square
def runningaverage(nums):
    val = 0
    averages = []
    numsx = []
    for x in range(len(nums)):
        numsx.append(nums[x])
        val = 0
        for y in range(len(numsx)):
            val += numsx[y]
        averages.append(val / len(numsx))
    return averages
def consecutive(nums):
    for x in range(len(nums)-1):
        if nums[x] == nums[x + 1] - 1 or nums[x] == nums[x + 1] + 1:
            return True
    return False
print(word_average(["aa","bbbb","ccc"]))
print(pal_count(["papap","word","mom"]))
print(make_str(["hi", "bye", "hi"]))
print(vowels(["aaa", "b"]))
print(upperlower(["hello","python","java"]))
print(negpos([6,-5,7,3,-9]))
print(fibcheck([0,1,1,2,3,5,8,13,21]))
print(squareroots([8,5,16,36]))
print(runningaverage([8,4,6,7,2]))
print(consecutive([1,1,1,1,4,2]))