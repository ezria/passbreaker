import datetime

def tryOtherValue(intArray, position, size, password) :
	passBreaked = False;	
	j = 48
	while j<58 and passBreaked == False:
		intArray[position] = j
		passBreaked = compareIntArrayToUniChrArray(intArray, password)
		if position+1 < size : 
			passBreaked = tryOtherValue (intArray, position+1, size, password)
		j+=1
	return passBreaked
def compareIntArrayToUniChrArray(intArray, password) :
	passBreaked = False
	uniStr = ""
	for charInt in intArray :
		uniStr+=chr(charInt)	
	if (uniStr == password) : 
		print("Numero trouve :" , uniStr)
 		passBreaked = True
	return passBreaked

def main () :
	password = raw_input("Saisissez un mot de passe avec seulement des chiffres : ")
	timeBegin = datetime.datetime.now()
	passBreaked = False
	arraySize = 0
	testingPass = [0]*arraySize
	while passBreaked == False:
		arraySize+=1
		print("ajout d'un numero, nombre de numero :", arraySize)
		testingPass = [0]*arraySize
		passBreaked = tryOtherValue(testingPass, 0, arraySize, password)		
	duration = datetime.datetime.now() - timeBegin

	uniStr = ""
	for charInt in testingPass :
		uniStr+=chr(charInt)	
	print ("Mot de passe trouve :", str(testingPass))
	print ("duree pour trouver le mot de passe : ")
 	print duration
#	print duration.strftime('%M minutes, %S secondes, %Z millisecondes') 
main()
