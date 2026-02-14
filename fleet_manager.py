def init_database():
    
#starting list of names and ranks and over info for functions to pull info from
    
    Titles = ["Picard", "Riker", "Data", "Forge", "Crusher"]
    Rank = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Commander"]
    Division = ["Command", "Command", "Operations","Operations", "Sciences"]
    Ids = [1001, 1002, 1003, 1004, 1005]

#sir the hardest thing so far is finding the names and roles of the characters as i have never watched star trek XD

    return Titles, Rank, Division, Ids

print("terminal activation")
print("systerm loading")
print("systerm open")
print("welcome user")
print("="*20)

# this is the opening welcome message to the user 

def display_menu():
            
#this function opens no mater the input and prints all the options for the user to use           
            
            print("please selct entry")
            print("1. display roster")
            print("2. add member")
            print("3. remover member")
            print("4. update rank")
            print("5. search crewmen")
            print("6. filter by divisions")
            print("7. calculate payroll")
            print("8. count oficers")
            print("9. exit terminal")
            choice = input("please select entry ")

#the requested input allows for the function in the main loop to be pulled
           
            return choice

def display_roster(Titles, Rank, Division, Ids):
     
     print("roster solected")
     print("loading please tsand by ")
     print("====displaying roster====")
     print("=" * 20)
     
     for i in range(len(Titles)):
          print(f"<  {Titles[i]}  >  <  {Rank[i]}  >  <  {Division[i]}  >  <  {Ids[i]}  >")

          print("=" * 20)

# i used a "for in range" to print all the caracters with there respected rank division and set id this roster will update when the add remove and update rank functions are used   
# also the roster will be used when searching crew 

def add_member(Titles, Rank, Division, Ids):
     #this section alows new members to be added to the crew by inputing the data in the the init_data base 
     
     print("add member selected")
     print("loading please stand by")
     print("====add member====")

     new_Title = input("insert crew members name ")
     new_Rank = input("insert new crem members rank ")
     new_Division = input("insert new crew members division ")
     new_Ids = input("insert new crew members I'd ")

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

#this function askes for a input(id) and removes them from the list and the init database if the id is not recognised then it print a error message
     
     remove_id = input("please enter the id of the crewmen to be terminated ")
     print("=" * 20)

     if remove_id in Ids:
          index = Ids.index(remove_id)

          remove_name = Titles[index]

          Titles.pop(index)
          Rank.pop(index)
          Division.pop(index)
          Ids.pop(index)

          print(f"crew member {remove_name} has been terminated, advised to escort crewmen of board ")
          print("=" * 20)
     else:
          print("error: id not recognised ")
          print("=" * 20) 

def update_rank(Titles, Rank, Ids):
     print("update rank selected ")
     print("loading,please stand by ")
     print("====update rank====")

#this function askes for a id and then a new rank to change again if the is is not recgnised it sends a error message
  
     update_id = int(input("input designated id of a crewmen to update there rank"))

     if update_id in Ids:
          index = Ids.index(update_id)

          print(f"current rank {Titles[index]} is {Rank[index]}")
          new_rank = input("please enter the new rank: ")
          Rank[index] = new_rank
          print(f"{Titles[index]}'s rank has been promoted to {new_rank} congratulations.")
          print("=" * 20)
     else:
          print("error: id not rcognised, plese try again")
          print("=" * 20)

def search_crew(Titles, Rank, Division, Ids):
     print("search crewmen selected ")
     print("please stand by, loading")
     print("====search crewmen selected====")
#this function searches for crewmen via a full string or a partical string.
     search_term = input("enter name or section of name to search for crewmen ")
#if the full string is found its declared false and inputs the result
     found = False

     for i in range(len(Titles)):
          if search_term in Titles[i].lower():
               print("=" * 20)
               print(f"<  {Titles[i]}  >  <  {Rank[i]}  >  <  {Division[i]}  >  <  {Ids[i]}  >")
               found = True
#if a partal string is input it will compare the partial string to the full string and if so it will be found true and input the result  
     if not found:
          print("no crew members match that search research.")
          print("please try again")
          print("=" * 20)

def  filter_by_division(Titles, Division):
     print("fillter by division")
     print("please stand by, loading")
     print("====filter by division====")

     search_div = input("please enter division to fillter by (command, operations, sciences):").lower()

     found = True

     for i in range(len(Division)):
          if Division[i].lower() == search_div:
               print("=" * 20)
               print(f"<  {Titles[i]}  >  <  {Division[i]}  >  ")
               found = True
               print("=" * 20)

     if not found:
          print("no crewmen present in this division.")
          print(" * 20")

def calculate_payroll(Rank):
     print("calculate payrole selected")
     print("please stand by, loading")
     print("====calculate payrole====")

     total_pay = 0 

     pay_rates = {
        "Admiral": 7000,
        "Captain": 5000,
        "Commander": 4000,
        "Lt. Commander": 3500,
        "Lieutenant": 3000,
        "Lieutenant Junior Grade": 2800,
        "Ensign": 2500,
        "Chief Petty Officer": 2200,
        "Petty Officer": 2000,
        "Crewman": 1800,
        "Chief Engineer": 4500,
        "Chief Medical Officer": 4500,
        "Counselor": 4200,
        "Tactical Officer": 4000
     } 
     for r in Rank:
          if r in pay_rates:
               total_pay += pay_rates[r]
          else:
               print(f"warning: rank not recognised '{r}',no pay added to total")
              
     print(f"total payroll for all crew members is {total_pay} credits.")
     print("=" * 20)

def count_officers(Rank):
     print("officer count selected")
     print("please stand by ")
     print("====officer count selected====")

     officer_ranks = [
          "Admrial",
          "Captain",
          "Commander",
          "Lt. Commander",
          "Lieutenant",
          "Lieutenant Junior Grade",
          "Ensign"
     ]
     officer_count = 0

     for r in Rank:
          if r in officer_ranks:
               officer_count += 1

     print(f"total number of commissioned officers onboard at this time: {officer_count}")
     print("=" * 20)

def main():

#this is my main loop that all the if elif and else loops run through

    Titles, Rank, Division, Ids = init_database()

#ask for the users name and welocmes them to star fleet comand
    
    name = input("what is your name ")
    print("hello", name)
    print("welcome to starfleet comand")
    print("=" *20)

#also it is where all the functions are called from allowing the systerm to run 

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