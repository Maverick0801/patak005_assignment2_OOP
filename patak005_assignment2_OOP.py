## getters -- return 
##

class Alchemist:
    def __init__(self):
        pass
    
    def getLaboratory(self):
        pass

    def getRecipes(self):
        pass

    def mixPosition(self):
        pass

    def drinkPotion(self):
        pass

    def collectReagents(self):
        pass

    def refineReagents(self):
        pass



class Laboratory:
    def __init__(self):
        pass

    def mixPotions(self):
        pass

    def addReagent(self):
        pass



class Potion:
    def __init__(self):
        pass

    def calculateBoost(self):
        pass

    def getName(self):
        pass

    def getStall(self):
        pass

    def getBoost(self):
        pass

    def setBoot(self):
        pass


class Reagent:
    def __init__(self):
        pass

    def refine(self):
        pass

    def getName(self):
        pass

    def getPotency(self):
        pass

    def setPotency(self):
        pass


class SuperPotion(Potion):
    def __init__(self):
        pass

    def calculateBoost(self):
        pass

    def getHerb(self):
        pass

    def getCatalyst(self):
        pass


class ExtremePotion(Potion):
    def __init__(self):
        super().__init__()

    def calculateBoost(self):
        return super().calculateBoost()
    
    def getReagent(self):
        pass

    def getPotion(self):
        pass



class Herb(Reagent):
    def __init__(self):
        super().__init__()

    def refine(self):
        pass

    def getGrimy(self):
        pass

    def setGrimy(self):
        pass


class Catalayst(Reagent):
    def __init__(self):
        pass

    def refine(self):
        pass

    def getQuality(self):
        pass

    

