import pandas as pd
import numpy as np

def AddTeams(dfStandings):
	dfStandings['Wins'] = 0
	dfStandings['Losses'] = 0
	dfStandings['DivLeader'] = 0
	dfStandings['Seed'] = 0
	dfStandings['Date Elim'] = 0
	return dfStandings

def UpdateRecord(dfStandings, TeamWon, TeamLost):
	
	Won = dfStandings.query('Team_Name == @TeamWon')['Wins']
	dfStandings.loc[dfStandings['Team_Name'] == TeamWon, 'Wins'] = Won + 1
	
	#print(dfStandings.loc[dfStandings['Team_Name'] == TeamLost])
	Lost = dfStandings.query('Team_Name == @TeamLost')['Losses']
	dfStandings.loc[dfStandings['Team_Name'] == TeamLost, 'Losses'] = Lost + 1
	
	return dfStandings


def Seed(dfStandings, Date, dfRegSeason, tiebreak, tiebreakIndex, gameIndex):
	
	dfStandings['W/L'] = dfStandings['Wins']/(dfStandings['Wins'] + dfStandings['Losses'])
	ToBeSorted = dfStandings
	
	dfWest = dfStandings[dfStandings['Conference_id'] == 'West']
	dfWest = dfWest.reset_index(drop = True)

	dfEast = dfStandings[dfStandings['Conference_id'] == 'East']
	dfEast = dfEast.reset_index(drop = True)
	
	Sorted = pd.DataFrame()
	while(len(Sorted)<15): 
		counter = 0
		Highest = -1
		while(counter!=len(dfWest)): #We go through the teams, find highest seed, then take it out and repeat
			if Highest == -1: #If this is the first team we are examining
				#print(dfWest)
				Highest = dfWest[counter]

	Sorted = pd.DataFrame()

		dfNewStandings = pd.DataFrame()

	#for team in range(len(dfStandings) - 1):


	return dfStandings



def ElimFromPlayoffs(dfStandings, dfRegSeason, arrTiebreak, tiebreakIndex, game):

	return 0

def HasPlayed42Games(dfStandings):
	np.where(dfStandings['Wins'] + dfStandings['Losses'] >= 42, 1, 0)
	Ans = 1 in np.where(dfStandings['Wins'] + dfStandings['Losses'] >= 42, 1, 0) 
	return Ans

def UpdateTiebreak(arrTiebreak, TeamWon, TeamLost):
	TeamIndex = {'Boston Celtics': 1, 'Brooklyn Nets': 2, 'New York Knicks': 3, 'Philadelphia 76ers': 4, 'Toronto Raptors': 5, 'Chicago Bulls': 6, 'Cleveland Cavaliers': 7, 'Detroit Pistons': 8, 'Indiana Pacers': 9, 'Milwaukee Bucks': 10, 'Atlanta Hawks': 11, 'Charlotte Hornets': 12, 'Miami Heat': 13, 'Orlando Magic': 14, 'Washington Wizards': 15, 'Denver Nuggets': 16, 'Minnesota Timberwolves': 17, 'Oklahoma City Thunder': 18, 'Portland Trail Blazers': 19, 'Utah Jazz': 20, 'Golden State Warriors': 21, 'LA Clippers': 22, 'Los Angeles Lakers': 23, 'Phoenix Suns': 24, 'Sacramento Kings': 25, 'Dallas Mavericks': 26, 'Houston Rockets': 27, 'Memphis Grizzlies': 28, 'New Orleans Pelicans': 29, 'San Antonio Spurs': 30}
	old_val = arrTiebreak[TeamIndex[TeamWon], TeamIndex[TeamLost]]
	new_val = old_val + 1 #Update the season series
	arrTiebreak[TeamIndex[TeamWon], TeamIndex[TeamLost]] = new_val

	return arrTiebreak
