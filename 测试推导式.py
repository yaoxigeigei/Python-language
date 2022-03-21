#列表推导式
y=[x for x in range(5)]
print(y)

x=[x*2 for x in range(1,5)]
print(x)

g=[]
for x in range(6):
    g.append(x)
print(g)

cells=[(row,col) for row in range(10) for col in range(10)]
print(cells)

#字典推导式
my_text="i love you,i love zhaihaojie,i love red"
a={c:my_text.count(c) for c in my_text}
print(a)

#集合推导式
t={x for x in range(100) if(x%2==0)}
print(t)

#生成器推导式(生成元组)  遍历只能用一次
gnt=(x for x in range(10))
print(gnt)          #<generator object <genexpr> at 0x00000222F60C5FC0>
print(tuple(gnt))   #(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(tuple(gnt))   #()   只能用一次
for x in gnt:
    print(x)       #(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)