import re
import functools as ft
#re.findall(r"[\w']+",)

f = open("prg5/test.txt",'r')

lis = f.read()
print(lis)
lis = re.findall(r"[\w']+",lis)
print("\n\n",lis)
words = {}

#print(lis)

for i in lis:
	if i not in words:
		words[i] = 1
	else:
		words[i] +=1

sorted_words = dict(sorted(words.items(), key = lambda x:x[1],reverse = True))

ls = list(words.values())

print("\n",ls,"\n")

top_ten = {x:sorted_words[x] for x in list(sorted_words)[:10]}

print("top ten words with most occurrences:")
for i in top_ten:
	print(i,":",top_ten[i])
word_len = []
for x in words.keys():
	word_len.append(len(x))

avg = ft.reduce(lambda a,b :a+b,word_len)/len(word_len)


odd_squares = [x**2 for x in word_len if x%2!= 0]

print("\nAvg length of the words are:{:.2f}\n".format(avg))
print("squares of odd numbers found in length list:\n",odd_squares)


f.close()