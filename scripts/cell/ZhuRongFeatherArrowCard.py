# -*- coding: utf-8 -*-
if 0:
    from scripts.lib.tips.cellapp import KBEngine
    from scripts.lib.tips.KBEDebug import *
    from cell.components.Card import Card
    from common.ReloadSystem import *
else:
    import KBEngine
    from KBEDebug import *
    from ReloadSystem import *

class ZhuRongFeatherArrowCard(KBEngine.Entity, Reload):

    def __init__(self):
        KBEngine.Entity.__init__(self)
        Reload.__init__(self)
        DEBUG_MSG("ZhuRongFeatherArrowCard[%i].cell init." % (self.id))