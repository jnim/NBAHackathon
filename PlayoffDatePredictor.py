import pandas as pd
import numpy as np
from helpers import AddTeams, UpdateRecord, Seed, UpdateTiebreak, ElimFromPlayoffs, HasPlayed42Games

#Here we make the object that will store the information for each team



#First, read in info about Regular Season and Divisions/Conferences.
#'df' is short for DataFrame, which is pretty much a table. 
dfRegSeason = pd.read_csv('RegularSeason.csv', encoding = 'ISO-8859-1')
dfDivisionConfInfo = pd.read_csv('DivisionInfo.csv', encoding = 'ISO-8859-1')
#print(dfRegSeason)

#Now we track games through the regular season with a dataframe for the standings 
#that we will update after each game - we start it by taking division/conference info
#and adding some other columns that we will want to track like Wins, Losses, etc.
dfStandings	= AddTeams(dfDivisionConfInfo)

print(dfStandings)
#We also make a 30x30 array that has the tiebreak results of each team. Each team
#has an index value assigned below. Say a team with index i beats a team with index
#j - then the matrix value at array(i, j) will be incremented by 1. If array(i, j)>
#array(j, i), then team i won the season series. Otherwise, team j won. 

tiebreak = np.zeros((31, 31))
TeamIndex = {'Boston Celtics': 1, 'Brooklyn Nets': 2, 'New York Knicks': 3, 'Philadelphia 76ers': 4, 'Toronto Raptors': 5, 'Chicago Bulls': 6, 'Cleveland Cavaliers': 7, 'Detroit Pistons': 8, 'Indiana Pacers': 9, 'Milwaukee Bucks': 10, 'Atlanta Hawks': 11, 'Charlotte Hornets': 12, 'Miami Heat': 13, 'Orlando Magic': 14, 'Washington Wizards': 15, 'Denver Nuggets': 16, 'Minnesota Timberwolves': 17, 'Oklahoma City Thunder': 18, 'Portland Trail Blazers': 19, 'Utah Jazz': 20, 'Golden State Warriors': 21, 'LA Clippers': 22, 'Los Angeles Lakers': 23, 'Phoenix Suns': 24, 'Sacramento Kings': 25, 'Dallas Mavericks': 26, 'Houston Rockets': 27, 'Memphis Grizzlies': 28, 'New Orleans Pelicans': 29, 'San Antonio Spurs': 30}

bool = False
for game in range(0, 576):
for game in range(len(dfRegSeason)):

	#Giving current game data names that are easier to read
	HomeTeam = dfRegSeason['Home Team'][game]
	AwayTeam = dfRegSeason['Away Team'][game]
	WinningTeam = dfRegSeason['Winner'][game]
	Date = dfRegSeason['Date'][game]
	TeamsCanBeEliminated = HasPlayed42Games(dfStandings) #Unless a team has played 42 games, no team can be eliminated
	

	if not bool and TeamsCanBeEliminated:
		print('game no: ' + str(game) + '\n')
		bool = True

	try: 
		NextGameDate = dfRegSeason['Date'][game+1]
	except(KeyError):
		NextGameDate = 0 #We are on the last game, and we want to re-seed. Setting it to 0 ensures re-seeding

	#print('Home ' + str(HomeTeam) + ' Away ' + str(AwayTeam) + ' Winner ' + str(WinningTeam))
	
	#print(dfRegSeason['Home Team'][game])

	if WinningTeam == 'Home': #If winner of the current game is the Home team, then we report the Home team as the winner
		tiebreak = UpdateTiebreak(tiebreak, HomeTeam, AwayTeam) #The season series is updated
		dfStandings = UpdateRecord(dfStandings, HomeTeam, AwayTeam)

		if (NextGameDate != Date and TeamsCanBeEliminated): #Only calculate standings after a full day of games - improves performance
			#Neither of the lines below run unless a team has played 42 games - before that, no team can be eliminated from playoff contention
			dfStandings = Seed(dfStandings, Date, dfRegSeason, tiebreak, TeamIndex, game) 
			dfStandings = ElimFromPlayoffs(dfStandings, dfRegSeason, tiebreak, TeamIndex, game)
	
	else: #If winner of the currentgame is the Away team, then we report the away team as the winner
		tiebreak = UpdateTiebreak(tiebreak, AwayTeam, HomeTeam) #Season series is updated
		dfStandings = UpdateRecord(dfStandings, AwayTeam, HomeTeam)

		if (NextGameDate != Date and TeamsCanBeEliminated): #Only calculate standings after a full day of games - improves performance
			NewSeeding(dfStandings, Date, dfRegSeason, tiebreak, TeamIndex, game)



