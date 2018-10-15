# -*- coding: utf-8 -*-
if 0:
    from scripts.lib.tips.cellapp import KBEngine
    from scripts.lib.tips.KBEDebug import *
    from scripts.server_common.ServerDefine import *
    from common.ReloadSystem import *
else:
    import KBEngine
    from KBEDebug import *
    import random
    from ServerDefine import *
    from ReloadSystem import *

class BattleField(KBEngine.Entity, Reload):

    def __init__(self):
        DEBUG_MSG("BattleField[%i] __init__[%i]." % (self.id, self.spaceID))
        KBEngine.Entity.__init__(self)
        Reload.__init__(self)
        self._avatarList = []
        self.cardPool = None

        self._readyClientNum = 0

    def onDestroy( self ):
        self.cardPool.destroy()

    def onTimer(self, timerHandle, userData ):
        pass

    def enterBattleField(self, _avatar):
        self._avatarList.append(_avatar)
        if len(self._avatarList) == 4:

            #init battlefield setttings
            self.initBattleField()

            #notify client battlefield ready
            self.battleFieldLogicStart()

    def leaveBattleField(self, _avatar):
        self._avatarList.remove(_avatar)
        if len(self._avatarList) == 0:
            self.destroy()

    def initBattleField(self):
        #create cardpool
        params = {
            "battleFieldEid": self.id
        }
        self.cardPool = KBEngine.createEntity("CardPool", self.spaceID, CARD_POOL_POSITION, self.direction, params)

        # set tableID for each player, abstract for each player get a random table position
        while(len(self._avatarList) > 0):
            _avatar = random.choice(self._avatarList)
            self.turnManager.playersInTurn.append(_avatar)
            _avatar.tableID = self.turnManager.playersInTurn.index(_avatar)
            _avatar.position = PLAYER_TABLE_POSITIONS[_avatar.tableID]
            self._avatarList.remove(_avatar)
        self._avatarList = self.turnManager.playersInTurn

    def battleFieldLogicStart(self):
        DEBUG_MSG("battleField[%i] Logic Start." % (self.id))

        for player in self._avatarList:
            player.client.onBattleFieldStart()

    def onClientBattleFieldReady(self,callerID):
        DEBUG_MSG("battleField[%i] onClientBattleFieldReady, callerID[%s]." % (self.id, callerID))
        self._readyClientNum += 1
        # start game logic
        if self._readyClientNum >= 4:
            self.turnManager.begin()

    def endTurn(self, callerID):
        DEBUG_MSG("battleField[%i] endTurn, callerID[%s]." % (self.id, callerID))
        self.turnManager.endTurn()