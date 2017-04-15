#Goon Generator
import random
import math

tuffness = input("Goon level?\n")
proficiency = (int)((tuffness/5)+2)			#approximate. it works well enough.

STR = random.randrange(-1,3)
DEX = random.randrange(-1,3)
CON = random.randrange(-1,4)
INT = random.randrange(-1,4)
WIS = random.randrange(2,5)
CHA = random.randrange(-1,4)

CAST = proficiency + WIS	#Druids use WIS, bro
SAVE = CAST + 8
SlotSet = [[2],[3],[4,2],[4,3],[4,3,2],[4,3,3],[4,3,3,1],[4,3,3,2],[4,3,3,3,1],[4,3,3,3,2],[4,3,3,3,2,1],[4,3,3,3,2,1],[4,3,3,3,2,1,1],[4,3,3,3,2,1,1],[4,3,3,3,2,1,1,1],[4,3,3,3,2,1,1,1],[4,3,3,3,2,1,1,1,1],[4,3,3,3,3,1,1,1,1],[4,3,3,3,3,2,1,1,1],[4,3,3,3,3,2,2,1,1]]
SLOTS = SlotSet[(int)(tuffness-1)]
MaxSpellLevel = len(SLOTS)
SpellCount = sum(SLOTS)

AC = 10+DEX+random.randrange(0,4)
HPMAX = 3+(int)((random.uniform(1,8)+CON)*tuffness)		#this is more exact.
HITDICE = random.choice(["1d4","1d6"])
HIT = (int)(STR+proficiency)
DAMAGE = HITDICE + "+" +  (str)((int)(STR+proficiency))

CantripList = open("0-SpellList.txt").read().split('\n')
CantripCount = 2
if tuffness >=4:
	CantripCount +=1
if tuffness >=10:
	CantripCount +=1
SpellCount = (int)(WIS+tuffness)
CANTRIPS = random.sample(CantripList, CantripCount)
Scan = 1
SPELLS = []
ABILITIES = []

while SpellCount>0:
	if len(SPELLS)==MaxSpellLevel:
		SpendSpells = SpellCount 	#at max level allowed, dump all spells left
	else:
		SpendSpells = (int)(SpellCount/2.4)+1
	Spellsheet = (str)(Scan) + "-SpellList.txt"
	SpellList = open(Spellsheet).read().split('\n')
	SPELLS.append(random.sample(SpellList, SpendSpells))
	SpellCount-=SpendSpells

CIRCLE = random.choice(["Arctic","Coast","Desert","Forest","Grassland","Mountain","Swamp","Underdark","Moon"])
if CIRCLE=="Arctic":
	ABILITIES.append("WILD SHAPE")
	if tuffness>=3:
		SPELLS[1].extend(["Hold Person","Spike Growth"])		#add second level spells
	if tuffness>=5:
		SPELLS[2].extend(["Sleet Storm","Slow"])					#add third level spells
	if tuffness>=6:
		ABILITIES.append("LAND'S STRIDE")
	if tuffness>=7:
		SPELLS[3].extend(["Freedom of Movement","Ice Storm"])
	if tuffness>=9:
		SPELLS[4].extend(["TBA","TBA"])
elif CIRCLE=="Coast":
	ABILITIES.append("WILD SHAPE")
	if tuffness>=3:
		SPELLS[1].extend(["Mirror Image","Misty Step"])		#add second level spells
	if tuffness>=5:
		SPELLS[2].extend(["Water Breathing","Water Walk"])					#add third level spells
	if tuffness>=6:
		ABILITIES.append("LAND'S STRIDE")
	if tuffness>=7:
		SPELLS[3].extend(["Control Water","Freedom of Movement"])
	if tuffness>=9:
		SPELLS[4].extend(["TBA","TBA"])
elif CIRCLE=="Desert":
	ABILITIES.append("WILD SHAPE")
	if tuffness>=3:
		SPELLS[1].extend(["Blur","Silence"])		#add second level spells
	if tuffness>=5:
		SPELLS[2].extend(["Create Food and Water","Protection from Energy"])					#add third level spells
	if tuffness>=6:
		ABILITIES.append("LAND'S STRIDE")
	if tuffness>=7:
		SPELLS[3].extend(["Blight","Hallucinatory Terrain"])
	if tuffness>=9:
		SPELLS[4].extend(["TBA","TBA"])
elif CIRCLE=="Forest":
	ABILITIES.append("WILD SHAPE")
	if tuffness>=3:
		SPELLS[1].extend(["Barkskin","Spider Climb"])		#add second level spells
	if tuffness>=5:
		SPELLS[2].extend(["Call Lightning","Plant Growth"])					#add third level spells
	if tuffness>=6:
		ABILITIES.append("LAND'S STRIDE")
	if tuffness>=7:
		SPELLS[3].extend(["Divination","Freedom of Movement"])
	if tuffness>=9:
		SPELLS[4].extend(["TBA","TBA"])
elif CIRCLE=="Grassland":
	ABILITIES.append("WILD SHAPE")
	if tuffness>=3:
		SPELLS[1].extend(["Invisibility","Pass without Trace"])		#add second level spells
	if tuffness>=5:
		SPELLS[2].extend(["Daylight","Haste"])					#add third level spells
	if tuffness>=6:
		ABILITIES.append("LAND'S STRIDE")
	if tuffness>=7:
		SPELLS[3].extend(["Divination","Freedom of Movement"])
	if tuffness>=9:
		SPELLS[4].extend(["TBA","TBA"])
elif CIRCLE=="Mountain":
	ABILITIES.append("WILD SHAPE")
	if tuffness>=3:
		SPELLS[1].extend(["Spider Climb","Spike Growth"])		#add second level spells
	if tuffness>=5:
		SPELLS[2].extend(["Lightning Bolt","Meld into Stone"])					#add third level spells
	if tuffness>=6:
		ABILITIES.append("LAND'S STRIDE")
	if tuffness>=7:
		SPELLS[3].extend(["Stone Shape","Stoneskin"])
	if tuffness>=9:
		SPELLS[4].extend(["TBA","TBA"])
elif CIRCLE=="Swamp":
	ABILITIES.append("WILD SHAPE")
	if tuffness>=3:
		SPELLS[1].extend(["Darkness","Melf's Acid Arrow"])		#add second level spells
	if tuffness>=5:
		SPELLS[2].extend(["Water Walk","Stinking Cloud"])					#add third level spells
	if tuffness>=6:
		ABILITIES.append("LAND'S STRIDE")
	if tuffness>=7:
		SPELLS[3].extend(["Freedom of Movement","Locate Creature"])
	if tuffness>=9:
		SPELLS[4].extend(["TBA","TBA"])
elif CIRCLE=="Underdark":
	ABILITIES.append("WILD SHAPE")
	if tuffness>=3:
		SPELLS[1].extend(["Spider Climb","Web"])		#add second level spells
	if tuffness>=5:
		SPELLS[2].extend(["Gaseous Form","Stinking Cloud"])					#add third level spells
	if tuffness>=6:
		ABILITIES.append("LAND'S STRIDE")
	if tuffness>=7:
		SPELLS[3].extend(["Greater Invisibility","Stone Shape"])
	if tuffness>=9:
		SPELLS[4].extend(["TBA","TBA"])
else: #moon circle
	ABILITIES.append("COMBAT WILD SHAPE")
	if tuffness>=6:
		ABILITIES.append("PRIMAL STRIKE")

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
print "CAST:\t" + (str)(CAST) 
print "SAVE:\t" + (str)(SAVE)
print "SLOTS:\t" + (str)(SLOTS)
print "CIRCLE:\t" + (str)(CIRCLE)
print "CANTRIPS:\n\t" + (str)(CANTRIPS)
print "SPELLS:"
for i in range(0, len(SPELLS)):
	if SPELLS[i] != "":			#if not empty
		print "LEVEL " + (str)(i+1) + ":\n\t" + (str)(SPELLS[i])
print "ABILITIES:\n\t" + (str)(ABILITIES)