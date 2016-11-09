import random
import pickle
import collections
#import copy

num = int(input("Number of users"))
counter = 1

label_users = collections.defaultdict(set)
attribute_values = {}
with open("C:\\Users\\yeshwanth\\Test\\attribute_values","rb") as f:
	attribute_values = pickle.load(f)
labels  = [i for i in attribute_values]

print("Processing Begin")
for counter in range(1,num+1):
	user_id = "user_"+str(counter)
	chars_cnt = random.randint(1,6)
	unused_lables = list(labels)
	#print(user_id,":",chars_cnt)
	for no_chars in range(0,chars_cnt):
		#Picking an unused label attribute
		#print(no_chars,":",unused_lables)
		if len(unused_lables)==1:
			label_idx = 0
		else:
			label_idx = random.randint(0,len(unused_lables)-1)
		label = unused_lables[label_idx]
		del unused_lables[label_idx]
		
		#Picking a value from the domain of the label
		label_len = len(attribute_values[label])
		label_val = attribute_values[label][random.randint(0,label_len-1)]
		char = label+":"+label_val
		
		#Adding user id to the characteristic
		label_users[char].add(user_id)
print("Writing to file")

with open("C:\\Users\\yeshwanth\\Test\\label_users","wb") as f:
	pickle.dump(label_users,f)
print("Processing Complete")