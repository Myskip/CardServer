# -*- coding: utf-8 -*-
if 0:
    from scripts.lib.tips.KBEDebug import *
    from scripts.lib.tips.bots import KBEngine
else:
    import KBEngine
    from KBEDebug import *


class Avatar(KBEngine.Entity):
    def __init__(self):
        KBEngine.Entity.__init__(self)
        self.beginMatch()

    def onBattleFieldStart(self):
        DEBUG_MSG("Avatar[%i].onBattleFieldStart." % (self.id))

    def beginMatch(self):
        self.base.reqMatch(0)