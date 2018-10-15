# -*- coding: utf-8 -*-
if 0:
    from scripts.lib.tips.cellapp import KBEngine
    from scripts.lib.tips.KBEDebug import *
    from common.ReloadSystem import *
else:
    import KBEngine
    from KBEDebug import *
    from ReloadSystem import *

class Avatar(KBEngine.Entity, Reload):

    def __init__(self):
        #self.controlledBy
        KBEngine.Entity.__init__(self)
        Reload.__init__(self)
        self.enterBattleField()
        self.cardsInHnad = []

    def enterBattleField(self):
        self._battleField = KBEngine.entities.get(self.battleFieldEid)
        self._battleField.enterBattleField(self)

    def reqEndTurn(self):
        DEBUG_MSG("Avatar[%i] reqEndTurn." % (self.id))
        self._battleField.endTurn()

    def onEnteredView( self, entity):
        DEBUG_MSG("Avatar[%i] onEnteredView entity[%i] name:[%s]." % (self.id, entity.id, entity.className))

    def drawCard(self, callerEntityID):
        DEBUG_MSG("Avatar[%i] drawCard callerEntityID[%i]." % (self.id, callerEntityID))
        cardEntity = self._battleField.cardPool.drawCard(self)
        self.cardsInHnad.append(cardEntity)

    def onDestroy(self):
        DEBUG_MSG("Avatar.cell[%i].onDestroy." % self.id)
        self._battleField.leaveBattleField(self)
        for card in self.cardsInHnad:
            card.destroy()

    def test(self):
        DEBUG_MSG("Avatar[%i] test." % self.id)