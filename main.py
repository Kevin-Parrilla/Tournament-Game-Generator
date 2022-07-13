# this will store a value for number of teams in tournament
num_teams = input("Enter the number of teams in the tournament: ")

# team naming -- need to store the team names in some way
for num in range(int(num_teams)):
    num = 1
    team_names = {}

    while num <= int(num_teams):
        new_team = input(f"Enter the name for team #{num}: ")
        team_names[f"team #{num}"] = new_team
        num +=1
    break

# number of games played by each team
num_games = input("Enter the number of games played by each team: ")

# number of wins each team had