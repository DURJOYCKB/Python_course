collection = {1, 2, 4, "hellow", "world"}

collection.add(5)
collection.remove(2)
#collection.clear()

print(collection)

set1 = {1, 2, 3}
set2 = {2, 3, 4}

print(set1.union(set2))     #{1, 2, 3, 4}    combines both sets.....

print(set1.intersection(set2)) #{2, 3}    returns common value...
