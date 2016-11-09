import pickle
import collections
import decimal

decimal.getcontext().prec = 3

def get_lable_key(label_list):
	return tuple(sorted(label_list))

def load_data(path):
	with open(path,"rb") as f:
		return pickle.load(f)

def get_users(label_set):
	l_users = {}
	for i,l in enumerate(label_set):
		if i ==0:
			l_users = set(label_users[l])
		else:
			l_users = l_users&label_users[l]
	return l_users

def get_hval(label_users):
	return max([user_fx[u] for u in label_users if user_fx[u] < 1])


def initialize_ri(users):
	return_list = []
	
	for l in label_cost:
		l_users = get_users(l)
		common_users = l_users&users #Users common to target set and current label set
		if len(common_users)>0:
			return_list.append(l) #Including label set as related label set
			label_ri[l] = len(common_users) / (len(l_users)* label_cost[l]) #Initializing Ratio of Increment
			#Adding label set to user's label set association
			for user in common_users:
				#print(user,":",l)
				user_set_assn[user].add(l) 
	return return_list
	
print("Initializing Data")
#Loading label_cost and label_users from data set file
label_cost = load_data("C:\\Users\\yeshwanth\\Test\\label_costs")
label_users = load_data("C:\\Users\\yeshwanth\\Test\\label_users")


while(input()!="N"):
	#Initialization
	print("[Initialization] In Progress..")
	user_set_assn = collections.defaultdict(set)
	user_fx = collections.defaultdict(int)
	label_ri = collections.defaultdict(int)
	budget = collections.defaultdict(decimal.Decimal)
	max_ri_label,max_ri_val,h_i,max_ri_users = (),0,0,[]
	target_count = 0
	
	l_p = input("Preferred Label:")
	b_0 = decimal.Decimal(input("Budget"))
	l_p_key = get_lable_key([i.strip() for i in l_p.split(",")])
	u_st = get_users(l_p_key) #Target User Set
	print("Total users:",u_st,"\nLen",len(u_st))
	print("Cost per user:",label_cost[l_p_key])
	related_ls = initialize_ri(u_st)
	print("[Initialization] Complete")
	
	input("Wanna beging Algo?:")
	
	while len(u_st) >0 and b_0 > 0  :
		#Getting the label set with maximum ratio of increment
		max_ri_label = max(label_ri.keys(),key = lambda key : label_ri[key])
		max_ri_users = get_users(max_ri_label)
		h_i = get_hval(max_ri_users)
		
		print("Max RI:",max_ri_label,":",max_ri_users,":",h_i)
		
		total_sc = label_cost[max_ri_label]*len(max_ri_users)
		budget_diff = min(b_0,(1-h_i)*total_sc)
		budget[max_ri_label] = budget[max_ri_label]+budget_diff
		
		print("Budget allocated:",budget_diff)
		
		b_0 = b_0 - budget_diff
		
		for user in max_ri_users&u_st:
			user_fx[user] += budget_diff/total_sc
			if user_fx[user] >=1 :
				u_st.remove(user)
				target_count += 1
				for ls in user_set_assn[user]:
					u_ls = get_users(ls)
					label_ri[ls] -= 1/(len(u_ls)*label_cost[ls])
					#update ri for sets with which user is associated with
	print("Total users targetted in expectation:",target_count)
	print("Result\n",budget)
	#print("Total users targetted in expectation:"target_count)