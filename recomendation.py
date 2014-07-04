from math import sqrt

# data about people's critics

critics ={'Me':{'MayamiVice':5, 'Social network':4, 'Orel&reshka':5},
'Nataly':{ 'Orel&reshka':4,'Social network':5, 'Bethoven':3},
'Galina':{'MayamiVice':5, 'Bethoven':5}}

# evklidov metod ocenki podobia person1 and person2 based on critics
def evk_distance(prefs, person1, person2):
	# similar items
	si={}
	for item in prefs[person1]:
		if item in prefs[person2]:
			si[item]=1
			
	if  len(si)==0: return 0
	
	# calculate distance
	sum_of_squares = sum([pow(prefs[person1][item] - prefs[person2][item],2)  for item in prefs[person1] if item in prefs[person2]])
	
	return 1/(1+sum_of_squares)
	
#print evk_distance(critics, 'Me','Nataly')
#print evk_distance(critics, 'Me','Galina')
