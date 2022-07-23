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
        global team_names
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
        break

# number of games played by each team
def games_played():
    min_games = int(num_teams) - 1
    global num_games
    num_games = input("Enter the number of games played by each team: ")
    if int(num_games) < min_games:  # validates user input
        print("Invalid number of games. Each team plays each other at least once in the regular season, try again.")
        return games_played()

# number of wins each team had
def win_record():
    for num in range(int(num_teams)):
        num = 1
        team_names_lst = list(team_names.values())
        team_wins = {}
        i = 0
        max_wins = int(num_games)
        min_wins = 0

        while num <= int(num_teams):
            num_wins = input(f"Enter the number of wins Team {team_names_lst[i]} had: ")
            team_wins[f"Team {team_names_lst[i]}"] = num_wins
            i += 1
            num += 1
            if int(num_wins) < min_wins:
                print("The minimum number of wins is 0, try again.")
                i += (-1)
                num += (-1)
            elif int(num_wins) > max_wins:
                print(f"The maximum number of wins is {int(num_games)}, try again.")
                i += (-1)
                num += (-1)
        break

num_of_team()
name_teams()
games_played()
win_record()