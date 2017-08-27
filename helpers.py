from team import Team
import pandas as pandas
import numpy as np

def NewTeam(TeamName, DivisionInfo):
	TeamConf = Division.query('Team_Name == @TeamName')['Conference_id']
	TeamDiv = Division.query('Team_Name == @TeamName')['Conference_id']
	#All we're doing is making a new instance of the team class - I made this class to make code easier to read
	HomeTeam, 0, 0, HomeTeamConf, HomeTeamDiv, False, 0
	return Team(TeamName, 0, 0, TeamDivision, TeamConference, 0, False)


def StandingsUpdate(TeamsInfo, DateofGame, TeamWon, TeamLost, RegSeasonSchedule):
	return 0
	

