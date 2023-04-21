


sec = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
l = sec.replace(".", "").replace(",", "").split(" ")
Dictionaly = {}
for i in range(len(l)):
    if i+1==1 or i+1==5 or i+1==6 or i+1==7 or i+1==8 or i+1==9 or i+1==15 or i+1==16 or i+1==19:
        Dic1 = {l[i][0]:i+1}
        Dictionaly.update(Dic1)
    else:
        Dic2 = {l[i][0:2]:i+1}
        Dictionaly.update(Dic2)

print(Dictionaly)
