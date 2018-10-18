# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
import d_card_init


class Card_INFOS(list):
    """
    """

    def __init__(self):
        """
        """
        list.__init__(self)

    def asDict(self):
        '''
        data = {
            "name"			    : self[0],
            "type"		        : self[1],
            "cardID"            : self[2],
            "cardScript"        : self[3],
            "cardCost"          : self[4],
            "cardGain"          : self[5],
            "powerNum"          : self[6],
            "skillType"         : self[7],
            "isDirected"        : self[8],
            "skillScript"       : self[9]
        }
        '''

        data = {}
        i = 0

        for value in d_card_init.datas.values():
            cardInfoDict = value
            break

        for keys,value in cardInfoDict.items():
            tmp = {
                keys: self[i]
            }
            data.update(tmp)
            i += 1
        return data

    def createFromDict(self, dictData):
        '''
        self.extend([dictData["name"],
                     dictData["type"],
                     dictData["cardID"],
                     dictData["cardScript"],
                     dictData["cardCost"],
                     dictData["cardGain"],
                     dictData["powerNum"],
                     dictData["skillType"],
                     dictData["isDirected"],
                     dictData["skillScript"]])
        '''
        for value in d_card_init.datas.values():
            cardInfoDict = value
            break

        for key in cardInfoDict.keys():
            self.append(dictData[key])

        return self

class Card_INFOS_PICKLER:
	def __init__(self):
		pass

	def createObjFromDict(self, dct):
		return Card_INFOS().createFromDict(dct)

	def getDictFromObj(self, obj):
		return obj.asDict()

	def isSameType(self, obj):
		return isinstance(obj, Card_INFOS)

card_info_inst = Card_INFOS_PICKLER()