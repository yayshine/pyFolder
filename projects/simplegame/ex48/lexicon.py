directions = ['north', 'south', 'east', 'west',
				'down', 'up', 'left', 'right', 'back']
verbs = ['go', 'stop', 'kill', 'eat']
stops = ['the', 'in', 'of', 'from', 'at', 'it']
nouns = ['door', 'bear', 'princess', 'cabinet']

def convert_number(s):
	try:
		return int(s)
	except ValueError:
		return None

def scan(sentence):
	words = sentence.split()
	output = []

	for word in words:
		temp = word.lower()
		if temp in directions:
			output.append(('direction', word))
		elif temp in verbs:
			output.append(('verb', word))
		elif temp in stops:
			output.append(('stop', word))
		elif temp in nouns:
			output.append(('noun', word))
		else:
			converted = convert_number(word)
			if isinstance(converted, int):
				output.append(('number', converted))
			else:
				output.append(('error', word))
	return output