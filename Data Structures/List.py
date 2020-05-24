import bisect
c = [1,2,2,2,3,4,7]
print(bisect.bisect(c,2))#useful for finding insertion points
print(bisect.bisect(c,5))
print(bisect.bisect(c,6))
#enumerate: keep track of the index of the current item
for i, value in enumerate(c):
    print("{},{}".format(i,value))

#zip: “pairs” up the elements of a number of lists, tuples, or other sequences
d = ["one","two","two","two","three","four","seven"]
zipped = zip(c,d)
print(list(zipped))