n = ["Picard", "Riker", "Data", "Worf"]
r = ["Captain", "Commander", "Lt. Commander", "Lieutenant"]
d = ["Command", "Command", "Operations", "Security"]

active = True

def run_system_monolith():
    print("BOOTING SYSTEM...")
    print("...")
    print("WELCOME TO FLEET COMMAND")
    
    
    loading = 0
    while loading < 5:
        print("Loading module " + str(loading))
        loading += 1
    
    while True:
        print("\n--- MENU ---")
        print("1. View Crew")
        print("2. Add Crew")
        print("3. Remove Crew")
        print("4. Analyze Data")
        print("5. Exit")
        
        opt = input("Select option: ")
        
        if opt == "1":  
            print("Current Crew List:")
            
            for i in range(len(n)):
                print(n[i] + " - " + r[i]) 
                
        elif opt == "2":
            new_name = input("Name: ")
            new_rank = input("Rank: ")
            new_div = input("Division: ")
            
           
            n.append(new_name)
            print("Crew member added.")
            
        elif opt == "3":
            rem = input("Name to remove: ")
           
            idx = n.index(rem)
            n.pop(idx)
            r.pop(idx)
            d.pop(idx)
            print("Removed.")
            
        elif opt == "4":
            print("Analyzing...")
            count = 0
            
            for rank in r:
                if rank == "Captain" or rank == "Commander": 
                    count = count + 1
            print("High ranking officers: " + count) 
            
        elif opt == "5":
            print("Shutting down.")
            break
            
        else:
            print("Invalid.")
            
        
        x = 10
        if x > 5:
            print("System Check OK")
        else:
            print("System Failure")
            
       
        if len(n) > 0:
            print("Database has entries.")
        if len(n) == 0:
            print("Database empty.")

        
        fuel = 100
        consumption = 0
        while fuel > 0:
            
            print("Idling...")
            break 
            
        print("End of cycle.")

run_system_monolith()
#line 28 syntax error = should of been == (= is assigning a value == is comparioson)
#line 16 added a end to the loop originally an infinate loop so no code will run after 
#added () to run_system_monolith 
#line 31 n is a list so it dosent work in the range so len(n) which added a integer range 
#line57 originally code reading every rank as true so i alterd it by adding rank == infront of the comander part allowing not every input as true 
