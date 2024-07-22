d = {}
print(type(d))
print(len(d))

d["a"] = 100
print(d)
d["a"] = 1000
print(d)
d["x"] = 10
print(d)

print(d.get('w', 123))
print(d)

print(d.setdefault('a', 123))
print(d)

# print(d["xd"])
print(d.get("xd"))

d["c"] = 999
print(d)

d.update({'e': 23, 'f': 12})
print(d)

# del d["a"]
# print(d)

print(d.pop("a"))
print(d)

print(d.popitem())
print(d)

for value in d.values():
    print(f"{value}")
