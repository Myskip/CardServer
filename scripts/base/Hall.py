# -*- coding: utf-8 -*-
if 0:
    from scripts.lib.tips.baseapp import KBEngine
    from scripts.lib.tips.KBEDebug import *
    from common.ReloadSystem import *
else:
    import KBEngine
    from KBEDebug import *
    from ReloadSystem import *

class Hall(KBEngine.Entity, Reload):
    def __init__(self):
        KBEngine.Entity.__init__(self)
        Reload.__init__(self)

        self.playerPool = {}
        self.battleFields = {}
        KBEngine.globalData["Halls"] = self
        self.addTimer(5, 0.5, 0)


    def onTimer(self, id, userArg):
        """
        KBEngine method.
        使用addTimer后， 当时间到达则该接口被调用
        @param id		: addTimer 的返回值ID
        @param userArg	: addTimer 最后一个参数所给入的数据
        """
        self.doMatch()

    def onDestroy(self):
        DEBUG_MSG("Hall[%i].onDestroy." % self.id)

    def reqMatch(self, avatarID):
        #record avatar in playPool
        DEBUG_MSG("avatar[%i].reqMatch." % avatarID)
        self.playerPool[avatarID] = KBEngine.entities.get(avatarID)

    def doMatch(self):
        if (len(self.playerPool) >= 4):
            player1ID = self.playerPool.popitem()[0]
            player2ID = self.playerPool.popitem()[0]
            player3ID = self.playerPool.popitem()[0]
            player4ID = self.playerPool.popitem()[0]

            params = {
                "playerIDList": [player1ID, player2ID, player3ID, player4ID]
            }

            KBEngine.createEntityAnywhere("BattleField", params)
        else:
            pass

    def onBattleFieldReady(self, _battleField):
        DEBUG_MSG("Hall[%i] onBattleFieldReady, battleFieldID[%i]." % (self.id, _battleField.id))
        self.battleFields[_battleField.id] = _battleField
        for playerID in _battleField.playerIDList:
            KBEngine.entities.get(playerID).enterBattleField(_battleField)

    def onBattleFieldEnd(self, _battleField):
        DEBUG_MSG("Hall[%i] onBattleFieldEnd, battleFieldID[%i]." % (self.id, _battleField.id))
        self.battleFields.pop(_battleField.id)
        for playerID in _battleField.playerIDList:
            avatar = KBEngine.entities.get(playerID)
            if avatar is not None:
                avatar.onBattleFieldEnd(_battleField)
