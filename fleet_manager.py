def init_database():
#starting list of names and ranks and over info
    Titles = ["Picard", "Riker", "Data", "Forge", "Crusher"]
    Rank = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Commander"]
    Division = ["Command", "Command", "Operations","Operations", "Sciences"]
    Ids = [1001, 1002, 1003, 1004, 1005] 
#sir the hardest thing so far is finding the names and roles of the characters as i have never watched star trek
    return Titles, Rank, Division, Ids

print("terminal activation")
print("systerm loading")
print("systerm open")
print("welcome user")
print("="*20)


def display_menu():
           
            #prints all the different menu options
            print("1. display roster")
            print("2. add member")
            print("3. remover member")
            print("4. update rank")
            print("5. search crewmen")
            print("6. filter by divisions")
            print("7. calculate payroll")
            print("8. count oficers")
            print("9. exit terminal")
            print("=" * 20)
            #allows the input for the different menus
            choice = input("please select entry ")
            print("=" * 20)

            return choice

def display_roster(Titles, Rank, Division, Ids):
     
     print("roster solected")
     print("loading please tsand by ")
     print("====displaying roster====")
     print("=" * 20)
     
     for i in range(len(Titles)):
          print(f"<  {Titles[i]}  >  <  {Rank[i]}  >  <  {Division[i]}  >  <  {Ids[i]}  >")

          print("=" * 20)
# i used a for in range to print all the caracters with there respected rank division and set id  

def add_member(Titles, Rank, Division, Ids):
     #this section alows new members to be added to the crew by inputing the data in the the init_data base 
     print("add member selected")
     print("loading please stand by")
     print("====add member====")

     new_Title = input("insert crew members name ")
     new_Rank = input("insert new crem members rank")
     new_Division = input("insert new crew members division")
     new_Ids = input("insert new crew members I'd")

     Titles.append(new_Title)
     Rank.append(new_Rank)
     Division.append(new_Division)
     Ids.append(new_Ids)

     print(f"{new_Title} crew member has been officaly added to the crew. ")
     print("=" * 20)

def remove_member(Titles, Rank, Division, Ids):
     print("remeve member selected ")
     print("loading please stand by")
     print("====remove member====")

     remove_id = int(input("please enter the id of the crewmen to be terminated"))

     if remove_id in Ids:
          index = Ids.index(remove_id)

          remove_name = Titles[index]

          Titles.pop(index)
          Rank.pop(index)
          Division.pop(index)
          Ids.pop(index)

          print(f"{remove_name} crew member has been terminated,advised to escort crewmen of board ")
     else:
          print("error: id not recognised ")
          print("=" * 20)     

def main():
#this is my main loop that all the if elif and else loops run through
    Titles, Rank, Division, Ids = init_database()
#ask for the users name and welocmes them to star fleet comand   
    name = input("what is your name ")
    print("hello", name)
    print("welcome to starfleet comand")
    print("=" *20)

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
main()