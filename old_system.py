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
            r.append(new_rank)
            d.append(new_div)
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
            print("High ranking officers: " + str(count)) 
            
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
            print("fuel:",fuel)
            print("Idling...")
            fuel -= 1 
            
        print("End of cycle.")

run_system_monolith()
#line 28 syntax error = should of been == (= is assigning a value == is comparioson)
#line 16 added a end to the loop, originally it was an infinate loop so no code will run for ever becausee it was waiting for a value before ending so i made it so the value would imcrease by one untill it reach the desired value to end the loop  
#line 92 added () to run_system_monolith this is because the function would never be called over wise  
#line 31 originally it was range(10) because i only had 4 things in the list it was causing an index error so i replaced it with (len(n)) which allowed the value to be chnaged 
#line57 originally code reading every rank as true so i alterd it by adding rank == infront of the comander part allowing not every input as true 
#in line 61 the code was trying to print the integer so i made it convert to a string before printing to solve any errors 
#in line 41 and 42 it was only able to add the appending name to the crew list so when it was locking for the appending rank and the appending division it was not able to find it in the list
# line 42 and 41 i had creatyed a new bug by putting my input in to the wrong lists so i had corrected this
# line 88 and 87 i had remove the break in the loop so it would run until i exit the systerm also i added -= 1 so the value would go down in increments of 1 
# line 87 i i added the code the reason i did this is because with out it it would continously frint idling     