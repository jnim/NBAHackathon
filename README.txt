README

My main file of code is PlayoffDatePredictor.py, reads in the Division/Conference Information and Regular Season games (which have been saved separately as CSVs for ease of use). 

My program reads through each game and updates the records of each team. It does not calculate seedings until one team has won 42 games (since no team can truly be eliminated from playoff contention before then) and unless one full day of games has passed (to save on performance - no information is lost by waiting until the end of a calendar day before reseeding and seeing if a team has been eliminated).

At that point, I seed teams. My program loops through the teams and finds the team with the Highest Win/Loss ratio, puts it in another list, and then repeats. There is a special tiebreaker function for ties, which checks the season series. To make finding the season series easier, I made a 30x30 matrix where each team has a number from 1 - 30. If team a defeats team b, then matrix(index(a), index(b)) is incremented by 1, and if team b defeats team a, then matrix(index(b), index(a)) is incremented by 1. Finding the winner of the season series is easy - find whether matrix(a, b) or matrix(b, a) is greater will tell you whether team a or team b won.

I then see which teams are eliminated from contention. My algorithm is as follows: for each team with a seed below the 8th seed, I go through the rest of the season and try to make the best possible outcome for them by using the following rules:
	1) The team I am simulating for wins every game they play
	2) If both teams have a higher seed than my team, the lower seed loses to give my team a 	better chance to catch up. Otherwise
	3) The lower seed wins.


Simply assuming that the 8th seed will lose all of their games and that my team can win all of my games does not account for the case in which teams seeded above me also competing for a playoff spot play the 8th seed as well - a loss for one team must be a win for another team. 

I intended to set the ‘Date Elim’ column in my standings data frame equal to the date that a team got eliminated, and then never touch it again if it had a value; after the last game, any teams without a value in that column would be assigned the value ‘playoffs’. Getting a spreadsheet with the answers would be a simple call to the pandas function to_csv using my standings CSV.


