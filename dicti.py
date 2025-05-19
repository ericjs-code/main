dic = {"joão": "a", "maria": "b"}
s = "%(joão)s e %(maria)s" 
print(s % dic)

dic.clear()
print(dic)