# -*- coding: utf-8 -*-
if 0:
    from scripts.lib.tips.baseapp import KBEngine
    from scripts.lib.tips.KBEDebug import *
    from scripts.base.Avatar import Avatar
else:
    import KBEngine
    from KBEDebug import *
    from Avatar import Avatar

def debugPlayers(avatarNum):
    params = {
        "name": "player1",
        "gems": 0
    }

    for i in range(0, avatarNum):
        KBEngine.createEntityAnywhere("Avatar", params)

    for key, value in KBEngine.entities.items():
        print(isinstance(value, Avatar))
        if isinstance(value, Avatar):
            KBEngine.entities.get(key).reqMatch(0)