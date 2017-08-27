import pandas as pd
import numpy as np
from helpers import NewTeam, StandingsUpdate

#Here we make the object that will store the information for each team



#First, read in info about Regular Season and Divisions/Conferences.
#'df' is short for DataFrame, which is pretty much a table. 
dfRegSeason = pd.read_csv('RegularSeason.csv', encoding = 'ISO-8859-1')
dfDivisionConfInfo = pd.read_csv('DivisionInfo.csv', encoding = 'ISO-8859-1')

#Now we track games through the regular season with a dataframe for the standings 
#that we will update after each game
dfStandings = pd.DataFrame([], columns = ['Team Name', 'Wins', 'Losses', 'Conference', 'Division', 'Conference Leader', 'Date Eliminated']) 

TeamsinList = [] #Just an easy way to keep track of teams I have in the system

for game in range (0, 1):
#for game in range(len(dfRegSeason)):

	#Giving current game data names that are easier to read
	HomeTeam = dfRegSeason['Home Team'][game]
	AwayTeam = dfRegSeason['Away Team'][game]
	WinningTeam = dfRegSeason['Winner'][game]
	Date = dfRegSeason['Date'][game]

	HomeTeamConf = dfDivisionConfInfo.query('Team_Name == @HomeTeam')['Conference_id']
	AwayTeamConf = dfDivisionConfInfo.query('Team_Name == @AwayTeam')['Conference_id']
	HomeTeamDiv = dfDivisionConfInfo.query('Team_Name == @HomeTeam')['Division_id']
	AwayTeamDiv = dfDivisionConfInfo.query('Team_Name == @AwayTeam')['Division_id']

	print('Home ' + str(HomeTeam) + ' Away ' + str(AwayTeam) + ' Winner ' + str(WinningTeam))
	
	#print(dfRegSeason['Home Team'][game])
	
	print(dfStandings['Team Name'])

	if(HomeTeam not in dfStandings['Team Name']): #If this team hasn't been added yet
		dfStandings.append(NewTeam(HomeTeam, dfDivisionConfInfo)()
		TeamsinList.append(HomeTeam)
		print(str(HomeTeam) + ' added successfully')

	if AwayTeam not in dfStandings['Team Name']:
		dfStandings.append([AwayTeam, 0, 0, AwayTeamConf, AwayTeamDiv, False, 0])
		TeamsinList.append(AwayTeam)
		print(str(AwayTeam) + ' added successfully')

	dfStandings.to_csv('NBATest.csv')

	print(TeamsinList)
	if WinningTeam == 'Home': #If winner of the currentgame is the Home team, then we report the Home team as the winner
		StandingsUpdate(dfStandings, Date, HomeTeam, AwayTeam, dfRegSeason)

	else: #If winner of the currentgame is the Away team, then we report the away team as the winner
		StandingsUpdate(dfStandings, Date, AwayTeam, HomeTeam)

