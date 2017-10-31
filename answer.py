import random
# This is to figure out if my brother Tom, bought Great Value Burritos or Tina's from WalMart at any given date. 

def q1(): 
	a1 = "Which aisle of Walmart?"
	a2 = "What color packaging was the burrito in?"
	a3 = "Were the beans, dare I say..... a bit grainy?"

	ansdict = {a1: False, a2: False, a3: True, a4: False} 
	randict = {}
	keys = ansdict.keys()
	random.shuffle(keys)
	for key in keys:
		randict[key] = ansdict[key]
	return randict 

def q2(): 
	a1 = "They were a bit grainy, so Tinas."
	a2 = "Not so grainy, so Great Value."
	a3 = "I got Totinos, so none of the above."
	ansdict = {a1: False, a2: True, a3: False, a4: False}
	randict = {}
	keys = ansdict.keys()
	random.shuffle(keys)
	for key in keys:
		randict[key] = ansdict[key]
	return randict

def q3(): 
	a1 = "Burrito aisle number."
	a2 = "Frozen food section."
	a3 = "Tinas."
	a4 = "Great Value."
	ansdict = {a1: True, a2: False, a3: False, a4: False}
	randict = {}
	keys = ansdict.keys()
	random.shuffle(keys)
	for key in keys:
		randict[key] = ansdict[key]
	return randict
