from hlt import *
from networking import *
from UntidyLogicHaha2 import UntidyLogicHaha2

myID, gameMap = getInit()
sendInit("OldBot")
bot = UntidyLogicHaha2(myID, gameMap)

while True:
	#numberOfSquares = len(myShit)
	moves = []
	gameMap = getFrame()
	myShit = bot.myShit(gameMap)
	productionRate=0
	
	if myShit < 10:
		productionRate = 8
	elif myShit < 30:
		productionRate = 6
	else:
		productionRate = 4
		
	for y in range(gameMap.height):
		for x in range(gameMap.width):
			location = Location(x, y)
			if gameMap.getSite(location).owner == myID:
				if gameMap.getSite(location).strength<gameMap.getSite(location).production*productionRate:
					moves.append(Move(location, STILL))				
				else:
					direction = bot.getClosestFreeEdge(location, gameMap)
					moves.append(Move(location, direction))
	sendFrame(moves)
