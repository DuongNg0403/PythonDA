f = open("test.txt")
lines = [x.rstrip() for x in f]
print(lines)
f.close()