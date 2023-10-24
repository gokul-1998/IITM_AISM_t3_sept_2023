







nodes='abcdefghijklmno'
nodes=list(nodes)

path='flamebingojkhcd'

ord_repr=[]

for i in path:
  ord_repr.append(nodes.index(i)+1)
  nodes.remove(i)
print(ord_repr)
   