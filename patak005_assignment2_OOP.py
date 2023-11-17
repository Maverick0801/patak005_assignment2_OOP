""" 
File: patak005_assignment2_OOP
Description: This is one of two file largely containing all the main code, consisting of all the classes updated from the UML diagram provided. No output was given so a sample output was produced by me to make sense of how the code comes into the picture. Note: All of the attributes are private and all of the methods are public.
StudentID: 110370430
EmailID: patak005@mymail.unisa.edu.au
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from abc import ABC, abstractmethod

"""
The alchemist class orchestrates and is responsible for collecting the reagents, mixing the potions, and drinking the potions, it does all of this in the laboratory and it has a composition relationship which is shown in the initializer # self.__laboratory = Laboratory()
The recipe dictionary is already provided in the assignment specification and all of the attributes from attack to necromacy are values between 0 and 100. The alchemists first collects the reagents and add them to the respective list, it then mixes the potion and potion is removed from the list and then it drinks the potion and attributes such as self.__attack is changed. 
This is hardcoded a bit in the drink potion() method and at last it refines the reagents. Basically orchestrating the whole game by requesting the herbs, reagents and carrying out lal of these 4 respective functions in the laboratory.
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
        return self.__laboratory

    def getRecipes(self):
        return self.__recipes
    

    "This is the second step that the Alchemist performs in the laboratory which is carrying out the mixPotion() and the potion is removed from the self.__potion list because the potion has been mixed "

    def mixPotion(self, recipes):
        pass 

    " After The potion has been mixed the next step is drinking the potion"
    def drinkPotion(self, potion):
        pass


    """ This is the first step that the Alchemist triggers and performs in the laboratry """

    def collectReagents(self, reagent, amount):  
       self.__laboratory.addReagent(reagent, amount)

    """ This is the last step that the Alchemist triggers """

    def refineReagents(self):
        herbs = self.__laboratory.getHerbs()  
        catalysts = self.__laboratory.getCatalysts()  
        
        for herb in herbs:
            herb.refine()
        
        for catalyst in catalysts:
            catalyst.refine()

""""
 Throughout the whole Alchemy Game, the Laboratory class serves as a container for the reagents, potions, and interactions between them. It cannot exist without the Alchemist class, so if instance of alchemist class is deleted this also is deleted due to the composition relationship it shares. It has 3 lists stored in its attributes and it has aggregation relationship shown to store the herbs and catalyst respectively in their specific lists. It contains lists of herbs, potions, and catalysts. The class methods handle adding reagents (addReagent), mixing potions (mixPotions), and assisting in reagent refinement (refine). 
 Together, these movements imitate an alchemist's mixing station for potions.
 
 """

class Laboratory:
    def __init__(self):
        self.__potions = []
        self.__herbs = []
        self.__catalysts = []


    """ The mixPotions method does this  """


    def mixPotions(self, name, stat, primary, secondary):
        pass 



    " The addReagent method is resposnible in appending the self.__herbs and self.__catalyst lists which are defined in the initializer. It checks whether the reagent is part of the Herb or Catalyst class and based on that it puts them in the specific list by using isinstance() but before appending them to their respective this the amount of potency is set to both the herb and the catalyst "

    def addReagent(self, reagent, amount):
        if isinstance(reagent, Herb):
            reagent.setPotency(amount)  
            self.__herbs.append(reagent)
        if isinstance(reagent, Catalyst):
            reagent.setPotency(amount) 
            self.__catalysts.append(reagent)
    

"""
The potion class is abstract class which is also the parent class of SuperPotion and ExtremePotion. This abstract class describes attributes and methoods of different kinds of potions. 
It includes abstract methods to calculate and access attributes like stat, boost, and name. This class defines the specific potion behaviors that are inherited by subclasses such as SuperPotion and ExtremePotion. 

"""

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

"""
The reagent class is another abstract class which is also a parent class to Hebs and Catlyst. 
This abstract class also controls reagent methods and attributes. It has abstract methods to access and refine attributes such as name and potency.
and has 2 subclasses like Herb and Catalyst, which used methods and inherits it from the parent class.

"""
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

"""
The SuperPotion class managers super potions and uses calculateBoost() to boost user stats. This calculation provided in the assignment specification calculates the potencies of herbs and catalysts, amplifying them by 1.5 times, providing notable stat gains. 
It contains enhancing qualities that are essential for imporiving user stats. The getName , getStat, getBoost, setBoost are all inherited from the abstract class and the getters and setters can be accessed via properties such as Boost defined in the class below
"""
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
        self.__boost += boost 

    Boost = property(getBoost, setBoost)

    """ The calculateBoost method in SuperPoiton inherits the method from the abstract class in Potion which takes in 3 parameters - herbsPotency, catalystPotency, and catalystQuality and performs the calculation as provided in the assignment specification and returns boost rounded to two decimal places"""

    def calculateBoost(self, herbPotency, catalystPotency, catalystQuality):
        boost = herbPotency + (catalystPotency * catalystQuality) * 1.5
        return round(boost, 2)  

    def getHerb(self):
        return self.__herb 
    
    Herb = property(getHerb)

    def getCatalyst(self):
        return self.__catalyst
    
    Catalayst = property(getCatalyst)

"""
Extreme potions are contained in the ExtremePotion class which has two private attributes defined as lists within the initializer. self.__reagent = [], and self.__potions = [] apart from the other attributes it inherits from the abstract class Potion.
, which uses calculateBoost to boost user statistics tenfold. By using this technique, the combined effect of the reagent and potion potencies is tripled. Its boosting methods and attributes allow for strong stat augmentation, which is essential to alchemical mixtures for exceptional user enhancement.

"""
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
        self.__boost += boost

    Boost = property(getBoost, setBoost)

    """ The calculateBoost method in ExtremePoiton inherits from the abstract class in Potion which takes reagentPotency and potionBoost as paramters and performs the calculation as provided by assignment specification. It further enhances the boost by multiplying it by 3 and it is rounded to 2  decimal places"""
    
    def calculateBoost(self, reagentPotency, potionBoost):
        boost = (reagentPotency * potionBoost) * 3.0
        return round(boost, 2)  

    def getReagent(self):
        return self.__reagent
    
    def getPotion(self):
        return self.__potion

"""
 The Herb class he Herb class represents the basic attributes  and methods of herbs.
 These classes include attributes inherited from their parent class whcih is Reagent, but apart from it has another private attribute named grimmmy ehihc returns a bollean value of True and False, grimmy is already True in the paramter, there are grimys in the herbs, but in the refine method the grimy is set to false,  and the potency has been multiplied by 2.5 times as given in the assignment specfication.
 Apart from this it has getGrimmy() which returns whether girmmy = False or grimmy =True and setsGrimmy() which sets the grimmy and to access both these getters and setters a property has been created   Every instance of the Herb class contains unique attributes, like a name, a potency level that indicates how effective it is, and a status that indicates how refined or grimy it is. 
 
 """

class Herb(Reagent):
    def __init__(self, name, potency = 0, grimy = True):
        super().__init__(name, potency)
        self.__grimy = grimy

    def getName(self):     
        return self.__name
        
    def getPotency(self):  
        return self.__potency
    
    def setPotency(self, potency):
        self.__potency += potency

    reagent_potency = property(getPotency, setPotency)

    " The refine method in the Herb class inherits from the abstract class reagent. The method enhances the potency of the herb when it is called by 2.5 times. Secondly, it sets grimmy = False, indicating us that the herb is now refined and doesn't have any grime "
   
    def refine(self):
        self.__potency *= 2.5  
        self.__grimy = False 
        print(f"{self.__name} has been refined. The new potency: {self.__potency}. it is not grimy !")

    def getGrimy(self):
        return self.__grimy

    def setGrimy(self, grimy):
        self.__grimy = grimy  

    Grimy = property(getGrimy, setGrimy)


"""
The Catalyst class is the embodiment of a reagent, inheriting various attributes from its parent class such as name and potency. Besides this, lity, and name. It provides ways to get the name and strength, adjust the strength, and find the current quality level. Its refine method, which improves the catalyst's quality, plays a crucial role and refines() using the calculations specified in the assignment specifications.
Enhancement is indicated by a 1.1 level of increase if the current quality is less than 8.9. But if the quality gets to 8.9 or higher, it peaks at 10, which is the ideal level of refinement. In essence, this class is a type of reagent that is put through a quality refinement process, which produces different effects in the alchemical system depending on the quality level of the reagent.

"""

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

    "  The refine method in the Catalyst class inherits from the abstract class reagent which refines the quality if it is less then 8.9 if it is equal or greater then 8.9 it sets the quanitity to 10 quality less then 8.9 increases it by 10 otherwise if it is equal or greater then 8.9 return or sets the quality as 10 "

    def refine(self):
        if self.__quality < 8.9:
            self.__quality += 1.1
            print(f"{self.__name}'s quality has been increased to {self.__quality}.")
        else:
            self.__quality = 10
            print(f"{self.__name} quality is set to 10. It cannot be refined any further.")

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

# first creating a instance in alchemist class.
alchemist = Alchemist()

# ## first step it does is it collects the reagents 
alchemist.collectReagents("Irit", "Eye of Newt")
print("The reagents collected are: ")

# Alchemist then proceeds to mix the potion
alchemist.mixPotion("Super Attack")
print("Potion is mixed.")

# Drinking the potion
# alchemist.drinkPotion(potion)
# print("Potion drunk.")

# Alchemist refine the reagents
# alchemist.refineReagents()
print("Reagents refined.")


