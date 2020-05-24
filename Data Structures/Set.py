s1 = {1,1,5,3,4,7,5}
print(s1)
s2 = {2,3,7,5,9}
print(s1|s2)    #s1|=s2 equivalent to s1 = s1|s2
print(s1&s2)    #s1&=s2 equivalent to s1 = s1&s2
print(s1-s2)    #s1-=s2 equivalent to s1 = s1-s2
print(s1^s2)    #s1^=s2 equivalent to s1 = s1^s2
print(s1.isdisjoint(s2))