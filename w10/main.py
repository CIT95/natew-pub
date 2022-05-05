import random

league_table = []
season_schedule = []
team_list = []
table = [["Club", "Played", "Wins", "Draws", "Losses", "Points"]]
club_season_results = []
club_wins = []
club_draws = []
club_losses = []
club_points = []

print("Welcome to Ash City Football League!")
team_names = ["Fresno", "Central Valley", "Madera", "Clovis",
              "Tower District", "Visalia", "Caruthers", "Cedar Street",
              "Herndon", "Pinedale", "Ranchos"]
club_description = ["SSC", "SC", "FC", "AFC"]
team_number = int(input("How many teams would you like in your league 6 or 8? \
"))
if team_number not in [6, 8]:
    print("Sorry, for right now the number of teams in the league must be 6 \
or 8.")
    team_number = int(input("Would you like 6 or 8 teams? "))
season_length = team_number * 2 - 2
print("Perfect, let's set up a {season_length} week season with \
{team_number} teams!")
user_club = input("What is your club name?\n")
print(f"Welcome to the league {user_club}!")
set_up = int(input("Would you like to enter all club names or have the \
computer generate the other teams?\n(1) --- I'll fill out the other club \
names\n(2) --- Please generate club names for me.\n"))
if set_up = 1:
    for i in range(0, team_number-1):
        team_slot = i + 2
        team = input(f"Club {team_slot} Name: ")
        league_table.append(team)
elif set_up == 2:
    while len(league_table) < (team_number - 1):
        for team in range(0, (team_number)):
            new_club_description = random.choice(club_description)
            if new_club_description == "AFC":
                new_team = new_club_description + " "\
                           + random.choice(team_names)
            else:
                new_team = random.choice(team_names) + " "\
                           + new_club_description
            if new_team not in league_table:
                league_table.append(new_team)
league_table.append(user_club)
game_week = 0
played = season_length
for club in league_table:
    club_wins.append(0)
    club_draws.append(0)
    club_losses.append(0)

decision = True
while decision:
    navigation = input("What would you like to do?\n(1) --- View League \
Clubs\n(2) --- Simulate Game Week\n(3) --- Exit\n")
    if navigation == "1":
        print(league_table)
    elif navigation == "2":
        cycle = True
        while (game_week < season_length) and (cycle):
            game_week += 1
            schedule_switch = True
            players = []
            schedule = [["Game Week", "Teams", "Result"]]
            results = []
            while schedule_switch:
                for i in league_table:
                    team_index = league_table.index(i)
                    players.append(league_table[team_index])
                while len(players) > 0:
                    pairs = random.sample(players, 2)
                    head_to_head = pairs[0] + " vs " + pairs[1]
                    outcome_int = random.randint(0, 2)
                    if outcome_int == 2:
                        outcome = "W"
                        result = (f"{pairs[0]} wins!")
                        win_index = league_table.index(pairs[0])
                        club_wins[win_index] = club_wins[win_index] + 1
                        loss_index = league_table.index(pairs[1])
                        club_losses[loss_index] = club_losses[loss_index] + 1
                    elif outcome_int == 1:
                        outcome = "D"
                        result = (f"{pairs[0]} and {pairs[1]} play to a draw!")
                        draw_index = league_table.index(pairs[0])
                        club_draws[draw_index] = club_draws[draw_index] + 1
                        draw_index = league_table.index(pairs[1])
                        club_draws[draw_index] = club_draws[draw_index] + 1
                    else:
                        outcome = "L"
                        result = (f"{pairs[1]} wins!")
                        loss_index = league_table.index(pairs[0])
                        club_losses[loss_index] = club_losses[loss_index] + 1
                        win_index = league_table.index(pairs[1])
                        club_wins[win_index] = club_wins[win_index] + 1
                    player_one = pairs[0]
                    player_two = pairs[1]
                    players.remove(player_one)
                    players.remove(player_two)
                    gameday = [game_week, head_to_head, result]
                    schedule.append(gameday)
                end_of_week = input("(1) --- Progress and view week \
results.\n(2) --- Simulate next week.\n(3) --- Exit to Main Menu\n")
                if end_of_week == "2":
                    schedule_switch = False
                elif end_of_week == "1":
                    for i in schedule:
                        print(i)
                    schedule_switch = False
                elif end_of_week == "3":
                    schedule_switch = False
                    cycle = False
        if game_week == season_length:
            end_of_season = input("What an exciting season! What would you \
like to do next?\n(1) --- View Season Results\n(2) --- Exit\n")
            if end_of_season == "1":
                season_winner_points = 0
                season_winner = ""
                for i in league_table:
                    team = i
                    team_index = league_table.index(i)
                    game_week = season_length
                    wins = club_wins[team_index]
                    draws = club_draws[team_index]
                    losses = club_losses[team_index]
                    points = (wins * 3) + draws
                    team_stats = [team, game_week, wins, draws, losses, points]
                    table.append(team_stats)
                    if points >= season_winner_points:
                        season_winner_points = points
                        season_winner = team
                for i in table:
                    print(i)
                print(f"Congratulations to {season_winner} for winning the \
league!")
                print("See you next season!")
                break
            else:
                cycle = False
                break
    elif navigation == "3":
        print("See you next time!")
        decision = False
        break
