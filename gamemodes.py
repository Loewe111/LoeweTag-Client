import link

class demo():
    def __init__(self):
        self.players = {}
        self.defaultHP = 100
        self.MHP = 100
        self.defaultSP = 50
        self.MSP = 100
        self.ATK = 50
    def loop(self):
        pass
    def hit(self):
        pass
    def death(self):
        pass
    def startGame(self):
        self.players = {}
        for i in link.link.node_ids:
            self.players[i] = [self.defaultHP,self.MHP,self.defaultSP,self.MSP,self.ATK,0,0]
        print(self.players)
    def setGameRules(self,HP,MHP,SP,MSP,ATK):
        self.defaultHP = HP
        self.MHP = MHP
        self.defaultSP = SP
        self.MSP = MSP
        self.ATK = ATK

global game
global gamelist
gamelist = {
    'names': ["Demo"],
    'class': [ demo ]
}