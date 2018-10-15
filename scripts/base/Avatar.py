# -*- coding: utf-8 -*-
if 0:
    from scripts.lib.tips.baseapp import KBEngine
    from scripts.lib.tips.KBEDebug import *
    from common.ReloadSystem import *
else:
    import KBEngine
    from KBEDebug import *
    from ReloadSystem import *


class Avatar(KBEngine.Proxy, Reload):
    def __init__(self):
        KBEngine.Proxy.__init__(self)
        Reload.__init__(self)
        self.cellData["nameC"] = self.name

    def onTimer(self, id, userArg):
        """
        KBEngine method.
        使用addTimer后， 当时间到达则该接口被调用
        @param id		: addTimer 的返回值ID
        @param userArg	: addTimer 最后一个参数所给入的数据
        """
        DEBUG_MSG(id, userArg)

    def onClientEnabled(self):
        """
        KBEngine method.
        该entity被正式激活为可使用， 此时entity已经建立了client对应实体， 可以在此创建它的
        cell部分。
        """
        INFO_MSG("Avatar[%i] entities enable. entityCall:%s" % (self.id, self.client))
        # Todo:init hero list here.Hero list should be a base_client property.

    def onLogOnAttempt(self, ip, port, password):
        """
        KBEngine method.
        客户端登陆失败时会回调到这里
        """
        INFO_MSG(ip, port, password)
        return KBEngine.LOG_ON_ACCEPT

    def onClientDeath(self):
        """
        KBEngine method.
        客户端对应实体已经销毁
        """
        DEBUG_MSG("Avatar[%i].onClientDeath, self.cell:%s." % (self.id, self.cell))

        if self.cell is not None:
            DEBUG_MSG("Avatar[%i].onClientDeath, self.cell is not None.")
            self.destroyCellEntity()
            return

        if not self.isDestroyed:
            self.destroy()

    def onDestroy(self):
        DEBUG_MSG("Avatar[%i].onDestroy." % self.id)

    def onLoseCell(self):
        DEBUG_MSG("Avatar[%i].onLoseCell." % self.id)
        self.destroy()

    def setName(self, _name):
        self.name = _name

    def reqMatch(self, heroID):
        self._heroID = heroID
        KBEngine.globalData["Halls"].reqMatch(self.id)

    def enterBattleField(self, _battleField):
        DEBUG_MSG("Avatar[%i].enterBattleField. battleFieldID[%i]." % (self.id, _battleField.id))
        self.battleField = _battleField
        self.cellData["battleFieldEid"] = _battleField.id
        self.createCellEntity(_battleField.getCell())
        self.battleField.onEnterBattleField(self)

    def leaveBattleField(self):
        DEBUG_MSG("Avatar[%i].leaveBattleField. battleFieldID[%i]." % (self.id, self.battleField.id))

        self.cellData["battleFieldEid"] = 0

        if self.cell is not None:
            self.destroyCellEntity()
        if self.battleField is not None:
            self.battleField.onLeaveBattleField(self)
            self.battleField = None

    def onBattleFieldEnd(self, _battleField):
        DEBUG_MSG("Avatar[%i].onBattleFieldEnd. battleFieldID[%i]." % (self.id, _battleField.id))
        if _battleField.id == self.battleField.id:
            self.battleField = None