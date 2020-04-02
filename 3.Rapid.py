'''n=int(input("How many persons:"))
kl=[]
vl=[]
c={}
for i in range(1,n+1):
    name=input("Enter the name:")
    val=int(input("Enter the values:"))
    kl.append(name)
    vl.append(val)
print(kl)
print(vl)
z=zip(kl,vl)
result=dict(z)
print(result)'''


d={"Rick": 85, "Amit": 42, "George": 53, "Tanya": 60, "Linda": 35}
res=0
c=d.values()
li=list(c)
print(li)
for i in li:
    i=res+i
    res=i
print(i)
    

