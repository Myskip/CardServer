# -*- coding: utf-8 -*-
if 0:
    from scripts.lib.tips.baseapp import KBEngine
    from scripts.lib.tips.KBEDebug import *
    from common.ReloadSystem import *

import KBEngine
from KBEDebug import *
from ReloadSystem import *


class Account(KBEngine.Proxy, Reload):
    def __init__(self):
        KBEngine.Proxy.__init__(self)
        Reload.__init__(self)
        self._avatar = None

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

        if self.avatarDBId != 0:
            INFO_MSG("account[%i] entities enable. avatarDBId:%s." % (self.id, self.avatarDBId))
            KBEngine.createEntityAnywhereFromDBID("Avatar", self.avatarDBId, self.onCreateAvatarFromDB)

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
        DEBUG_MSG("Account[%i].onClientDeath:" % self.id)
        self.destroy()

    def onDestroy(self):
        self._avatar.destroy(writeToDB=True)

    def onCreateAvatarFromDB(self, _avatar, dbId, wasActive):
        DEBUG_MSG("onCreateAvatarFromDB,entityCall:%s, dbId:%s, wasActive:%s." % (_avatar, dbId, wasActive))
        self._avatar = _avatar
        self.giveClientTo(_avatar)

    def onCreateAvatar(self, _avatar):
        DEBUG_MSG("onCreateAvatar,args1:%s, args2:%s." % (self, _avatar))
        if _avatar:
            self._avatar = _avatar
            _avatar.writeToDB(self.onAvatarWriteToDB)
        else:
            ERROR_MSG("onCreateAvatar failed.")

    def onAvatarWriteToDB(self, success, _avatar):
        DEBUG_MSG("onAvatarWriteToDB,success:%s." % (success))
        if success:
            self.avatarDBId = _avatar.databaseID
            self.writeToDB()
            self.giveClientTo(_avatar)
            DEBUG_MSG("onAvatarWriteToDB,avatarDBId:%s." % (self.avatarDBId))

    def createAvatar(self, avatar_Infos):
        DEBUG_MSG("createAvatar, name:%s, gems:%s." % (avatar_Infos.asDict()["name"], avatar_Infos.asDict()["gems"]))
        params = {
            "name": avatar_Infos.asDict()["name"],
            "gems": avatar_Infos.asDict()["gems"]
        }

        KBEngine.createEntityAnywhere("Avatar", params, self.onCreateAvatar)

    def reqHasAvatar(self):
        DEBUG_MSG("reqHasAvatar, avatarDBId:%s." % (self.avatarDBId))
        if self.avatarDBId == 0:
            self.client.onHasAvatar(0)
        else:
            self.client.onHasAvatar(1)
