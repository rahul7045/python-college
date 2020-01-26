'''n=int(input("enter the number :"))
d=dict()

for x in range(1,n+1):
	d[x]=x*x

print(d)
#merge
d2={'Rahul':'rahul','PUJARI':'pujari','roll':8692}

d3={'PYTHON':'python','JAVA':'java'}
d2.update(d3)
print(d2)

#sorted by key value not solved

s=dict()

s[1]="rahul"
s[2]="pujari"
s[9]="python"
s[6]="java"
s[11]="programming"

for i in sorted (s) : 
    print (i, s[i])'''

s2=[{'rahul':1},{'pujari':2},{'java':3},{'python':2},{'c++':4},{'languages':5},{'programming':1}]

unique =set(val for dic in s2 for val in dic.values())
print("unique values",unique)
