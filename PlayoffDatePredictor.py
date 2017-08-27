import pandas as pd
import numpy as np
from helpers import AddTeams, StandingsUpdate

#Here we make the object that will store the information for each team



#First, read in info about Regular Season and Divisions/Conferences.
#'df' is short for DataFrame, which is pretty much a table. 
dfRegSeason = pd.read_csv('RegularSeason.csv', encoding = 'ISO-8859-1')
dfDivisionConfInfo = pd.read_csv('DivisionInfo.csv', encoding = 'ISO-8859-1')

#Now we track games through the regular season with a dataframe for the standings 
#that we will update after each game - we start it by taking division/conference info
#and adding some other columns that we will want to track like Wins, Losses, etc.
dfStandings	= AddTeams(dfDivisionConfInfo)


for game in range (0, 1):
#for game in range(len(dfRegSeason)):

	#Giving current game data names that are easier to read
	HomeTeam = dfRegSeason['Home Team'][game]
	AwayTeam = dfRegSeason['Away Team'][game]
	WinningTeam = dfRegSeason['Winner'][game]
	Date = dfRegSeason['Date'][game]

	print('Home ' + str(HomeTeam) + ' Away ' + str(AwayTeam) + ' Winner ' + str(WinningTeam))
	
	#print(dfRegSeason['Home Team'][game])

	if WinningTeam == 'Home': #If winner of the currentgame is the Home team, then we report the Home team as the winner
		StandingsUpdate(dfStandings, Date, HomeTeam, AwayTeam, dfRegSeason)

	else: #If winner of the currentgame is the Away team, then we report the away team as the winner
		StandingsUpdate(dfStandings, Date, AwayTeam, HomeTeam, dfRegSeason)

