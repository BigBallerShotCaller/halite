from hlt import *
from networking import *
from UntidyLogicHaha4 import UntidyLogicHaha4
import timeit

myID, gameMap = getInit()
sendInit("BIGBALLERSHOTCALLERHAHA")
bot = UntidyLogicHaha4(myID, gameMap)

while True:
	start_time = timeit.default_timer()
	maxTime = .95
	#numberOfSquares = len(myShit)
	moves = []
	gameMap = getFrame()
	#myShit = bot.myShit(gameMap)
	productionRate = 5
	goQuick=False #if time is nearly up	
	numSquares = 0
	
	for y in range(gameMap.height):
		for x in range(gameMap.width):
			if (x + y) % 50 == 0:
				if timeit.default_timer() - start_time > maxTime:
					goQuick=True
			location = Location(x, y)
			if goQuick != True:
				site = gameMap.getSite(location)
				if site.owner == myID:
					numSquares+=1
					if numSquares > (3*gameMap.height*gameMap.width)/4 and numSquares > 2000:
						productionRate = numSquares/10
					else:
						productionRate = 5
					reachedProductionRate = site.strength>=site.production*productionRate
					direction = bot.getClosestFreeEdge(location, gameMap, reachedProductionRate)
					moves.append(Move(location, direction))
			else: #times up lets make everything stay still
				moves.append(Move(location, STILL))
				
	sendFrame(moves)
