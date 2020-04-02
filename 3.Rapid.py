
print("                 METHOD 1                      ")
print("-------------------------------------------------")
print('\n')
d={"Rick": 85, "Amit": 42, "George": 53, "Tanya": 60, "Linda": 35}
print("d=",d)
c=d.values()
print(c)
print("Result is=",sum(c))
print('\n')
print('\n')


print("                 METHOD 2                      ")
print("-------------------------------------------------")


n=int(input("How many dictionary items :"))
l1=[]
l2=[]
for i in range(n):
    keys=input("Enter the key name:")
    values=int(input("Enter the values:"))
    l1.append(keys)
    l2.append(values)
a=zip(l1,l2)
d=dict(a)
print("d=",d)

result=d.values()
print("Result is=:",sum(result))




