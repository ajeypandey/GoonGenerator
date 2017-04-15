#ORC Generator
import random

proficiency = random.randrange(1,5) 

STR = random.randrange(2,5)
DEX = random.randrange(0,3)
CON = random.randrange(2,5)
INT = random.randrange(-3,1)
WIS = random.randrange(-2,2)
CHA = random.randrange(-2,3)

AC = 10+DEX+random.randrange(2,5)
HPMAX = (3*(random.randrange(1,9)+CON))
WEAPON = random.choice([["Crossbow (100/400)","1d8","piercing"],["Maul","2d6","bludgeoning"],["Greataxe","1d12","slashing"]])
HIT = (int)(STR+proficiency)
DAMAGE = WEAPON[0]+ " " + WEAPON[1] + "+" +  (str)((int)(STR+proficiency)) + " " + WEAPON[2]

print "STR:\t" + (str)(STR)
print "DEX:\t" + (str)(DEX)
print "CON:\t" + (str)(CON)
print "INT:\t" + (str)(INT)
print "WIS:\t" + (str)(WIS)
print "CHA:\t" + (str)(CHA)
print "+" + (str)(proficiency) + " to Intimidation"
print "Darvision 60 ft, Passive Perception 10"
print "AC:\t" + (str)(AC)
print "HP:\t" + (str)(HPMAX)
print "HIT:\t+" + (str)(HIT)
print "DMG:\t" + DAMAGE