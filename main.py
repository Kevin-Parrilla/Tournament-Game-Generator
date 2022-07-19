# this will store a value for number of teams in tournament
num_teams = input("Enter the number of teams in the tournament: ")

# team naming and storing
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
for num in range(int(num_teams)):
    num = 1
    team_names_lst = list(team_names.values())
    team_wins = {}
    i = 0

    while num <= int(num_teams):
        num_wins = input(f"Enter the number of wins Team {team_names_lst[i]} had: ")
        team_wins[f"Team {team_names_lst[i]}"] = num_wins
        i += 1
        num += 1
    break