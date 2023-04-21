#N-gram...任意の文字列をn個の文字で分割するテキスト方法。
#n=2の時、bi-gram(バイグラム)と呼ぶ。
#単語単位と文字単位がある
from ast import Index


s = "I am an NLPer"
l = s.split(" ")
def ngr(S, n):
    return [S[x:x + n] for x in range(len(S) - n + 1)]
print(ngr(s,2))
print(ngr(l,2))
