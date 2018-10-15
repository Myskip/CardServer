# -*- coding: utf-8 -*-
if 0:
    from scripts.lib.tips.KBEDebug import *
    from scripts.lib.tips.bots import KBEngine
else:
    import KBEngine
    from KBEDebug import *
    import Avatar_INFOS
    from Avatar_INFOS import Avatar_INFOS


class Account(KBEngine.Entity):
    def __init__(self):
        KBEngine.Entity.__init__(self)
        self.base.reqHasAvatar()

    def onHasAvatar(self, hasAvatar):
        DEBUG_MSG("Account[%i].onHasAvatar[%i]." % (self.id, hasAvatar))
        if (hasAvatar):
            pass
        else:
            avatar_info = {
                "name" : "kbe_bot_%s" % self.id,
                "gems" : 0,
            }
            self.base.createAvatar(avatar_info)
