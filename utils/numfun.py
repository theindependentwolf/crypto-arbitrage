from decimal import *


def get_largest_difference(input_list):
	"""
	Get the largest difference of the elements in the list. Return 0 if atmost 1 elements is present. 
	"""
	if len(input_list) <= 1:
		return "0.00000000"
	else:
		sorted_list = sorted(input_list)
		max_diff = '{:.9f}'.format(Decimal(sorted_list[len(sorted_list) - 1]) - Decimal(sorted_list[0]))
		return max_diff

def get_percentage_difference(input_list):
	"""
	Get percentage difference between highest and lowest numbers
	"""
	if len(input_list) <= 1:
		return "0.00"
	else:
		sorted_list = sorted(input_list)
		highest = Decimal(sorted_list[len(sorted_list) - 1])
		lowest = Decimal(sorted_list[0])
		price_diff = highest - lowest
		if format(price_diff) == 0.00:
			per_diff = '0.00'
		else:
			if lowest == 0:
				per_diff = 0.00
			else:
				per_diff = ((highest - lowest)/lowest) * 100
		return '{:.2f}'.format(per_diff)


def get_percent_difference(val_1, val_2):
	"""
	Get percent difference between two values
	"""
	per_diff = ((val_1 - val_2)/val_2) * 100
	return per_diff