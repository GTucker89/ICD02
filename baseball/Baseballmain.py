def read_baseball_data(file_path):
    names, hits, run, rbis = [],[],[],[]
    try: 
        with open(file_path,"r") as file:
            #Skip the header line
            next(file)
            for line in file:
                data = line.strip().split(',')
                names.append(data[0])
                hits.append(int(data[1]))
                run.append(int(data[2]))
                rbis.append(int(data[3]))
    except FileNotFoundError:
        print(f"Error: File Not Found '{file_path}' not found")
    return names, hits, run, rbis
def display_all_baseball_stats(names,hits,run,rbis):
    for index in range(len(names)):
        print(f"|{names[index]}|{hits[index]}|{run[index]}|{rbis[index]}|")
def calculate_and_display_average(hits,runs,rbis):
    print(f"Average Hits: {round(sum(hits)/len(hits),2)}")
    print(f"Average Runs: {round(sum(runs)/len(runs),2)}")
    print(f"Average Rbis: {round(sum(rbis)/len(rbis),2)}")

if __name__ == "__main__":
    # Specify the file path
    file_path = "baseball_stats.txt"
    # Read baseball data from the file
    names, hits, runs, rbis = read_baseball_data(file_path)
    # Display menu and handle user choices
    while True:
        print("\nMenu:")
        print("1. Display all baseball player statistics")
        print("2. Calculate and display average baseball statistics")
        print("3. Identify player with the most hits")
        print("4. Identify player with the most RBIs")
        print("5. Display top 10 players in a category")
        print("6. Add a new baseball player")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")
        
        if choice == "1":
            print("here")
            display_all_baseball_stats(names,hits,runs,rbis)
        elif choice == "2":            
            calculate_and_display_average(hits,runs,rbis)
        elif choice == "3":
            stat_leader("Hits")
        elif choice == "4":
            statleader("RBIs")
        elif choice == "5":
            category = input("enter the category to display top 10 players")
            display_top_10_in_catergory(category, names, runs,rbis)
        elif choice == "6":
            add_new_player(names,hits,runs,rbis)
        elif choice == "7":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")

