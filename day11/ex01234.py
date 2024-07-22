s1 = set()
s1.add(100)
s1.update([1,2,3,4])
print(s1)

s2 = {1,3,5,7,9}
new_set01 = s1.union(s2)
new_set02 = s1.symmetric_difference(s2)
new_set03 = s1.intersection(s2)
print(new_set01, new_set02, new_set03, sep = "\n")