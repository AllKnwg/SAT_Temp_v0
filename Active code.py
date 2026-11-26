# This program flags SAT Temps on BAS systems
# needs to add place to add file for parsing
database = input("Enter the path to the file for parsing: ")
print("You entered the following file path: " + database)
# parse file and list out all SAT Temps

with open(database, 'r') as file:
    for line in file:
        if 'SAT' in line:
            print(line.strip())
# in these temps read, flag any that are outside the  range of 3 degrees higher or lower than set point 
set_point = float(input("Enter the set point for SAT Temps: "))
with open(database, 'r') as file:
    for line in file:
        if 'SAT' in line:
            try:
                temp = float(line.split()[-1])
                if temp < set_point - 3 or temp > set_point + 3:
                    print("Flagged SAT Temp: " + line.strip())
            except ValueError:
                continue    
# create a report of flagged SAT Temps
with open(database, 'r') as file:
    for line in file:
        if 'SAT' in line:
            try:
                temp = float(line.split()[-1])
                if temp < set_point - 3 or temp > set_point + 3:
                    print("Report - Flagged SAT Temp: " + line.strip())
            except ValueError:
                continue
# color code flagged SAT Temps in the report
with open(database, 'r') as file:
    for line in file:
        if 'SAT' in line:
            try:
                temp = float(line.split()[-1])
                if temp < set_point - 3 or temp > set_point + 3:
                    print("\033[31mReport - Flagged SAT Temp: " + line.strip() + "\033[0m")  # red color for flagged temps
            except ValueError:
                continue
