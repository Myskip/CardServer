# -*- coding: utf-8 -*-
if 0:
    from scripts.lib.tips.baseapp import KBEngine
    from scripts.lib.tips.KBEDebug import *
else:
    import KBEngine
    from KBEDebug import *


def countPlayers():
    i = 0
    for e in KBEngine.entities.values():
        if e.__class__.__name__ == "Avatar":
            i += 1

    return i


def countEntities():
    i = 0
    for e in KBEngine.entities.values():
        i += 1

    return i


def playerPool():
    list = []
    for e in KBEngine.globalData["Halls"].playerPool:
        list.append(e.id)

    return list

def setup():
    #KBEngine.addWatcher("playerPool", "PY_LIST", playerPool)
    KBEngine.addWatcher("entities", "UINT32", countEntities)
    KBEngine.addWatcher("players", "UINT32", countPlayers)
