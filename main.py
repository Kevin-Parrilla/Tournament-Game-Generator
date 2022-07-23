# this will house the first operation -- taking in the number of teams
def num_of_team():
    global num_teams 
    num_teams = input("Enter the number of teams in the tournament: ")  # this will store a value for number of teams in tournament
    if int(num_teams) < 2:  # this will validate the user input
        print("The minimum number of teams is 2, try again.")
        return num_of_team()

# this will house the second operation -- team naming and storing // LEFT OFF: IF INVALID USER INPUT THEN NEED TO RESUME WHERE IT LEFT OFF INSTEAD OF RESTARTING THE WHOLE LOOP
def name_teams():
    for num in range(int(num_teams)):
        num = 1
        team_names = {}

        while num <= int(num_teams):
            new_team = input(f"Enter the name for team #{num}: ")
            team_names[f"team #{num}"] = new_team
            num += 1
            if len(new_team) < 2:  # validates min char needed for team name
                print("Team names must have at least 2 characters, try again.")
                num += (-1)  # resets team name entry until valid
            elif len(new_team.split()) > 2:  # validates max word len for team name
                print("Team names may have at most 2 words, try again.")
                num += (-1)
            else:
                pass
        print(team_names)
        break
       
num_of_team()
name_teams()
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