from hlt import *
from networking import *
from UntidyLogicHaha import UntidyLogicHaha

myID, gameMap = getInit()
sendInit("OldBot")
bot = UntidyLogicHaha(myID, gameMap)

while True:
	moves = []
	gameMap = getFrame()
	for y in range(gameMap.height):
		for x in range(gameMap.width):
			location = Location(x, y)
			if gameMap.getSite(location).owner == myID:
				if gameMap.getSite(location).strength<50:
					moves.append(Move(location, STILL))				
				else:
					direction = bot.getClosestFreeEdge(location, gameMap)
					moves.append(Move(location, direction))
	sendFrame(moves)
