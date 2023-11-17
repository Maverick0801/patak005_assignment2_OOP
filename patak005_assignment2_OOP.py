""" 
File: patak005_assignment2_OOP
Description: This is one of two file largely containing all the main code, consisting of all the classes updated from the UML diagram provided. No output was given so a sample output was produced by me to make sense of how the code comes into the picture. Note: All of the attributes are private and all of the methods are public.
StudentID: 110370430
EmailID: patak005@mymail.unisa.edu.au
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from abc import ABC, abstractmethod

"""
The alchemist class orchestrates and is responsible for collecting the ragents, mixing the potions, and drinking the potions, it does all of this in the laboratory and it has a composition relationship which is shown in the initializer # self.__laboratory = Laboratory()
The recipe dictionary is already provided in the assignment specification and all of the attributes from attack to necromacy are values between 0 and 100
"""
class Alchemist:
    def __init__(self):
        self.__attack = 0 
        self.__strength = 0
        self.__defense = 0
        self.__magic = 0
        self.__ranged = 0
        self.__necromacy = 0
        self.__laboratory = Laboratory() 
        self.__recipes = {
            "Super Attack": ["Irit", "Eye of Newt"],
            "Super Strength": ["Kwuarm", "Limpwurt Root"],
            "Super Defence": ["Cadantine", "White Berries"],
            "Super Magic": ["Lantadyme", "Potato Cactus"],
            "Super Ranging": ["Dwarf Weed", "Wine of Zamorak"],
            "Super Necromancy": ["Arbuck", "Blood of Orcus"],
            "Extreme Attack": ["Avantoe", "Super Attack"],
            "Extreme Strength": ["Dwarf Weed", "Super Strength"],
            "Extreme Defence": ["Lantadyme", "Super Defence"],
            "Extreme Magic": ["Ground Mud Rune", "Super Magic"],
            "Extreme Ranging": ["Grenwall Spike", "Super Ranging"],
            "Extreme Necromancy": ["Ground Miasma Rune", "Super Necromancy"]
        }

    
    def getLaboratory(self):
        # do i show the composition relationsip here
        ## labboatory = Laboratory()
        return self.__laboratory

    def getRecipes(self):
        return self.__recipes

    def mixPotion(self, recipes):
        pass
    ## recipe = self.__recipes.get(potion_name)
       # if recipe:
         #   self.__laboratory.mixPotions(recipe[0], recipe[1]) 

    def drinkPotion(self, potion):
        pass

    def collectReagents(self, reagant, amount):  ## amount i think so refers to the potency 
        return self.__potions.append(reagant, amount)

    def refineReagents(self):
        pass


""""""

""""""

class Laboratory:
    def __init__(self):
        self.__potions = []
        self.__herbs = []
        self.__catalysts = []

    def mixPotions(self, name, type, stat, primaryIngrediant, secondaryIngrediant):
       # if isinstance(primaryIngrediant, ):
            # retTURN 
        ## IF isinstance(secondayIngrediant, )
        pass 

    def addReagent(self, reagent, amount):
        pass

## Doubt 1 - where do i establish that all the attributes ranging from attack to necromancy are from 0 to 100 not more than that not less then that


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
        pass
        
    @abstractmethod
    def getStat(self):
        pass

    @abstractmethod
    def getBoost(self):
        pass 

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
    def getName(self):    
        pass

    @abstractmethod
    def getPotency(self):
        pass  

    @abstractmethod
    def setPotency(self, potency):
        pass


class SuperPotion(Potion):
    def __init__(self, name, stat, boost,):
        super().__init__(name, stat, boost)
        self.__herb = []
        self.__catalyst = [] 

    def getName(self):
        return self.__name

    def getStat(self):
        return self.__stat

    def getBoost(self):
        return self.__boost
        
    def setBoost(self, boost):
        pass 

    Boost = property(getBoost, setBoost)


    def calculateBoost(self, herb_potency, catalyst_potency, catalyst_quality):
        # Calculatd  the boost for SuperPotion
        boost = herb_potency + (catalyst_potency * catalyst_quality) * 1.5
        return round(boost, 2)  

    def getHerb(self):
        return self.__herb 
    
    Herb = property(getHerb)

    def getCatalyst(self):
        return self.__catalyst
    
    Catalayst = property(getCatalyst)


class ExtremePotion(Potion):
    def __init__(self, name, stat, boost, ):
        super().__init__(name, stat, boost)
        self.__reagent = []
        self.__potion = []

    def getName(self):
        return self.__name

    def getStat(self):
        return self.__stat

    def getBoost(self):
        return self.__boost
        
    def setBoost(self, boost):
        pass 

    Boost = property(getBoost, setBoost)

    def calculateBoost(self, reagent_potency, super_potion_boost):
        boost = (reagent_potency * super_potion_boost) * 3.0
        return round(boost, 2)  

    def getReagent(self):
        return self.__reagent
    
    def getPotion(self):
        return self.__potion
    

class Herb(Reagent):
    def __init__(self, name, potency):
        super().__init__(name, potency)
        self.__grimy = True

    def getName(self):     
        return self.__name
        
    def getPotency(self):  
        return self.__potency
    
    def setPotency(self, potency):
        self.__potency += potency

    reagent_potency = property(getPotency, setPotency)

    def refine(self):
        self.__potency *= 2.5  
        self.__grimy = False 
        print(f"{self.__name} has been refined. New potency: {self.__potency}. It's no longer grimy.")


    def getGrimy(self):
        return self.__grimy

    def setGrimy(self, grimmy):
        if grimmy == False:
            print("yolo")
        return self.__grimy 

    Grimy = property(getGrimy, setGrimy)

class Catalyst(Reagent):
    def __init__(self, name, potency, quality ):
        super().__init__(name, potency)
        self.__quality = quality


    def getName(self):     
        return self.__name
    
    reagent_name = property(getName)
    
    def getPotency(self):  
        return self.__potency
    
    def setPotency(self, potency):
        self.__potency += potency

    reagent_potency = property(getPotency, setPotency)


    def refine(self):
        if self.__quality < 8.9:
            self.__quality += 1.1
            print(f"{self.__name}'s quality has been increased to {self.__quality}.")
        else:
            self.__quality = 10
            print(f"{self.__name} quality is set to maximum (10). It cannot be refined any further.")


    def getQuality(self):
        return self.__quality



"""
That cuminates all the main code, below here is a small output generated. Objects have been defined as mentioned in the assignmnet specification and I have produced a small output code a the end as well
"""

# I have defined all the herb objects as given in the assignment specification 
arbuck = Herb("Arbuck", 2.6)
avantoe = Herb("Avantoe", 3.0)
cadantine = Herb("Cadantine", 1.5)
dwarf_weed = Herb("Dwarf Weed", 2.5)
irit = Herb("Irit", 1.0)
kwuarm = Herb("Kwuarm", 1.2)
lantadyme = Herb("Lantadyme", 2.0)
torstol = Herb("Torstol", 4.5)

# I have defined all the catalyst objects as given in the assignment specification
eye_of_newt = Catalyst("Eye of Newt", 4.3, 1.0)
limpwurt_root = Catalyst("Limpwurt Root", 3.6, 1.7)
white_berries = Catalyst("White Berries", 1.2, 2.0)
potato_cactus = Catalyst("Potato Cactus", 7.3, 0.1)
wine_of_zamorak = Catalyst("Wine of Zamorak", 1.7, 5.0)
blood_of_orcus = Catalyst("Blood of Orcus", 4.5, 2.2)
ground_mud_rune = Catalyst("Ground Mud Rune", 2.1, 6.7)
grenwall_spike = Catalyst("Grenwall Spike", 6.3, 4.9)
ground_miasma_rune = Catalyst("Ground Miasma Rune", 3.3, 5.2)


""" I have created a small output code of how the Alchemist Game runs """

## first creating a instance in alchemist class.
alchemist = Alchemist()

## first step it does is it collects the reagents which are added in the potions list in the laboratory
alchemist.collectReagents("irit", "eye_of_newt")

## second thing is that it mixes the potions and 
alchemist.mixPotion()

## print out the list of potions
laboratory = Laboratory ()
#laboratory(.get().get())

alchemist.drinkPotion()

## print out the potion list again to remove it

alchemist.refineReagents()

