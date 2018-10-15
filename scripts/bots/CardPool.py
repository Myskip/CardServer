# -*- coding: utf-8 -*-
if 0:
    from scripts.lib.tips.KBEDebug import *
    from scripts.lib.tips.bots import KBEngine
else:
    import KBEngine
    from KBEDebug import *

class CardPool(KBEngine.Entity):
    def __init__(self):
        KBEngine.Entity.__init__(self)
