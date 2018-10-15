# -*- coding: utf-8 -*-
if 0:
    from scripts.lib.tips.baseapp import KBEngine
    from scripts.lib.tips.KBEDebug import *
    from common.ReloadSystem import *
else:
    import KBEngine
    from KBEDebug import *
    from ReloadSystem import *

class BattleField(KBEngine.Entity, Reload):
    def __init__(self):
        KBEngine.Entity.__init__(self)
        Reload.__init__(self)
        DEBUG_MSG("BattleField[%i] __init__" % (self.id))
        #KBEngine.createEntityAnywhere("CardPool")
        self.cellData["playerIDListC"] = self.playerIDList
        self.createCellEntityInNewSpace(None)


    def onTimer(self, id, userArg):
        """
        KBEngine method.
        使用addTimer后， 当时间到达则该接口被调用
        @param id		: addTimer 的返回值ID
        @param userArg	: addTimer 最后一个参数所给入的数据
        """
        DEBUG_MSG(id, userArg)

    def onDestroy(self):
        DEBUG_MSG("BattleField[%i].onDestroy." % self.id)

    def onGetCell( self ):
        DEBUG_MSG("BattleField[%i].onGetCell." % self.id)
        KBEngine.globalData["Halls"].onBattleFieldReady(self)

    def onEnterBattleField(self, _avatar):
        DEBUG_MSG("BattleField[%i].onEnterBattleField. _avatar[%s]" % (self.id, _avatar))

    def onLeaveBattleField(self, _avatar):
        DEBUG_MSG("BattleField[%i].onLeaveBattleField. _avatar[%s]" % (self.id, _avatar))

    def getCell(self):
        DEBUG_MSG("BattleField[%i].getCell." % (self.id))
        return self.cell

    def onLoseCell(self):
        DEBUG_MSG("BattleField[%i].onLoseCell." % (self.id))
        KBEngine.globalData["Halls"].onBattleFieldEnd(self)
        self.destroy()