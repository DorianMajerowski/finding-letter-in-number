strInput = input('Give number: ')

def hasLetter(letter):
	if letter >= '0' and letter <= '9' or letter == '.':
		return True
	else:
		False

for x in range(len(strInput)):
	print(hasLetter(strInput[x]))