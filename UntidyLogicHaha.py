import numpy as np
from hlt import Move, WEST, EAST, NORTH, SOUTH, STILL, Location

class EdgeWeight:
	def __init__(self, loc=0, weight=255):
		self.loc = loc
		self.weight = weight

class UntidyLogicHaha(object):

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
		return (gameMap.getSite(myLocation).strength > gameMap.getSite(prospectiveLocation).strength)
				
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
		eWeight = 0
		wWeight = 0
		nWeight = 0
		sWeight = 0
		
		eFound = False
		wFound = False
		nFound = False
		sFound = False
		
		distanceWeight = 500
		
		eastLocation = self.getNextXLocation(xDistance, location)
		westLocation = self.getNextXLocation(-xDistance, location)
		southLocation = self.getNextYLocation(yDistance, location)
		northLocation = self.getNextYLocation(-yDistance, location)
		
		
		if gm.getSite(eastLocation).owner != self.myID and self.canTake(gameMap, location, eastLocation):
				return EAST
		elif gm.getSite(westLocation).owner != self.myID and self.canTake(gameMap, location, westLocation):
				return WEST
		elif gm.getSite(southLocation).owner != self.myID and self.canTake(gameMap, location, southLocation):
				return SOUTH
		elif gm.getSite(northLocation).owner != self.myID and self.canTake(gameMap, location, northLocation):
				return NORTH			
				
		if sum([gm.getSite(eastLocation).owner != self.myID, gm.getSite(westLocation).owner != self.myID, gm.getSite(southLocation).owner != self.myID, gm.getSite(northLocation).owner != self.myID]) >= 3:
			return STILL
		
		eDistance = 0
		while True:
			eastLocation = self.getNextXLocation(eDistance, location)
			eWeight+=gm.getSite(eastLocation).strength #+ eDistance*distanceWeight
			if eDistance > (self.gameMap.width):
				eWeight = 5000000
				break
			elif gm.getSite(self.getNextXLocation(eDistance, location)).owner == self.myID:
				break
			eDistance += 1
			
		wDistance = 0
		while True:
			westLocation = self.getNextXLocation(-wDistance, location)
			wWeight+=gm.getSite(westLocation).strength #+ wDistance*distanceWeight
			if wDistance > (self.gameMap.width):
				wWeight = 5000000
				break
			elif gm.getSite(self.getNextXLocation(-wDistance, location)).owner == self.myID:
				break
			wDistance += 1
				
		if eDistance < wDistance:
			xDirection = EAST
			xWeight = eWeight
		else:
			xDirection = WEST
			xWeight = wWeight

		sDistance = 0
		while gm.getSite(self.getNextYLocation(sDistance, location)).owner == self.myID:	
			southLocation = self.getNextYLocation(sDistance, location)
			sWeight+=gm.getSite(southLocation).strength #+ sDistance*distanceWeight
			#if sDistance > (self.gameMap.height):
			#	sWeight = 5000000
			#	break
			sDistance += 1

		nDistance = -1
		while gm.getSite(self.getNextYLocation(-nDistance, location)).owner == self.myID:
			nDistance += 1 
			northLocation = self.getNextYLocation(-nDistance, location)
			nWeight+=gm.getSite(northLocation).strength
			#+ nDistance*distanceWeight
			#if nDistance > (self.gameMap.height):
			#	nWeight = 5000000
			#	break
				
		# if sWeight < nWeight:
			# yDirection = SOUTH
			# yWeight = sWeight
		# elif nWeight < sWeight:
			# yDirection = NORTH
			# yWeight = nWeight
		# else:
			# return STILL
			
		# if xWeight < yWeight:
			# return xDirection
		# elif yWeight < xWeight:
			# return yDirection
			
		if (eWeight <= wWeight) and (eWeight<= sWeight) and (eWeight <= nWeight):
			return EAST
		elif (wWeight <= nWeight) and (wWeight<= sWeight):
			return WEST
		elif (nWeight <= sWeight):
			return NORTH
		else:
			return SOUTH
			
			
		return STILL
			
	def getDirections(self, gameMap):
		directions = []
		return directions

	
