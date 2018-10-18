# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *


class Avatar_INFOS(list):
    """
    """

    def __init__(self):
        """
        """
        list.__init__(self)

    def asDict(self):
        data = {
            "name"			: self[0],
            "gems"		    : self[1],
        }

        return data

    def createFromDict(self, dictData):
        self.extend([dictData["name"], dictData["gems"]])
        return self

class Avatar_INFOS_PICKLER:
	def __init__(self):
		pass

	def createObjFromDict(self, dct):
		return Avatar_INFOS().createFromDict(dct)

	def getDictFromObj(self, obj):
		return obj.asDict()

	def isSameType(self, obj):
		return isinstance(obj, Avatar_INFOS)

avatar_info_inst = Avatar_INFOS_PICKLER()