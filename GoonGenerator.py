#Goon Generator
import random

level = input("Player level?\n")
party = input("Number in party?\n")
goonz = input("Number of goons?\n")

tuffness = level*party/goonz
proficiency = (int)((tuffness/5)+2)

STR = random.randrange(-1,5)
DEX = random.randrange(-1,5)
CON = random.randrange(-1,5)
INT = random.randrange(-1,5)
WIS = random.randrange(-1,5)
CHA = random.randrange(-1,5)

AC = 10+DEX+random.randrange(0,4)
HPMAX = 5+((random.randrange(1,6)+CON)*tuffness)
HITDICE = random.choice(["1d4","1d6","1d8"])
HIT = (int)(STR+proficiency+random.randrange(-1,2))
DAMAGE = HITDICE + "+" +  (str)((int)(STR+proficiency+random.randrange(-1,2)))

print "STR:\t" + (str)(STR)
print "DEX:\t" + (str)(DEX)
print "CON:\t" + (str)(CON)
print "INT:\t" + (str)(INT)
print "WIS:\t" + (str)(WIS)
print "CHA:\t" + (str)(CHA)
print ""
print "AC:\t" + (str)(AC)
print "HP:\t" + (str)(HPMAX)
print "HIT:\t" + (str)(HIT)
print "DMG:\t" + DAMAGE