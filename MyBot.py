from hlt import *
from networking import *
from UntidyLogicHaha import UntidyLogicHaha
import timeit

myID, gameMap = getInit()
sendInit("BIGBALLERSHOTCALLERHAHA")
bot = UntidyLogicHaha(myID, gameMap)

while True:
	start_time = timeit.default_timer()
	maxTime = .95
	#numberOfSquares = len(myShit)
	moves = []
	gameMap = getFrame()
	myShit = bot.myShit(gameMap)
	productionRate = 4
	goQuick=False #if time is nearly up	
	
	for y in range(gameMap.height):
		for x in range(gameMap.width):
			if (x + y) % 80 == 0:
				if timeit.default_timer() - start_time > maxTime:
					goQuick=True
			location = Location(x, y)
			if goQuick != True:
				if gameMap.getSite(location).owner == myID:
					if gameMap.getSite(location).strength<gameMap.getSite(location).production*productionRate:
						moves.append(Move(location, STILL))				
					else:
						direction = bot.getClosestFreeEdge(location, gameMap)
						moves.append(Move(location, direction))
			else: #times up lets make everything stay still
				moves.append(Move(location, STILL))
				
	sendFrame(moves)
