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

	#The while loops below don't work, but the inner one loops through the list, 
	#iterating through the teams, and setting 'highest' equal to the team with the 
	#highest win ratio. If there is a tie, that is handled by the tiebreaker function.
	#Once it has gone through all the teams, the team with the Highest win ratio is 
	#filtered out and added to the 'Sorted' dataframe. The inner loop then repeats
	#for the rest of the teams. This occurs until the length of Sorted is 15 - which means
	#all fifteen teams from the conference have been sorted.

	while(len(Sorted)<15): 
		counter = 0
		HighestRec = 0
		while(counter<len(dfWest)): #We go through the teams, find highest seed, then take it out and repeat
			CurrentTeam = dfWest.iloc[[counter]]
			CurrentRec = float(CurrentTeam['W/L'])

			if HighestRec == 0: #if this is the first team we are looking at
				Highest = CurrentTeam
				HighestRec = float(Highest['W/L'])
			else:

				if CurrentRec > HighestRec:
					Highest = CurrentTeam
					HighestRec = float(Highest['W/L'])
				
				elif CurrentRec == HighestRec:
					Highest = Tiebreaker(Highest, CurrentTeam, tiebreak, tiebreakIndex)
					HighestRec = float(Highest['W/L'])
				
			counter += 1
			print('counter updated')
			print(HighestRec)

		dfWest = dfWest[~dfWest['Team_Name'].isin(Highest['Team_Name'])]
		Sorted.append(Highest)
		
		#Repeat above loop for East Teams
	
	Sorted = pd.DataFrame()

	dfNewStandings = pd.DataFrame()


	return dfStandings

def Tiebreaker(Team1, Team2, arrTiebreak, tiebreakIndex):
	print('Team_Name')
	print('\n')
	
	if(arrTiebreak[tiebreakIndex[Team1['Team_Name']], tiebreakIndex[Team2['Team_Name']]] > arrTiebreak[tiebreakIndex[Team2], tiebreakIndex[Team1]]):
		return Team1 #If Team1 won the season series, they win the tiebreaker
	else:
		return Team2

		#I ran out of time before I coded the second layer of tiebreakers - doing it 
		#by Division and then record against one's own conference


def ElimFromPlayoffs(dfStandings, dfRegSeason, arrTiebreak, tiebreakIndex, game):
	#I ran out of time, so this is what I intended to do:
	#For each team below the 8th seed, I would go through the rest of the games
	#of the regular season and try and create an optimal scenario: the team I am 
	#simulating for wins every game, and for games with other teams, the lower seeded
	#team wins unless both teams have a higher seeded than my team, in which case the 
	#lower seeded team loses (to help my team catch up to them and take their spot)


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
