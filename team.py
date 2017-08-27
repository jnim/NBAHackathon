class Team:
	def __init__(self, name, wins, losses, division, conference, seed, eliminated):
		self.name = name
		self.wins = wins
		self.losses = losses
		self.division = division
		self.conference = conference
		self.seed = seed
		self.notinplayoffs = eliminated

	#I'm writing these as functions to make the code easier to read
	def loss(self): #If you lose, add one to the team's loss count
		self.losses = self.losses + 1


	def win(self): #If you win, add one to the team's win count
		self.wins = self.losses + 1