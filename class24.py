'''Operations on Sets
Outline:
Write a program to create a set and perform the following operations on that set-
1. Create a set with integer elements 2. Create a set with mixed data type elements 3.
Create another set with elements - 1, 2, 3, 4, 3, 2 4.
Create a set from a list with elements -
[1, 2, 3, 2] 5. Print the set after removing the first element from this set - [0, 1, 3, 4, 5]
'''
mySet = {1, 2, 3, 4, 3.14, "string"}
mySet2 = {1, 2, 3, 4, 3, 2, 4}
print(mySet)
print(mySet2)
mySet3 = set([1, 2, 3, 2])
print(mySet3)
newSet = set([0, 1, 3, 4, 5])
newSet.pop()
print(newSet)

'''Set Intersection
Outline:
Write a program to find the intersection of two sets. Set1 = {green, blue} Set2 =
{blue, yellow}'''
Set1 = {"green", "blue"}
Set2 = {"blue", "yellow"}
Set3 = Set1.union(Set2)
print(Set3)
'''Arrays
Outline:
Write a program to create an array with the following elements -
[1, 3, 5, 3, 7, 9, 3]. Then find the number of occurrences of number 3 in the array.
Also, print the reversed array.'''
array = [1, 3, 5, 3, 7, 9, 3]
print(array.count(3))
array.reverse()
print(array)

