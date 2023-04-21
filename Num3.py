sec = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
l = sec.replace(",", "").replace(".", "").split()
lis = []
for i in range(len(l)):
    lis.append(len(l[i]))
print(lis)