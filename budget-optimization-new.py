import pickle
import collections
from decimal import *

getcontext().prec = 3
################Utility Methods########################

#Returns label set in dictionary key format
def get_lable_key(label_list):
	return tuple(sorted(label_list))

#Loads serialized data
def load_data(path):
	with open(path,"rb") as f:
		return pickle.load(f)
#Returns users matching labels in label_set
def get_users(label_set):
	l_users = {}
	for i,l in enumerate(label_set):
		if i ==0:
			l_users = set(label_users[l])
		else:
			l_users = l_users&label_users[l]
	return l_users

def initialize_data():
	usr_size = input("User set size")
	label_cost = load_data("C:\\Users\\yeshwanth\\Test\\label_costs")
	label_users = load_data("C:\\Users\\yeshwanth\\Test\\label_users-"+usr_size)
	label_attribues = load_data("C:\\Users\\yeshwanth\\Test\\attribute_values")
	return label_cost,label_users,label_attribues

################Algorithm Methods########################	

def threshold_check(allocation,threshold,li,lp):
	li_cover = allocation/label_cost[li]
	lp_cover = allocation/label_cost[lp]
	
	if li_cover-lp_cover >= Decimal(threshold)*lp_cover:
		return True
	else:
		return False
	

#Extends current label set by adding an optimal attribute. Attribute with highest cummulative RI is chosen optimal
#Param : cur_ls - Current Label Set | label_ri - Current Ratio of Increment List | u_st - Target Users
#Return : labels_found - Status of extension | label_ri - Updated RI List
def extend_labelset(cur_ls, label_ri,u_st):
	#Selecting unused label attributes
	unused_l = label_attribues.keys() - [i.split(":")[0] for i in cur_ls ]
	labels_found = False
	if len(unused_l) >0:
		attribute_ri = collections.defaultdict(Decimal)
		attr_label_ri = collections.defaultdict(list)
		for attr in unused_l:
			for val in label_attribues[attr]: #Domain of each unused attribute
				ext_l = attr+":"+val
				ext_lk = get_lable_key(list(cur_ls)+[ext_l])
				u_ext_lk = get_users(ext_lk)
				common_users = u_ext_lk & u_st
				if len(common_users) > 0 and label_cost[ext_lk] < label_cost[cur_ls]:
					#Calculating the ratio of increment
					ri_val = getcontext().divide(len(common_users)* label_cost[cur_ls],label_cost[ext_lk]*len(u_ext_lk))
					attr_label_ri[attr].append((ext_lk,ri_val))
					attribute_ri[attr] += ri_val
		#Deducing the optimal attribute to add
		if len(attribute_ri) >0 :
			labels_found = True
			opt_attr = max(attribute_ri.keys(), key = lambda k : attribute_ri[k])
			#print("Optimal Attribute : ",opt_attr )
			for l_ri in attr_label_ri[opt_attr]:
				label_ri[l_ri[0]] = l_ri[1] #Including labels of optimal attribute to RI list
			#print("Total Lables Added on top of",cur_ls,":", len(attr_label_ri[opt_attr]))
	
	return labels_found,label_ri

# Allocates 'budget' to the label set 'ls'
# Param : ls - target label set | budget - budget allocation for ls | users - total uncovered users
# Return: remaining budget, remaining uncovered users from input 'users'

def allocate_budget(ls, budget, users):
	global users_covered
	ls_users = get_users(ls)
	#Allocation = Minimum of covering entire set or the available budget
	allocation = min(label_cost[ls]*len(ls_users), budget)
	label_budget[ls] = allocation #Adding to budget distribution
	b_budget = budget - allocation
	if allocation==label_cost[ls]*len(ls_users):
		b_users  = users - ls_users #Remaining uncovered users 
	else:
		b_users = users
	users_covered += int(allocation/label_cost[ls]) #Users covered stats tracker
	#print("Budger Allocation:\nLabel:",ls,"\nBudger Allocated:",allocation,"\nUsers Covered",  allocation/label_cost[ls],"\nRemaining Budger:",b_budget)
	
	return b_budget,b_users

#Optimized Budget Distribution for a given Budget and Preferred Label set
#Param : label_set - Preferred Label Set | b_0 - Advertiser Budger | u_st - Target Users
def optimize_budget(label_set, b_0, u_st, alloc_thrsold):
	label_ri = collections.defaultdict(Decimal)
	#Initial Extension of Label set
	extension, label_ri = extend_labelset(label_set,label_ri,u_st)
	if extension == True:
		while b_0 >0 and len(u_st) >0: #Iterates untill budget available or untill all users are covered
			if len(label_ri) >0: #If optimal lables available for adding
				max_ri_label = max(label_ri.keys(),key = lambda k : label_ri[k])
				max_ri_users = get_users(max_ri_label)
				allocation_needed = min(label_cost[max_ri_label]*len(max_ri_users), b_0)
				del label_ri[max_ri_label]
				#print("Max RI Label :",max_ri_label)
				if threshold_check(allocation_needed,alloc_thrsold,max_ri_label,label_set) == True:
					#print("Allocation Threshold met")
					b_0,u_st = allocate_budget(max_ri_label,b_0,u_st)
				else:
					#print("Allocation Threshold Not Met")
					extension, label_ri = extend_labelset(max_ri_label,label_ri,u_st)
					if extension == True:
						#print("Further Extension Possible. Continuing..")
						continue
					else:
						#print("No more extension possible")
						b_0,u_st = allocate_budget(max_ri_label,b_0,u_st)
			else:
				#Allocates maximum budget to current optimal label set
				b_0,u_st = allocate_budget(label_set,b_0,u_st)
	else:
		#No optimization possible.
		b_0,u_st = allocate_budget(label_set,b_0,u_st)

		

################Main Logic########################
		
print("[Debug] Initializing Data")
#Loading label_cost and label_users from data set file
label_cost,label_users,label_attribues = initialize_data()

print("[Debug] Initization Complete")

print("Enter a key to continue. 'N' to exit")
while(input()!="N"):
	#Initialization
	users_covered = 0
	label_budget = collections.defaultdict(Decimal)

	l_p = input("Preferred Label:")
	l_p_key = get_lable_key([i.strip() for i in l_p.split(",")])
	u_st = get_users(l_p_key) #Target User Set
	print("Total users in input label set: ",len(u_st))
	print("Cost per user: ",label_cost[l_p_key])
	
	b_0 = Decimal(input("Budget:"))
	alloc_threshold = int(input("Allocation Threshold in %: "))/100
	print("[Debug] Algorithm Begin")
	
	optimize_budget(l_p_key,b_0,u_st,alloc_threshold)
	
	print("Result Summary\n",label_budget)
	print("Users Covered:", users_covered)
	print("Extra users covered:", users_covered - int(b_0/label_cost[l_p_key]))
	print("Enter a key to continue. 'N' to exit")