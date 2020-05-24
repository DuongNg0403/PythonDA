nested_tup = (4,5,6),(7,8)
print(nested_tup)
tup = tuple('string')
print(tup)
print(tup[0])
tup = tuple(['foo', [1, 2], True])
tup[1].append(3)
print(tup)
#######Unpacking tuples
seq = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
for a, b, c in seq:
    print("a={}, b={}, c={}".format(a,b,c))