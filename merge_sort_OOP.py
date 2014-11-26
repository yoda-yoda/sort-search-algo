#Author: Denis Karanja, P15/55431/2012
#Institution: The University of Nairobi, Kenya,
#Department: School of Computing and Informatics, Chiromo campus
#Email: dee.caranja@gmail.com,
#Task: Merge sort- divides a list into 3 parts
#License type: MIT

import time
startTime = time.clock()
class MergeSort:

	def __init__(self):
		pass


	def divideList(self, fullList):
		length = len(fullList)
		if length <= 1:
		  return fullList

		else:
			#divide elemnts
			midOne = length / 3
			midTwo = ((length - midOne) * -1) / 2

			if midOne is not length:	
				#divide list into three parts
				listOne = fullList[0:midOne]
				listTwo = fullList[midOne:midTwo]
				listThree = fullList[midTwo:]
				
				#conquer lists
				sortedListOne = MergeSort().divideList(listOne)
				sortedListTwo = MergeSort().divideList(listTwo)
				sortedListThree = MergeSort().divideList(listThree)

				return MergeSort().mergeLists(sortedListOne, sortedListTwo, sortedListThree)

			else:
				return "\nThe list has to be divided :)"
	def mergeTwoLists(self, listOne, listTwo):
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

	def mergeLists(self, listOne, listTwo, listThree):
		output = outputFinal = []

		#merge listOne and listTwo
		output = MergeSort().mergeTwoLists(listOne, listTwo)

		#Merge listThree and (output = listOne+listTwo)
		outputFinal = MergeSort().mergeTwoLists(output, listThree)

		
		return outputFinal



sortList = [4,3,-1,5,9,10,-4,2,-5,15, 60, -90, 55, 40, 5]

merge = MergeSort()

print merge.divideList(sortList)
print "Program took %f secs to execute\n"%(time.clock() - startTime)


