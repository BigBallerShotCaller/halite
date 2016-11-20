import numpy as np
from hlt import Move, WEST, EAST, NORTH, SOUTH, STILL, Location

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
		return (gameMap.getSite(myLocation).strength > gameMap.getSite(myLocation).prospectiveLocation)
				
	def getClosestFreeEdge(self, location, gameMap):
		gm = gameMap
		x = location.x
		y = location.y
		xDistance = 1
		yDistance = 1
		yFound=False
		xFound=False
		xDirection = STILL
		yDirection = STILL
		
		eastLocation = self.getNextXLocation(xDistance, location)
		westLocation = self.getNextXLocation(-xDistance, location)
		northLocation = self.getNextYLocation(yDistance, location)
		southLocation = self.getNextYLocation(-yDistance, location)
		
		#if gm.getSite(eastLocation).owner != self.myID:
		#elif gm.getSite(westLocation).owner != self.myID:
		#elif gm.getSite(northLocation).owner != self.myID:
		#elif gm.getSite(southLocation).owner != self.myID:
		
		while (xDistance < (self.gameMap.width/2)) and (xFound == False):
			xDistance += 1
			eastLocation = self.getNextXLocation(xDistance, location)
			westLocation = self.getNextXLocation(-xDistance, location)
			
			if gm.getSite(eastLocation).owner != self.myID:
				xDirection = EAST
				xFound = True
			elif gm.getSite(westLocation).owner != self.myID:
				xDirection = WEST
				xFound = True
		while (yDistance < (self.gameMap.height/2)) and (yFound == False):
			yDistance += 1
			northLocation = self.getNextYLocation(yDistance, location)
			southLocation = self.getNextYLocation(-yDistance, location)
			if gm.getSite(northLocation).owner != self.myID:
				yDirection = SOUTH
				yFound = True
			elif gm.getSite(southLocation).owner != self.myID:
				yDirection = NORTH
				yFound = True
				
		if (xDistance <= yDistance):
			return xDirection
		else:
			return yDirection
			
		

	
