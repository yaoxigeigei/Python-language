r1=dict(name="八嘎",age=18,salary=10000)
r2=dict(name="消极",age=18,salary=30000)
r3=dict(name="啊大大",age=18,salary=20000)
tb=[r1,r2,r3]
for x in tb:
    if x.get("salary")>10000:
        print(x)