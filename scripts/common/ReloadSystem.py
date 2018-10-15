import inspect
import os
import importlib
import imp
import copy
import weakref

import KBEngine
from KBEDebug import *

if 0:
    from baseapp import KBEngine
    from common.KBEDebug import *
if 0:
    from cellapp import KBEngine

# 需要把此文件加入热更新黑名单
_blackList = ["ReloadSystem"]
g_allClasses = {}

g_allReloadObjectList = []
class Reload:
    __reload__ = True

    def __init__(self):
        g_allReloadObjectList.append(weakref.ref(self))


def reloadAllModule():
    global g_allClasses
    g_allClasses = {}
    # base cell common user_type文件夹内的所有py全部重载
    if KBEngine.component == "baseapp":
        sb = KBEngine.getResFullPath("base/kbemain.py")
        sb = sb[:-10]
        ll = len(sb)
        for s in KBEngine.listPathRes("base", "py"):
            s = s[ll:-3]
            s = s.replace('/', '.')
            mo = importlib.import_module(s)
            _reloadModule(mo)
    elif KBEngine.component == "cellapp":
        sb = KBEngine.getResFullPath("cell/kbemain.py")
        sb = sb[:-10]
        ll = len(sb)
        for s in KBEngine.listPathRes("cell", "py"):
            s = s[ll:-3]
            s = s.replace('/', '.')
            mo = importlib.import_module(s)
            _reloadModule(mo)
    # reload common
    sb = KBEngine.getResFullPath("common/KBEDebug.py")
    sb = sb[:-11]
    ll = len(sb)
    for s in KBEngine.listPathRes("common", "py"):
        s = s[ll:-3]
        s = s.replace('/', '.')
        mo = importlib.import_module(s)
        _reloadModule(mo)
    # reload userType
    sb = KBEngine.getResFullPath("user_type/UserType.py")
    sb = sb[:-11]
    ll = len(sb)
    for s in KBEngine.listPathRes("user_type", "py"):
        s = s[ll:-3]
        s = s.replace('/', '.')
        mo = importlib.import_module(s)
        _reloadModule(mo)

    _reloadAllObjects()

"""
重载模块,然后把模块里面的需要重载的类全部加
"""


def _reloadModule(mo):
    if mo.__name__ in _blackList:
        return

    imp.reload(mo)
    for name, Cls in inspect.getmembers(mo):
        if getattr(Cls, '__reload__', False):
            path = inspect.getsourcefile(Cls)
            g_allClasses[path + Cls.__name__] = Cls


def _reloadAllObjects():
    delList = []

    for ref in g_allReloadObjectList:
        obj = ref()
        if obj:
            n = inspect.getsourcefile(obj.__class__) + obj.__class__.__name__
            if n in g_allClasses:
                obj.__class__ = g_allClasses[n]
            else:
                WARNING_MSG("not find Class " + n)
        else:
            delList.append(ref)
    for ref in delList:
        g_allReloadObjectList.remove(ref)
