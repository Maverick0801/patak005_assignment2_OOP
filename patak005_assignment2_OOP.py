""" 
File: filename.py
Description: There is only one file containing all the code, consisting of all the classes updated from the class diagram. Class Materials is not changed and enough docstrings are provided to ecplain the code functionality
Author: Aum Patel
StudentID: 110100110
EmailID: patak005@mymail.unisa.edu.au
This is my own work as defined by the University's Academic Misconduct Policy.

"""
from abc import ABC, abstractmethod

class Alchemist:
    def __init__(self):
        self.__attack = 0 ## int 
        self.__strength = 0
        self.__defense = 0
        self.__magic = 0
        self.__ranged = 0
        self.__necromacy = 0
        self.__laboratory = [] ## do i write this self.__laboratory = Laboratory() to show the compostiotn relationship
        self.__recipes = {}
    
    def getLaboratory(self):
        # do i show the composition relationsip here
        ## labboatory = Laboratory()
        return self.__laboratory

    def getRecipes(self):
        self.__recipes

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
        self.__potions = []
        self.__herbs = []
        self.__catalysts = []

    def mixPotions(self):
        pass

    def addReagent(self):
        pass



class Potion(ABC):
    def __init__(self, name, stat, boost):
        self.__name = name 
        self.__stat = stat
        self.__boost = boost

    @abstractmethod
    def calculateBoost(self):
        pass
    
    @abstractmethod
    def getName(self):
        return self.__name ## abstract class pass methods
        

    @abstractmethod
    def getStat(self):
        return self.__stat ## abstract class pass methods

    @abstractmethod
    def getBoost(self):
        return self.__boost ## abstract class pass methods 

    @abstractmethod
    def setBoot(self, boost):
        pass


class Reagent(ABC):
    def __init__(self, name, potency):
        self.__name = name
        self.__potency = potency 

    @abstractmethod
    def refine(self):
        pass
    
    @abstractmethod
    def getName(self):     ## abstract class pass method
        return self.__name 

    @abstractmethod
    def getPotency(self):  ## abstract class pass method
        return self.__potency

    @abstractmethod
    def setPotency(self, potency):
        pass


class SuperPotion(Potion):
    def __init__(self, name, stat, boost,):
        super().__init__(name, stat, boost)
        self.__herb = []
        self.__catalyst = [] 

    def calculateBoost(self):
        pass

    def getHerb(self):
        return self.__herb 

    def getCatalyst(self):
        return self.__catalyst


class ExtremePotion(Potion):
    def __init__(self, name, stat, boost, ):
        super().__init__(name, stat, boost)
        self.__reagent = []
        self.__potion = []

    def calculateBoost(self):
        pass

    def getReagent(self):
        return self.__reagent

    def getPotion(self):
        return self.__potion



class Herb(Reagent):
    def __init__(self, name, potency):
        super().__init__(name, potency)
        self.__grimy = True

    def refine(self):
        pass

    def getGrimy(self):
        return self.__grimy

    def setGrimy(self, grimmy):
        pass


class Catalayst(Reagent):
    def __init__(self, name, potency, quality ):
        super().__init__(name, potency)
        self.__quality = quality

    def refine(self):
        pass

    def getQuality(self):
        return self.__quality

    

