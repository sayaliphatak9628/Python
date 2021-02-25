#Sets is unordered collection of data & is iterable, mutable, no duplicates
# it uses hashtable to check values, no index linking available
'''
#creation of set
set_example = {"python","machine learning","data structure"}
print(set_example)

set_examp = set(["machinelearning","python","data structure"])
print(set_examp)

myset = {2.0, "Hello", (2,1,4), 2.0}
print(myset)

#{} - is a dictionary while set() is a set
myset = {}
print(type(myset))
myset = set()
print(type(myset))

#adding & updating sets
set_courses = {"python","ds","ml"}
print(set_courses)
set_courses.add("OOP")
print(set_courses)
set_courses.update("res",["c++","java","ai"])
print(set_courses)

#removing deleting elements of sets
courses={"python","ml","ds","oop","c++","java"}
print(courses)
courses.discard("c++")
print(courses)
courses.remove("ds")
print(courses)
courses.clear()
print(courses)
del courses
print(courses)

#sets operation
set1 = {1,2,3,4,5}
set2 = {5,6,7,8,9}
print(set1 | set2) #union
print(set1 & set2) #intersect
print(set1 - set2) #difference
print(set1 ^ set2) #symetric difference i.e exclusive of present values in both

#sets function
set1 = {1,2,3,4,5}
print(2 in set1)
print(4 not in set1)

print(len(set1))
for s in set1:
    print(s)

#frozen sets - elements once assigned cant be changed, added or deleted.
A = frozenset([1,2,3,4,5,6,7])
print(A)
A.add(8)
'''
#assignment
l1=[1 ,2, 3, 6, 5, 4, 4, 2, 5, 3, 6, 1, 6, 5, 3, 2, 4, 1, 2, 5, 1, 4, 3, 6, 8, 4, 3, 1,5 ,6, 2 ]
set1, set2 = set(), set()
for room in l1:
    if room not in set1:
        set1.add(room)
    else:
        set2.add(room)
        set1.difference_update(set2)
print(set1.pop())
    
