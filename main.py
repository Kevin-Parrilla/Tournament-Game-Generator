# this will store a value for number of teams in tournament
num_teams = input("Enter the number of teams in the tournament: ")

# team naming -- need to store the team names in some way
for num in range(int(num_teams)):
    num = 1
    
    while num <= int(num_teams):
        print(input(f"Enter the name for team #{num}: "))
        num +=1
    break

    