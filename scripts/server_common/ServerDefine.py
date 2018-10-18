# -*- coding: utf-8 -*-
if 0:
    from scripts.lib.tips.cellapp import KBEngine
    from scripts.lib.tips.KBEDebug import *
else:
    import KBEngine
    from KBEDebug import *

#服务端timer定义
TIMER_TYPE_TURN_MANAGER                                         = 1 #TimeManager timer

PLAYER_TABLE_POSITIONS                                          = [(10, 0, 0), (0, 0, -10), (-10, 0, 0), (0, 0, 10)]
CARD_POOL_POSITION                                              = (0,0, 0)
CARD_INIT_POSITION                                              = (500,0, 0)
