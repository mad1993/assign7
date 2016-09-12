###### this is the first .py file ###########

####### write your code here ##########

#import modules
import sys

#variable declarations
i = 0
j = 0
counts = [] 
dummy = []
top = []	

#initailization of the data after splitted in the words
str1 = sys.argv
mylist = str1[1].split()
words = len(mylist)

#count the no of unique words in the sentence
while ( i < words ) :
	if (i == 0) :
		dummy.append(mylist[i])
		counts.append(mylist.count(mylist[i]))
		i = i + 1
	else :	
		if (mylist[i] in dummy) :
			mylist.remove(mylist[i])
			i = i + 1
			words = words - 1
		else :	
			dummy.append(mylist[i])
			counts.append(mylist.count(mylist[i]))
			i = i + 1

#print the top 3 used words in the sentence
while (j < 3) :
	maximum = max(counts)
	max_index = counts.index(maximum)
	print dummy[max_index],counts[max_index]
	top.append(dummy[max_index])
	dummy.remove(dummy[max_index])
	counts.remove(counts[max_index])
	j = j + 1

#find the next permutation of these 3 words
max_word = top[0]
second_word = top[1]
third_word = top[2]

length_1 = len(max_word)
length_2 = len(second_word)
length_3 = len(third_word)

print 'Next Permutations of this words are as follows.'
print "%s%s%s" %(max_word[0:length_1-2],max_word[length_1-1],max_word[length_1-2])
print "%s%s%s" %(second_word[0:length_2-2],second_word[length_2-1],second_word[length_2-2])
print "%s%s%s" %(third_word[0:length_3-2],third_word[length_3-1],third_word[length_3-2])







	

