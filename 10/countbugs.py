

def input_bug_counts(bug_type):
    numbugs = int(input(f"How many {bug_type} are there: "))
    return numbugs

def calculate_percent(total,count):
    bug_percent = int(count)/int(total)
    return bug_percent

def bug_type_and_count():
    bug_type = input("Enter bug type: ")
    numbug = input_bug_counts(bug_type)
    return bug_type, numbug

# def print_next_line(index_position):
#     print(f"{bug_types[index_position]:<15}{bug_count[index_position]:>8}{bug_percent[index_position]:>15.2%}")

    
def display_table(bug1,count1,bug2,count2,bug3,count3):
    print(f"{'Bug type'}{'Count':>15}{'Percentage':>15}")
    print("="*38)
    print(f"{bug_type_one:<15}{bug_count_one:>8}{calculate_percent(total,bug_count_one):>15.2%}")
    print(f"{bug_type_two:<15}{bug_count_two:>8}{calculate_percent(total,bug_count_two):>15.2%}")
    print(f"{bug_type_three:<15}{bug_count_three:>8}{calculate_percent(total,bug_count_three):>15.2%}")
    print("="*38)
    print(f"{'Total'}{total:>18}{'100%':>15}")

# def display_table(array):
#      print(f"{'Bug type'}{'Count':>15}{'Percentage':>15}")
#      print("="*38)
#      t =0
#      while t < array:
#          print("T = " + str(t))
#          print_next_line(t)
#          t = t + 1
#      print("="*38)
#      print(f"{'Total'}{total:>18}{'100%':>15}")

bug_type_one = input("Enter First Bug: ")
bug_count_one = input("Enter First Bug count: ")
bug_type_two = input("Enter Second Bug: ")
bug_count_two = input("Enter Second Bug count: ")
bug_type_three = input("Enter Third Bug: ")
bug_count_three = input("Enter Third Bug count: ")

total = bug_count_two + bug_count_one + bug_count_three
display_table(bug_type_one,bug_count_one,bug_type_two,bug_count_two,bug_type_three,bug_type_three)



# next = "Yes"
# array_len = int(input("How many bugs do you want to enter: "))
# bug_types = [array_len]
# bug_count = [array_len]
# bug_percent = [array_len]
# for i in range(array_len):
#     bug_types[i], bug_count[i] = bug_type_and_count()

# print(len(bug_types))
# x = 0

# total_bugs = 0
# while x < len(bug_types):
#     total = total_bugs + bug_count[x]
#     x = x + 1
# x = 0
# while x < len(bug_types):
#     bug_percent[x] = calculate_percent(total, bug_count[x])
#     x = x + 1
# print(display_table(array_len))



