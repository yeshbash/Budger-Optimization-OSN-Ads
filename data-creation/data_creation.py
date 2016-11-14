import random
import pickle
from decimal import *

getcontext().prec = 3
loc_attr = "Location"
age_attr = "Age"
edu_attr = "Education"
gender_attr = "Gender"
eth_attr = "Ethinicity"
income_attr = "Income"

def generate_price(type):
	if type ==1:
		return Decimal(random.uniform(6,12))/Decimal(1)
	elif type ==2:
		return Decimal(random.uniform(5,10))/Decimal(1)
	elif type ==3:
		return Decimal(random.uniform(4,8))/Decimal(1)
	elif type ==4:
		return Decimal(random.uniform(4,6))/Decimal(1)
	elif type ==5:
		return Decimal(random.uniform(3,5))/Decimal(1)
	elif type ==6:
		return Decimal(random.uniform(2,4))/Decimal(1)

label_sets = {}
with open("C:\\Users\\yeshwanth\\Test\\attribute_values","rb") as f:
	attribute_values = pickle.load(f)

for loc in attribute_values["Location"]:
	label_sets[tuple(sorted({loc_attr+":"+loc}))]= generate_price(1)
	for gender in attribute_values["Gender"]:
		label_sets[tuple(sorted({gender_attr+":"+gender}))]= generate_price(1)
		label_sets[tuple(sorted({loc_attr+":"+loc,gender_attr+":"+gender}))]= generate_price(2)
		for edu in attribute_values["Education"]:
			label_sets[tuple(sorted({edu_attr+":"+edu}))]= generate_price(1)
			label_sets[tuple(sorted({loc_attr+":"+loc,edu_attr+":"+edu}))]= generate_price(2)
			label_sets[tuple(sorted({gender_attr+":"+gender,edu_attr+":"+edu}))]= generate_price(2)
			label_sets[tuple(sorted({loc_attr+":"+loc,gender_attr+":"+gender,edu_attr+":"+edu}))]= generate_price(3)
			for age in attribute_values["Age"]:
				#4C1
				label_sets[tuple(sorted({age_attr+":"+age}))]= generate_price(1)
				#4C2
				label_sets[tuple(sorted({loc_attr+":"+loc,age_attr+":"+age}))]= generate_price(2)
				label_sets[tuple(sorted({gender_attr+":"+gender,age_attr+":"+age}))]= generate_price(2)
				label_sets[tuple(sorted({edu_attr+":"+edu,age_attr+":"+age}))]= generate_price(2)
				#4C3
				label_sets[tuple(sorted({loc_attr+":"+loc,gender_attr+":"+gender,age_attr+":"+age}))]= generate_price(3)
				label_sets[tuple(sorted({loc_attr+":"+loc,edu_attr+":"+edu,age_attr+":"+age}))]= generate_price(3)
				label_sets[tuple(sorted({gender_attr+":"+gender,edu_attr+":"+edu,age_attr+":"+age}))]= generate_price(3)
				#4C4
				label_sets[tuple(sorted({loc_attr+":"+loc,gender_attr+":"+gender,edu_attr+":"+edu,age_attr+":"+age}))]= generate_price(4)
				for income in attribute_values["Income"]:
					#5C1
					label_sets[tuple(sorted({income_attr+":"+income}))]= generate_price(1)
					#5C2
					label_sets[tuple(sorted({loc_attr+":"+loc,income_attr+":"+income}))]= generate_price(2)
					label_sets[tuple(sorted({gender_attr+":"+gender,income_attr+":"+income}))]= generate_price(2)
					label_sets[tuple(sorted({edu_attr+":"+edu,income_attr+":"+income}))]= generate_price(2)
					label_sets[tuple(sorted({age_attr+":"+age,income_attr+":"+income}))]= generate_price(2)
					#5C3
					label_sets[tuple(sorted({loc_attr+":"+loc,gender_attr+":"+gender,income_attr+":"+income}))]= generate_price(3)
					label_sets[tuple(sorted({loc_attr+":"+loc,edu_attr+":"+edu,income_attr+":"+income}))]= generate_price(3)
					label_sets[tuple(sorted({loc_attr+":"+loc,age_attr+":"+age,income_attr+":"+income}))]= generate_price(3)
					label_sets[tuple(sorted({gender_attr+":"+gender,edu_attr+":"+edu,income_attr+":"+income}))]= generate_price(3)
					label_sets[tuple(sorted({gender_attr+":"+gender,age_attr+":"+age,income_attr+":"+income}))]= generate_price(3)
					label_sets[tuple(sorted({edu_attr+":"+edu,age_attr+":"+age,income_attr+":"+income}))]=generate_price(3)
					#5C4
					label_sets[tuple(sorted({loc_attr+":"+loc,gender_attr+":"+gender,edu_attr+":"+edu,income_attr+":"+income}))]= generate_price(4)
					label_sets[tuple(sorted({loc_attr+":"+loc,gender_attr+":"+gender,age_attr+":"+age,income_attr+":"+income}))]= generate_price(4)
					label_sets[tuple(sorted({gender_attr+":"+gender,age_attr+":"+age,edu_attr+":"+edu,income_attr+":"+income}))]= generate_price(4)
					label_sets[tuple(sorted({loc_attr+":"+loc,age_attr+":"+age,edu_attr+":"+edu,income_attr+":"+income}))]= generate_price(4)
					#5C5				
					label_sets[tuple(sorted({loc_attr+":"+loc,gender_attr+":"+gender,edu_attr+":"+edu,age_attr+":"+age,income_attr+":"+income}))]= generate_price(5)
					for eth in attribute_values["Ethinicity"]:
						#6C1
						label_sets[tuple(sorted({eth_attr+":"+eth}))]= generate_price(1)
						#6C2
						label_sets[tuple(sorted({loc_attr+":"+loc,eth_attr+":"+eth}))]= generate_price(2)
						label_sets[tuple(sorted({gender_attr+":"+gender,eth_attr+":"+eth}))]= generate_price(2)
						label_sets[tuple(sorted({edu_attr+":"+edu,eth_attr+":"+eth}))]= generate_price(2)
						label_sets[tuple(sorted({age_attr+":"+age,eth_attr+":"+eth}))]= generate_price(2)
						label_sets[tuple(sorted({income_attr+":"+income,eth_attr+":"+eth}))]= generate_price(2)
						#6C3
						label_sets[tuple(sorted({loc_attr+":"+loc,gender_attr+":"+gender,eth_attr+":"+eth}))]= generate_price(3)
						label_sets[tuple(sorted({loc_attr+":"+loc,edu_attr+":"+edu,eth_attr+":"+eth}))]= generate_price(3)
						label_sets[tuple(sorted({loc_attr+":"+loc,age_attr+":"+age,eth_attr+":"+eth}))]= generate_price(3)
						label_sets[tuple(sorted({loc_attr+":"+loc,income_attr+":"+income,eth_attr+":"+eth}))]= generate_price(3)
						label_sets[tuple(sorted({gender_attr+":"+gender,edu_attr+":"+edu,eth_attr+":"+eth}))]= generate_price(3)
						label_sets[tuple(sorted({gender_attr+":"+gender,age_attr+":"+age,eth_attr+":"+eth}))]= generate_price(3)
						label_sets[tuple(sorted({gender_attr+":"+gender,income_attr+":"+income,eth_attr+":"+eth}))]= generate_price(3)
						label_sets[tuple(sorted({edu_attr+":"+edu,age_attr+":"+age,eth_attr+":"+eth}))]=generate_price(3)
						label_sets[tuple(sorted({edu_attr+":"+edu,income_attr+":"+income,eth_attr+":"+eth}))]= generate_price(3)
						label_sets[tuple(sorted({age_attr+":"+age,income_attr+":"+income,eth_attr+":"+eth}))]= generate_price(3)
						#6C4
						label_sets[tuple(sorted({loc_attr+":"+loc,gender_attr+":"+gender,edu_attr+":"+edu,eth_attr+":"+eth}))]= generate_price(4)
						label_sets[tuple(sorted({loc_attr+":"+loc,gender_attr+":"+gender,age_attr+":"+age,eth_attr+":"+eth}))]= generate_price(4)
						label_sets[tuple(sorted({loc_attr+":"+loc,gender_attr+":"+gender,income_attr+":"+income,eth_attr+":"+eth}))]= generate_price(4)
						label_sets[tuple(sorted({loc_attr+":"+loc,edu_attr+":"+edu,income_attr+":"+income,eth_attr+":"+eth}))]= generate_price(4)
						label_sets[tuple(sorted({loc_attr+":"+loc,edu_attr+":"+edu,age_attr+":"+age,eth_attr+":"+eth}))]= generate_price(4)						
						label_sets[tuple(sorted({loc_attr+":"+loc,age_attr+":"+age,income_attr+":"+income,eth_attr+":"+eth}))]= generate_price(4)												
						#label_sets[tuple(sorted({loc_attr+":"+loc,gender_attr+":"+gender,edu_attr+":"+edu,eth_attr+":"+eth}))]= generate_price(1,12)
						label_sets[tuple(sorted({gender_attr+":"+gender,edu_attr+":"+edu,age_attr+":"+age,eth_attr+":"+eth}))]= generate_price(4)
						label_sets[tuple(sorted({gender_attr+":"+gender,edu_attr+":"+edu,income_attr+":"+income,eth_attr+":"+eth}))]= generate_price(4)
						label_sets[tuple(sorted({gender_attr+":"+gender,age_attr+":"+age,income_attr+":"+income,eth_attr+":"+eth}))]= generate_price(4)
						label_sets[tuple(sorted({edu_attr+":"+edu,age_attr+":"+age,income_attr+":"+income,eth_attr+":"+eth}))]= generate_price(4)
						#label_sets[tuple(sorted({age_attr+":"+age,edu_attr+":"+edu,income_attr+":"+income,eth_attr+":"+eth}))]= generate_price(1,12)
						#6C5
						label_sets[tuple(sorted({loc_attr+":"+loc,gender_attr+":"+gender,edu_attr+":"+edu,age_attr+":"+age,eth_attr+":"+eth}))]= generate_price(5)
						label_sets[tuple(sorted({gender_attr+":"+gender,edu_attr+":"+edu,age_attr+":"+age,income_attr+":"+income,eth_attr+":"+eth}))]= generate_price(5)
						label_sets[tuple(sorted({loc_attr+":"+loc,edu_attr+":"+edu,age_attr+":"+age,income_attr+":"+income,eth_attr+":"+eth}))]= generate_price(5)
						label_sets[tuple(sorted({loc_attr+":"+loc,gender_attr+":"+gender,age_attr+":"+age,income_attr+":"+income,eth_attr+":"+eth}))]= generate_price(5)
						label_sets[tuple(sorted({loc_attr+":"+loc,gender_attr+":"+gender,edu_attr+":"+edu,income_attr+":"+income,eth_attr+":"+eth}))]= generate_price(5)
						#6C6
						label_sets[tuple(sorted({loc_attr+":"+loc,gender_attr+":"+gender,edu_attr+":"+edu,age_attr+":"+age,income_attr+":"+income,eth_attr+":"+eth}))]= generate_price(6)

with open("C:\\Users\\yeshwanth\\Test\\label_costs","wb") as f:
	pickle.dump(label_sets,f)

print("Done")