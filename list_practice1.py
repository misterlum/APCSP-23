#Practice: 0
#0) Print out each element in the list
print("0:\nYour output:")
list0 = [2, 4, 6, 8]

#implement your code between here and the Expected output line
for x in list0:
	print(x)

print("Expected output:\n2\n4\n6\n8\n")

#Exercises: 1 - 9
#1) Print out each element in the list, followed by an exclamation point
#	Hint: Concatenate strings with +
print("1:\nYour output:")
list1 = ["Let's","Go","Dogs"]

#implement code here

print("Expected output:\nLet's!\nGo!\nDogs!\n")

#2) Sum up all of the elements in the list, then print out that resulting sum.
#	Hint: Add numbers with +
#	Real Hint: Do we need to create another variable for this?
print("2:\nYour output:")
list2 = [1, 3, 5, 7, 9]

#implement code here
#sum = 0

print("Expected output:\n25\n")

#3) Write your own version of extend(), where you append() each element of a list
#		to the end of another list
print("3:\nYour output:")
list3a = [1, 2]
list3b = [3, 4]

#implement code here

print("Expected output:\n[1, 2, 3, 4]\n")

#4) Write your own version of count(), where you count the number of times a value is
#		found in a list. In this case, that value we are trying to find is True
#	Hint: Check for equality with what symbol(s)?
print("4:\nYour output:")
list4 = [False, False, True, False, True, True, False, True, False]
count = 0

#implement code here

print(count)
print("Expected output:\n4\n")

#5) Write your own version of reverse that prints the contents of a list in reverse order
#	Extension: Don't just print it, make the list equal to the reversed list!
print("5:\nYour output:")
list5 = ["H","He","Li","Be","B", "C", "N", "O", "F"]

#implement code here

print("Expected output:\n[F, O, N, C, B, Be, Li, He, H]\n")

#6) Write an improved version of index() that prints the indices of each occurrence of
#		a target value. In this case, that value we are trying to find is contained in toFind
#               whose value is True.
#	Example: Finding 1 in [1, 1, 2]
#	Output:
#	0
#	1
print("6:\nYour output:")
toFind = True
list6 = [False, False, True, False, True, True, False, True, False]

#implement code here

print("Expected output:\n2\n4\n5\n7\n")

#7) Write your own version of remove() that removes all values from the list that equal
#		the target value. In this case, toFind's value is Goose
print("7:\nYour output:")
toFind = "Goose"
list7 = ["Duck","Goose","Duck","Goose","Duck","Duck"]

#implement code here

print("Expected output:\n[Duck, Duck, Duck, Duck]\n")

#8) Write code that will remove all evens from the list
#	Example: From list8 = [1, 2, 3, 4, 5, 6], remove all even values
#       Hint: How do we find out if a value is even?
print("8:\nYour output:")
list8 = [1, 2, 3, 4, 5, 6]

#implement code here

print("Expected output:\n[1, 3, 5]\n")

#9) Write code that will remove each value in one list from another list
#	Example: From list9a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], remove the values [2, 4, 6, 8]
#       which are contained in list9b
#       Hint: This may be tricky, but try using more loops?
print("9:\nYour output:")
list9a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list9b = [2, 4, 6, 8]

#implement code here

print("Expected output:\n[1, 3, 5, 7, 9, 10]\n")
