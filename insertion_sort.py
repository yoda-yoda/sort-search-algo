def insertionSort(list):
	for index in range(1, len(list)):
		value = list[index]
		i = index - 1

		while i >= 0 and (value < list[i]):
			list[i+1] = list[i]
			list[i] = value
			i -= 1

	return list

a = [1,4,3,6,2,9,5,3,-1,-3,0]
print "The list was {0}".format(a)
insertionSort(a)
print "Sorted list is{0}".format(a)