# -*- coding: utf-8 -*-
if 0:
    from scripts.lib.tips.cellapp import KBEngine
    from scripts.lib.tips.KBEDebug import *
    from scripts.user_type.Card_INFOS import *
    from scripts.data import d_card_init
    from scripts.server_common.ServerDefine import *
    from common.ReloadSystem import *
else:
    import KBEngine
    from KBEDebug import *
    from Card_INFOS import *
    import d_card_init
    from ServerDefine import *
    import random
    from ReloadSystem import *

class CardPool(KBEngine.Entity, Reload):

    def __init__(self):
        KBEngine.Entity.__init__(self)
        Reload.__init__(self)
        DEBUG_MSG("CardPool[%i].cell init." % (self.id))
        self.battleField = KBEngine.entities.get(self.battleFieldEid)
        self.cards = []
        self.initPool()

    # init pool from d_card_init
    def initPool(self):
        index = 0
        tmpCards = []
        for cardInfos in d_card_init.datas.values():
            DEBUG_MSG(cardInfos["cardScript"] + " entity created.")
            params = {
                "card":{
                    "cardInfo": card_info_inst.createObjFromDict(cardInfos),
                    "drawedBy": 0,
                }
            }
            card = KBEngine.createEntity(cardInfos["cardScript"], self.spaceID, CARD_INIT_POSITION, self.direction, params)
            tmpCards.append(card)

        self.cards = self.mixCards(tmpCards)
        self.cardsNum = len(self.cards)

    def mixCards(self, _cards):
        cards = []

        while(len(_cards) > 0):
            i = random.randint(0, (len(_cards)-1))
            card = _cards.pop(i)
            cards.append(card)
            card.index = cards.index(card)
        return cards

    #init draw for players
    def initDraw(self, _avatar, cardNum):
        pass

    def drawCard(self, _avatar):
        DEBUG_MSG("CardPool drawCard._avatar[%i]" % (_avatar.id))
        if (len(self.cards) <= 0):
            #TODO: card used out effects.
            DEBUG_MSG("CardPool drawCard._avatar[%i] card used out." % (_avatar.id))
            return

        i = random.randint(0, (len(self.cards) - 1))
        cardEntity = self.cards.pop(i)
        cardEntity.card.drawedBy = _avatar.id
        self.cardsNum = len(self.cards)
        cardEntity.teleport(_avatar, _avatar.position, _avatar.direction)
        return  cardEntity

    def onDestroy( self ):
        for card in self.cards:
            card.destroy()


