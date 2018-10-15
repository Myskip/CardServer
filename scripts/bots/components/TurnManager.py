# -*- coding: utf-8 -*-
if 0:
    from scripts.lib.tips.KBEDebug import *
    from scripts.lib.tips.bots import KBEngine
else:
    import KBEngine
    from KBEDebug import *

class TurnManager(KBEngine.EntityComponent):
    def __init__(self):
        KBEngine.EntityComponent.__init__(self)

    def onAttached(self, owner):
        """
        """
        INFO_MSG("Card::onAttached(): owner=%i" % (owner.id))

    def onDetached(self, owner):
        """
        """
        INFO_MSG("Card::onDetached(): owner=%i" % (owner.id))