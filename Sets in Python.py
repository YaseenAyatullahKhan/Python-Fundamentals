#Creating a set
a_set = {1,2,3,4,5}
print(a_set) #output is same
#another way to create:
new_set = set([1,2,3,4,5])
print(new_set) #output is {1,2,3,4,5}

#Adding and removing elements
a_set.add(6)
print(a_set)

new_set.remove(3)
print(new_set)  #raises error if not found

a_set.discard(0)
print(a_set) #no error even if not found

#set operations
A = {1,2,3}
B = {2,4,5}
C = A|B #union
print(C) #C is {1,2,3,4,5}
C = A&B #intersection
print(C) #C is {2}
C = A-B #difference: C is {1,3}
C = B-A #difference: C is {4,5}. Use this for complement operation.
C = A^B #symmetric difference - in A and B but not both
print(C) #C is {1,3,4,5}

#checking membership
print(3 in B) #False
print(3 in A) #True

#Iteration through a set is like in a list but set is unordered
#Converting between set and list
lst = [1,2,3,4,5]
st = set(lst) #st is {1,2,3,4,5}

st2 = {1,2,3,4,5}
lst2 = list(st2) #lst2 is [1,2,3,4,5]