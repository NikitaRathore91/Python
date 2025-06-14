#collection of unordered items
#each element in et must be unique and it is immutable    set on whole is mutable ie we can add remove things
# we cannot store list and dictionary in set
# we can store int,float,string,tuple in set

collection = {1,2,3,4} # this is a set
print(type(collection))
print(collection)  # o/p -> 1 2 3 4

collection1 = {1,1,2,3,4}
print(type(collection1))
print(collection1)   # o/p -> 1 2 3 4

collection2 = {1,2.2,"hello",True}
print(type(collection2))
print(collection2)

print(len(collection2))

collection3 = {}  #this is syntax of empty dictionary not empty set
print(type(collection3))

# set methods -> set.add(ele) , set.remove(el) , set.clear() , set.pop() ,set.union(set2) , set.intersection(set2)

collection.add(5)
print(collection)

collection.remove(1)  #removes element with val = 1
print(collection)

collection.clear()  # clears up whole set
print(collection)

collection1.pop()   #pops a random value
print(collection1)

set1 = {1,2,3,4}
set2 = {3,4,5,6}

print(set1.union(set2))
print(set1.intersection(set2))