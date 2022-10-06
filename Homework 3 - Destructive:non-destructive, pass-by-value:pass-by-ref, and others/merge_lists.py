def merge_lists(list_a, list_b):
	"""
	the function takes two sorted lists, list_a and list_b, and it should 
	return a single sorted list by merging the two sorted lists. 
	eg: 
	input: list_a = [1, 2, 4, 5, 10]
	       list_b = [1, 3, 3, 6, 9, 10, 11]
	output: merge_lists(list_a, list_b) -> [1, 1, 2, 3, 3, 4, 5, 6, 9, 10, 10, 11]
	"""
	pass

if __name__ == "__main__":
	print(merge_lists([1, 2, 3, 8], [2, 3, 5, 9, 12]))
	print(merge_lists([], [1,2,7,8]))
	print(merge_lists([1, 2, 3, 4, 5], []))
	