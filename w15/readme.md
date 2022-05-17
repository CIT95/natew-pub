# LeagueTable Class

## Methods
   - user_club_name()
    Returns a str of user's input club name.
   
   - computer_club_creation(user_name, num_teams)
     Returns list of randomly generated club names based on determined number of teams.
     Takes the user's club name and number of teams.
     e.g. ["Fresno FC", "Fresno SC", "AFC Madera", "Clovis SSC", "Central Valley SC"]

   - user_team_creation(user_name, num_teams)
     Returns list of user generated club names based on determined number of teams and input prompt.
     Takes the user's club name and number of teams.
     e.g. ["Fresno FC", "Fresno SC", "AFC Madera", "Clovis SSC", "Central Valley SC"]

   - league_size()
     Determines the number of teams in the league. Returns an int.

# FieldChart Class

## Methods
   - show_field()
     Draws a field diagram using Turtle in GUI.

   - visualize_winner(num_teams, club_points)
     Calculates distance relative to field size from points. Illustrates in GUI

# SeasonCalc Class

## Methods
   - club_point_tally(games_won, games_drawn)
     Determines club's point tally. Returns int of club points.

   - season_calc(num_team)
     Determines season length based on number of teams. Returns int of season length.


