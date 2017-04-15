#Eldritch Knight Generator. Because Eldritch Knights are too damn cool
import random
import math

tuffness = input("Goon level? (Min Lvl 3)\n")
proficiency = (int)((tuffness/5)+2)			#approximate. it works well enough.

STR = random.randrange(0,3)
DEX = random.randrange(0,3)
CON = random.randrange(0,3)
INT = random.randrange(2,5)
WIS = random.randrange(-1,3)
CHA = random.randrange(-1,3)

CAST = proficiency + INT	#Eldritch Knights use INT
SAVE = CAST + 8
SlotSet = [[2],[3],[3],[3],[4,2],[4,2],[4,2],[4,3],[4,3],[4,3],[4,3,2],[4,3,2],[4,3,2],[4,3,3],[4,3,3],[4,3,3],[4,3,3,1],[4,3,3,1]]
SlotCount = [3,4,4,4,5,6,6,7,8,8,9,10,10,11,11,11,12,13]
SLOTS = SlotSet[(int)(tuffness-4)]
MaxSpellLevel = len(SLOTS)
SpellCount = SlotCount[(int)(tuffness-4)]

CantripList = open("0-SpellList.txt").read().split('\n')
CantripCount = 2
if tuffness >=10:
	CantripCount +=1
CANTRIPS = random.sample(CantripList, CantripCount)
Scan = 1
SPELLS = []
ABILITIES = []

while SpellCount>0:
	if len(SPELLS)>=MaxSpellLevel-1:
		SpendSpells = SpellCount 	#at max level allowed, dump all spells left
	else:
		SpendSpells = (int)(SpellCount/2.4)+1
	Spellsheet = (str)(Scan) + "-SpellList.txt"
	SpellList = open(Spellsheet).read().split('\n')
	SPELLS.append(random.sample(SpellList, SpendSpells))
	SpellCount-=SpendSpells

STYLE = random.choice(["ARCH","DEF","DUELDEX","DUELSTR","GWEAP","PROT","2WEAP"])
if STYLE=="ARCH":	#Archery
	DEX+=2
	DMG=DEX
	WEAPON = random.choice([["Crossbow (100/400)","1d10"],["Longbow (150/600)","1d8"]])
	SHIELD = False
elif STYLE=="DEF":	#Defense
	CON+=2
	DMG=STR
	WEAPON = random.choice([["Battleaxe","1d8"],["Morningstar","1d8"]])
	SHIELD = True
elif STYLE=="DUELDEX": #Dueling, Dexterity
	DEX+=2
	DMG=DEX
	WEAPON = ["Rapier","1d8+2"]
	SHIELD = False
elif STYLE=="DUELSTR": #Dueling, Strength
	STR+=2
	DMG=STR
	WEAPON = random.choice([["Battleaxe","1d8+2"],["Morningstar","1d8+2"]])
	SHIELD = False
elif STYLE=="GWEAP": #Great Weapon
	STR+=2
	DMG=STR
	WEAPON = random.choice([["Greatsword","2d6"],["Halberd","1d10"],["Warhammer","1d10"],["Pike","1d10"]])
	SHIELD = False
	ABILITIES.append("Great Weapon")
elif STYLE=="PROT": #Protection
	DEX+=2
	DMG=DEX
	WEAPON = ["Rapier","1d8"]
	SHIELD = True
	ABILITIES.append("Protection")
else: #Two-weapon.
	DEX+=2
	DMG=DEX
	WEAPON = ["Shortsword x2","1d6x2"]
	SHIELD = False
	ABILITIES.append("Two-Weapon")

ABILITIES.extend(["Second Wind","Action Surge","Weapon Bond"])

if tuffness >=5:
	ABILITIES.append("Extra Attack")
if tuffness >=7:
	ABILITIES.append("War Magic")
if tuffness >=9:
	ABILITIES.append("Indomitable")
if tuffness >=10:
	ABILITIES.append("Eldritch Strike")

AC = 10+DEX+random.randrange(1,4)
if STYLE=="DEF":
	AC+=1
HPMAX = 3+(int)((random.uniform(1,8)+CON)*tuffness)		#this is more exact.
HITDICE = WEAPON[1]
HIT = (int)(DMG+proficiency)
DAMAGE = HITDICE + "+" +  (str)((int)(DMG))

print "STR:\t" + (str)(STR)
print "DEX:\t" + (str)(DEX)
print "CON:\t" + (str)(CON)
print "INT:\t" + (str)(INT)
print "WIS:\t" + (str)(WIS)
print "CHA:\t" + (str)(CHA)
print ""
print "STYLE:\t" + (str)(STYLE)
print "AC:\t" + (str)(AC)
print "SHIELD?\t" +(str)(SHIELD)
print "HP:\t" + (str)(HPMAX)
print "WEAPON:\t" + (str)(WEAPON[0])
print "HIT:\t" + (str)(HIT)
print "DMG:\t" + DAMAGE
print "CAST:\t" + (str)(CAST) 
print "SAVE:\t" + (str)(SAVE)
print "SLOTS:\t" + (str)(SLOTS)
print "CANTRIPS:\n\t" + (str)(CANTRIPS)
print "SPELLS:"
for i in range(0, len(SPELLS)):
	if SPELLS[i] != "":			#if not empty
		print "LEVEL " + (str)(i+1) + ":\n\t" + (str)(SPELLS[i])
print "ABILITIES:\n\t" + (str)(ABILITIES)