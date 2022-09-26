import link

class gameMode():
    def __init__(self):
        self.name = "Demo"
        self.description = "A Demo to test the Lasertag system"
        self.icon = None
        
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