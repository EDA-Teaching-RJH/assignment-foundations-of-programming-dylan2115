def init_database():

    Titles = ["Picard", "Riker", "Data", "Forge", "Crusher"]
    Rank = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Commander"]
    Division = ["Command", "Command", "Operations","Operations", "Sciences"]
    Ids = [1001, 1002, 1003, 1004, 1005] 

    return Titles, Rank, Division, Ids

print("terminal activation")
print("systerm loading")
print("systerm open")
print("welocome user")
print("="*20)

def main():

    Titles, Rank, Division, Ids = init_database()
    while True:
        choice = display_menu()

        if choice == "1":
            display_roster(Titles, Rank, Division, Ids)

        elif choice == "2":
            add_member(Titles, Rank, Division, Ids)

        elif choice == "3":
            remove_member(Titles, Rank, Division, Ids) 

        elif choice == "4":
            update_rank(Titles, Rank, Ids)

        elif choice == "5":
            search_crew(Titles, Rank, Division, Ids)

        elif choice == "6":
            filter_by_division(Titles, Division)

        elif choice == "7":
            total = calculate_payroll(Rank)
            print("total payroll:",total)

        elif choice == "8":
            count = count_officers(Rank) 
            print("total senior officer count", count)

        elif choice == "9":
            print("exit terminal")
            print("shut down in progress")
            print("loading")
            print("shutdown compleate")
            print("live long and prosper")
            print("=" * 20)
            break
        else:
            print("option not avaliable")
            print("try gain")