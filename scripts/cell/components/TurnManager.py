# -*- coding: utf-8 -*-
if 0:
    from scripts.lib.tips.cellapp import KBEngine
    from scripts.common.KBEDebug import *
    from scripts.server_common.ServerDefine import *
else:
    import KBEngine
    from KBEDebug import *
    import time
    import random
    from ServerDefine import *

class TurnManager(KBEngine.EntityComponent):

    def __init__(self):
        self._loopIndex = 1
        self.newTurn = False
        self._hasBegan = False
        self.playersInTurn = []
        self.currentPlayerID = -1
        self._turnManagerTimerID = self.addTimer(0, 0.1, TIMER_TYPE_TURN_MANAGER)

        KBEngine.EntityComponent.__init__(self)

    def begin(self):
        # initial hand draw
        if (self.owner.cardPool is None):
            time.sleep(1)

        if (self.owner.cardPool is None):
            ERROR_MSG("TurnManager[%i] cardPool is None." % (self.id))
        else:
            for player in self.owner._avatarList:
                # every player draw 13 cards for initial
                self.owner.cardPool.initDraw(player, 13)
                self._hasBegan = True

            #choose a random player for start, mayebe has some mechanism someday.
            self.currentPlayerID = random.randint(0, 3)

            #start turn
            self.nextTurn()

    def onTurnStart(self):
        DEBUG_MSG("Turn[%i] onTurnStart.currentPlayerID[%i]" % (self.turnIndex, self.currentPlayerID))

        #player draw a card at turn start.
        self.owner.cardPool.drawCard(self.playersInTurn[self.currentPlayerID])

    def onTurnEnd(self):
        DEBUG_MSG("Turn[%i] onTurnEnd." % (self.turnIndex))

        #set current player to next
        self.currentPlayerID = (self.currentPlayerID + 1) % 4

    def endTurn(self):
        DEBUG_MSG("Turn[%i] endTurn." % (self.turnIndex))
        self.onTurnEnd()
        self.nextTurn()

    def nextTurn(self):
        self.turnIndex += 1
        self._loopIndex = 1 + int(self.turnIndex / 4)
        self.newTurn = True

    def onTimer(self, timerHandle, userData ):
        if (userData == TIMER_TYPE_TURN_MANAGER):
            if not self._hasBegan:
                return

            if (self.newTurn):
                self.newTurn = False
                self.onTurnStart()

    def onAttached(self, owner):
        INFO_MSG("TurnManager::onAttached(): owner=%i" % (owner.id))

    def onDetached(self, owner):
        INFO_MSG("TurnManager::onDetached(): owner=%i" % (owner.id))
        if (self._turnManagerTimerID > 0):
            self.delTimer(self._turnManagerTimerID)