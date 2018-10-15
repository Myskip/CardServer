# -*- coding: utf-8 -*-
if 0:
    from scripts.lib.tips.cellapp import KBEngine
    from scripts.lib.tips.KBEDebug import *
else:
    import KBEngine
    from KBEDebug import *


class Card(KBEngine.EntityComponent):

    def __init__(self):
        KBEngine.EntityComponent.__init__(self)
        pass

    def use(self, targetEid):
        pass

    def onAttached(self, owner):
        INFO_MSG("Card::onAttached(): owner=%i" % (owner.id))

    def onDetached(self, owner):
        INFO_MSG("Card::onDetached(): owner=%i" % (owner.id))