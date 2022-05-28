class SentenceReverser:
	vowels = ["a","e","i","o","u"]
	sentence = ""
	rev = ""
	vcount = 0
	def __init__(self,sentence):
		self.sentence = sentence
		self.revsentence()
	def revsentence(self):
		self.rev = " ".join(reversed(self.sentence.split()))
		#self.rev = " ".join(sorted(self.sentence.split(), key = lambda i: self.getcount(i) , reverse=True))
	def getvcount(self):
		self.vcount = sum(s in self.vowels for s in self.sentence.lower())
		return self.vcount
	def getrev(self):
		return self.rev
	#def getcount(self,sen):
	#	count = sum(s in self.vowels for s in sen.lower())
	#	return count

items = []

for i in range(3):
	sentence = input("Enter a phrase : ")
	reverser = SentenceReverser(sentence.strip())
	items.append(reverser)
	print()

sortedItems = sorted(items, key = lambda i: i.getvcount(), reverse=True)

print ("Sorted on vowel count (descending) : \n")
for i in range(len(sortedItems)):
	print ("Reverse : ", sortedItems[i].getrev(), ", Vowel Count : ", sortedItems[i].getvcount())