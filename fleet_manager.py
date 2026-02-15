def init_database():
# starting list of names and ranks
 
# all lists are parrale lists if the 3 name is selected then the 3 rank and the 3 id and so on    
    
    Titles = ["Picard", "Riker", "Data", "Forge", "Crusher"]
    Rank = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Commander"]
    Division = ["Command", "Command", "Operations","Operations", "Sciences"]
#ids must be an interger to match correctly
    
    Ids = ["1001", "1002", "1003", "1004", "1005"]
#sir the hardest thing so far is finding the names and roles of the characters as i have never watched star trek XD

    return Titles, Rank, Division, Ids

print("terminal activation")
print("systerm loading")
print("systerm open")
print("welcome user")
print("="*20)

# this is the opening welcome message to the user 

def display_menu():
#prints the main menu at the beggining of every loop          

#returns the inpuit choice so main() can choice the right function to pull            
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
           
    return choice

def display_roster(Titles, Rank, Division, Ids):
#shows the full crew list
 
#i used a range(len()) to keep all 4 lists alligned 
      
    print("roster solected")
    print("loading please tsand by ")
    print("====displaying roster====")
    print("=" * 20)
     
    for i in range(len(Titles)):
        print(f"<  {Titles[i]}  >  <  {Rank[i]}  >  <  {Division[i]}  >  <  {Ids[i]}  >")

        print("=" * 20)

def add_member(Titles, Rank, Division, Ids):
#this function adds the new crewmen to all 4 lists
 
#also it validates the rank with tng and always creates a new id      
    print("add member selected")
    print("loading please stand by")
    print("====add member====")
#all the valed tng ranks i could find i think i got them all 

    valid_Ranks = [
        "Admiral", "Captain", "Commander", "Lt. Commander",
        "Lieutenant", "Lieutenant Junior Grade", "Ensign",
        "Chief Petty Officer", "Petty Officer", "Crewman",
        "Chief Engineer", "Chief Medical Officer",
        "Counselor", "Tactical Officer"
    ]

    new_Title = input("insert crew members name ")
    new_Rank = input("insert new crem members rank ")
#checks if the input rank is the same as a valid rank 

    if new_Rank not in valid_Ranks:
        print("error: Rank not recognised. failed to add member.")
        print("=" * 20)

    new_Division = input("insert new crew members division ")
    new_Ids = input("insert new crew members I'd ")
#makes sure the IDS do not overlap

    if new_Ids in Ids:
        print("error: id already allocated, failed to add member")
        print("please try again with an alternative ID")
        print("=" * 20)
        return
#this adds to allthe lists and stay a parrale list

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
  
    update_id = input("input designated id of a crewmen to update there rank ")

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
    search_term = input("enter name or section of name to search for crewmen ").lower()
#if the full string is found its declared false and inputs the result
    found = False

    for i in range(len(Titles)):
        if search_term in Titles[i].lower():
            print("=" * 20)
            print(f"<  {Titles[i]}  >  <  {Rank[i]}  >  <  {Division[i]}  >  <  {Ids[i]}  >")
            found = True
#if a partal string is input it will compare the partial string to the full string and if so it will be found true and input the result  
    if not found:
        print("no crew members match that search research result.")
        print("please try again")
        print("=" * 20)

def  filter_by_division(Titles, Division):
    print("fillter by division")
    print("please stand by, loading")
    print("====filter by division====")
#only shows crew members in a specific division

#the user but input command, operations, or science 

#if a division has not been added to the data base it will not come up with anything 
    search_div = input("please enter division to fillter by (command, operations, sciences):").lower()

    found = False

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
#this function calculates the crew total by asociating each rank with a cretid amount
    total_pay = 0 
#a list with each rank with its set pay rate
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
#i added more ranks as it looked empty andd i wanted to try and add a full crew to the systerm which i found online 
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
#this function count which ranks count as officers and how many are present
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
#all ranks are based of tng i think 
    for r in Rank:
        if r in officer_ranks:
            officer_count += 1

    print(f"total number of commissioned officers onboard at this time: {officer_count}")
    print("=" * 20)

def main():
#loads the database and keeps the list in parralell acording to there index
#this is my main loop that all the functions are called from
#i used if elif and else staments to do this
    Titles, Rank, Division, Ids = init_database()

#ask for the users name and welocmes them to star fleet comand
#this will keep loping untill the user choices the exit function     
    name = input("what is your name ")
    print("hello", name)
    print("welcome to starfleet comand")
    print("=" *20) 

    while True:
        choice = display_menu() 

        if choice == "1":
            display_roster(Titles, Rank, Division, Ids)
#the display roster
        elif choice == "2":
            add_member(Titles, Rank, Division, Ids)
#add new crew member
        elif choice == "3":
            remove_member(Titles, Rank, Division, Ids) 
#remove crew member
        elif choice == "4":
            update_rank(Titles, Rank, Ids)
#update rank
        elif choice == "5":
            search_crew(Titles, Rank, Division, Ids)
#search crew tab
        elif choice == "6":
            filter_by_division(Titles, Division)
#filter by division
        elif choice == "7":
            total = calculate_payroll(Rank)
            
#calculate payroll
        elif choice == "8":
            count = count_officers(Rank) 
            
#count officers 
        elif choice == "9":
            print("exit terminal")
            print("shut down in progress")
            print("loading")
            print("shutdown compleate")
            print("live long and prosper")
            print("=" * 20)
            break
#exit the programe
#end the while true loop        
        else:
            print("option not avaliable")
            print("try gain")
#handles non valid inputs 
#starts the program
main()