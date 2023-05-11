#集合
from Num5 import ngr

se = "paraparaparadise"
ss = "paragraph"

X = set(ngr(se,2))
Y = set(ngr(ss,2))
set1 = X | Y
set2 = X & Y 
set3 = X - Y
print(f'X | Y = {set1}')
print(f'X & Y = {set2}')
print(f'X - Y = {set3}')
if "se" in X:
    print("X has se")
else:
    print("X hasn't se")

if se in Y :
    print("Y has se")
else:
    print("Y hasn't se")

