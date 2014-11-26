#Author: Denis Karanja, P15/55431/2012
#Institution: The University of Nairobi, Kenya,
#Department: School of Computing and nodeInformatics,
#Email: dee.caranja@gmail.com,
#Task: Merge sort- divided into 3 parts

def divideList(fullList):
	length = len(fullList)
	if length <= 1:
	  return fullList

	else:
		#divide elemnts
		mid = length / 3
		midTwo = ((length - mid) * -1) / 2

		#divide list into three parts
		listOne = fullList[0:mid]
		listTwo = fullList[mid:midTwo]
		listThree = fullList[midTwo:]

		#conquer lists
		sortedListOne = divideList(listOne)
		sortedListTwo = divideList(listTwo)
		sortedListThree = divideList(listThree)

		return mergeLists(sortedListOne, sortedListTwo, sortedListThree)

def mergeTwoLists(listOne, listTwo):
	i = j = 0
	output = []
	lengthOne = len(listOne)
	lengthTwo = len(listTwo)

	#deal with two lists first
	while i < lengthOne or j < lengthTwo:
		#case 1 (both lists have data)
		if i < lengthOne and j < lengthTwo:
			if listOne[i] <= listTwo[j]:
				output += [listOne[i]]
				i += 1
			else:
				output += [listTwo[j]]
				j += 1

		#case 2 (only listOne have data)
		elif i < lengthOne:
			output += [listOne[i]]
			i += 1

			#case 3 (only list two has data)
		else:
			output += [listTwo[j]]
			j += 1

	return output

def mergeLists(listOne, listTwo, listThree):
	output = outputFinal = []

	#merge listOne and listTwo
	output = mergeTwoLists(listOne, listTwo)

	#Merge listThree and (output = listOne+listTwo)
	outputFinal = mergeTwoLists(output, listThree)

	
	return outputFinal


sortList = [4,3,-1,5,9,10,-4,2,-5,15, 60, -90, 55, 40]

print divideList(sortList)


