import random

s = list(map(str, input().split()))
li = []
last = []
li.append(s[0])
last.append(s[-1])
del s[0],s[-1] 
l = random.sample(s, len(s))
li = li + l + last
print(li)
