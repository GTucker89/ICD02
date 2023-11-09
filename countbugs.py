def input_bug_counts(bug_type):
    numbugs = int(input(f"How many {bug_type} are there: "))
    return numbugs

def calculate_percent(total,count):
    bug_percent = count/total
    return bug_percent

def bug_type_and_count():
    bug_type = input("Enter bug type: ")
    numbug = input_bug_counts(bug_type)
    return bug_type, numbug

def display_table(bug1,count1,bug2,count2,bug3,count3):
    print(f"{'Bug type'}{'Count':>15}{'Percentage':>15}")
    print("="*38)
    print(f"{bug_type_one:<15}{bug_count_one:>8}{calculate_percent(total,bug_count_one):>15.2%}")
    print(f"{bug_type_two:<15}{bug_count_two:>8}{calculate_percent(total,bug_count_two):>15.2%}")
    print(f"{bug_type_three:<15}{bug_count_three:>8}{calculate_percent(total,bug_count_three):>15.2%}")
    print("="*38)
    print(f"{'Total'}{total:>18}{'100%':>15}")

bug_type_one, bug_count_one = bug_type_and_count()
bug_type_two, bug_count_two = bug_type_and_count()
bug_type_three, bug_count_three = bug_type_and_count()
total = bug_count_one + bug_count_two + bug_count_three

display_table(bug_type_one,bug_count_one,bug_type_two,bug_count_two,bug_type_three,bug_count_three)

