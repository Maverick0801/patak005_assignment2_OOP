"""
There are 10 main functions in the whole game so there are 10 tests written for each of the methods. There is no tests written for the two abstract class - Potion and Reagent 
This is a smal summary of the 10 tests and how it was divided in a chrinological order

test1 - class SuperPotion - calculateBoost()
test2 -class ExtremePotioon - calculateBoost()
test3 - class Herb - calculateBoost()
test4 - class Catalyst - calculateBoost()

No tests in the the abstract classes


test5 - class Laboratory - mixPotion()
test6- class Laboratory -addReagent()


test7 - class Alchemist - collectReagent()
test8 - class Alchemist - mixPotion()
test9 - class Alchemist - drinkPotion()
test10 - class Alchemist - refineReagents()

"""
import pytest
from patak005_assignment2_OOP import *
" First tests - Herb class - pytest "

def test_refine_method_refines():
    herb = Herb("Some Herb", 3.0)  
    herb.refine() 

    assert herb.getPotency() == 8.0
    assert not herb.getGrimy() 


def test_refine_method_refines_negative_potency():
    herb = Herb("Negative Potency Herb", -2.0)  
    herb.refine()  

    assert herb.getPotency() == -5.0 
    assert not herb.getGrimy()


" Second tests- Catalyst class"

def test_catalyst_refine_quality_below_8_9():
    catalyst = Catalyst(" Catalyst example is ", potency=5, quality=8.0)
    catalyst.refine()
    assert catalyst.getQuality() == pytest.approx(9.1) 


def test_catalyst_refine_quality_at_8_9():
    catalyst = Catalyst(" Catalyst example is", potency=5, quality=8.9)
    catalyst.refine()
    assert catalyst.getQuality() == 10  


" Third sets of tests - Super Potion class"

@pytest.fixture
def superPotion(): ## variable method defined using pytestfixturee
    return SuperPotion("Super Strength", "Strength", 10)

def test_super_potion_name(superPotion):
    assert superPotion.getName() == "Super Strength"

def test_super_potion_stat(superPotion):
    assert superPotion.getStat() == "Strength"

def test_super_potion_boost(superPotion):
    assert superPotion.getBoost() == 10

def test_super_potion_calculate_boost(superPotion):
    herb_potency = 5
    catalyst_potency = 8
    catalyst_quality = 1.5

    expected_boost = herb_potency + (catalyst_potency * catalyst_quality) * 1.5
    calculated_boost = superPotion.calculate_boost(herb_potency, catalyst_potency, catalyst_quality)

    assert calculated_boost == round(expected_boost, 2)



"set 4 of pytests - ExtremePotion class "


def test_calculate_boost_extreme_potion():
    extreme_potion = ExtremePotion("Extreme Strength", "Strength", 0)
    calculated_boost = extreme_potion.calculateBoost(5, 10)
    expected_boost = (5 * 10) * 3.0
    assert calculated_boost == expected_boost


" set 5 of pytests - Laboratory class - addReagent() "

def test_add_herb_to_lab():
    lab1 = Laboratory()
    herb = Herb("Irit", 0)
    lab1.addReagent(herb, 5)
    assert len(lab1._Laboratory__herbs) == 2
    assert isinstance(lab1._Laboratory__herbs[0], Herb)


def test_add_catalyst_to_lab():
    lab2 = Laboratory()
    catalyst = Catalyst("Eye of Newt", 0, 0)
    lab2.addReagent(catalyst, 10)
    assert len(lab2._Laboratory__catalysts) == 2
    assert isinstance(lab2._Laboratory__catalysts[0], Catalyst)