import numpy as np
from hlt import Move, WEST, EAST, NORTH, SOUTH, STILL, Location

class EdgeWeight:
	def __init__(self, loc=0, weight=255):
		self.loc = loc
		self.weight = weight

class UntidyLogicHaha3(object):

	def __init__(self, myID, gameMap):
		self.myID = myID
		self.gameMap = gameMap
	
	#def move(self):
	
	
	def myShit(self, gameMap):
		i=0	
		myShit=[]
		for y in range(gameMap.height):
			for x in range(gameMap.width):
				location = Location(x, y)
				if gameMap.getSite(location).owner == self.myID:
					myShit.append(Location(x,y))
					i+=1
		return i

	def getNextXLocation(self, increment, location):
		newX = location.x + increment
		if newX >= self.gameMap.width:
			return Location(0, location.y)
		elif newX < 0:
			return Location(self.gameMap.width-1, location.y)
		return Location(newX, location.y)
	
	def getNextYLocation(self, increment, location):
		newY = location.y + increment
		if newY >= self.gameMap.height:
			return Location(location.x, 0)
		elif newY < 0:
			return Location(location.x, self.gameMap.height-1)
		return Location(location.x, newY)
		
	def canTake(self, gameMap, myLocation, prospectiveLocation):
		return (gameMap.getSite(myLocation).strength > prospectiveLocation.strength)
				
	def getClosestFreeEdge(self, location, gameMap):
		gm = gameMap
		x = location.x
		y = location.y
		xDistance = 1
		yDistance = 1
		yFound=0
		xFound=0
		xDirection = STILL
		yDirection = STILL
		edgeWeights = []
		eWeight = 500000
		wWeight = 500000
		nWeight = 500000
		sWeight = 500000
		
		eastLocation = self.getNextXLocation(xDistance, location)
		westLocation = self.getNextXLocation(-xDistance, location)
		northLocation = self.getNextYLocation(yDistance, location)
		southLocation = self.getNextYLocation(-yDistance, location)
		
		if gm.getSite(eastLocation).owner != self.myID and self.canTake(gameMap, location, gm.getSite(eastLocation)):
				return EAST
			#else:
			#	return STILL
		elif gm.getSite(westLocation).owner != self.myID and self.canTake(gameMap, location, gm.getSite(westLocation)):
				return WEST
			#else:
			#	return STILL
		elif gm.getSite(northLocation).owner != self.myID and self.canTake(gameMap, location, gm.getSite(northLocation)):
				return SOUTH
			#else:
			#	return STILL
		elif gm.getSite(southLocation).owner != self.myID and self.canTake(gameMap, location, gm.getSite(southLocation)):
				return NORTH
			#else:
			#	return STILL
		
		while (xDistance < (self.gameMap.width)) and (xFound < 2):
			xDistance += 1
			eastLocation = self.getNextXLocation(xDistance, location)
			westLocation = self.getNextXLocation(-xDistance, location)
			
			if gm.getSite(eastLocation).owner != self.myID:
				edgeWeights
				xDirection = EAST
				eWeight=gm.getSite(eastLocation).strength / (gm.getSite(eastLocation).production+1) + xDistance*20
				xFound += 1
			elif gm.getSite(westLocation).owner != self.myID:
				xDirection = WEST
				wWeight=gm.getSite(westLocation).strength / (gm.getSite(westLocation).production+1) + xDistance*20
				xFound += 1
		while (yDistance < (self.gameMap.height)) and (yFound < 2):
			yDistance += 1
			northLocation = self.getNextYLocation(yDistance, location)
			southLocation = self.getNextYLocation(-yDistance, location)
			if gm.getSite(northLocation).owner != self.myID:
				yDirection = SOUTH
				sWeight=gm.getSite(northLocation).strength / (gm.getSite(northLocation).production+1) + yDistance*20
				yFound += 1
			elif gm.getSite(southLocation).owner != self.myID:
				yDirection = NORTH
				nWeight=gm.getSite(southLocation).strength / (gm.getSite(southLocation).production+1) + yDistance*20
				yFound += 1
				
		xDistance = 1
		yDistance = 1
		eastLocation = self.getNextXLocation(xDistance, location)
		westLocation = self.getNextXLocation(-xDistance, location)
		northLocation = self.getNextYLocation(yDistance, location)
		southLocation = self.getNextYLocation(-yDistance, location)
				
		if (eWeight <= wWeight) and (eWeight<= sWeight) and (eWeight <= nWeight):
			if gm.getSite(eastLocation).owner == self.myID:
				return EAST
			elif self.canTake(gameMap, location, gm.getSite(eastLocation)) == False:
				return STILL
		elif (wWeight <= nWeight) and (wWeight<= sWeight):
			if gm.getSite(westLocation).owner == self.myID:
				return WEST
			elif self.canTake(gameMap, location, gm.getSite(westLocation)) == False:
				return STILL
		elif (nWeight <= sWeight):
			if gm.getSite(southLocation).owner == self.myID:
				return NORTH
			elif self.canTake(gameMap, location, gm.getSite(southLocation)) == False:
				return STILL
		else:
			if gm.getSite(northLocation).owner == self.myID:
				return SOUTH
			elif self.canTake(gameMap, location, gm.getSite(northLocation)) == False:
				return STILL
			
			
	def getDirections(self, gameMap):
		directions = []
		return directions

	
