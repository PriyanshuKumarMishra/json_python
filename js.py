from io import open_code
import json
a={"Name":"Ram","Class":"IV","Age":9}
b=open('kij.json','w')
json.dump(a,b)
b=open('kij.json')
c=json.load(b)
for i in c.items():
    print(i)
# Q.1 Json data ko python object main convert karne ka program likho?.
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
a={"name": "David","class":"I","age": 6}
b=json.dumps(a)
print(type(b))
# Q.2 Python object ko json data main convert karne ka program likho?
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
a=input()
b=json.dumps(a)
print(type(b))
# Q.3 Python object ko json string mai convert karne ka program likho?
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
d = {'4': 5,'6': 7,'1': 3,'2': 4}
sd= sorted(d.items())
d.clear()
for k,v in sd:
    d[k]=v
b=json.dumps(d)
print(type(b))
# Q4.Python dictionary(sort by key) object ko json data ::mai convert karne ka program likho?
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
a=open('kij.json')
b=json.load(a)
c=0
for i,k in b.items():
    c=1
    if type(i)!=str and type(i)!=int or type(k)!=str and type(k)!=int:
        print('it is containing complex data')
        break
    else:
        c=0
if c==0:
    print('naah its normal')
# Q5.Json string ko check karo ki bo complex object contain karti hai ya nahi?    
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
a='{"a":  1,"a":  2,"a":  3,"a": 4,"b": 1,"b": 2}'
d=json.loads(a)
print(d['a'],d['b'])
# Q6.Python object key unique key value ko access karne ka program likho?
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
a=open('TEXT_FILE.txt','r')
d={}
for i,k in enumerate(a):
    g=k.split()
    b=g[0]
    g.remove(g[0])
    f=''
    for i in g:
        f+=i
        f+=' '
    d[b]=f
z=open('kij.json','w')
json.dump(d,z)
# Q7.Text file data ko json file data mai convert karo,jaise ki neeche diya hai?
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
a=[["neelam","programer","24","2400"],["komal","trainer","24","20000"],["anuradha","HR","25","40000"],["Abhishek","manager","29","63000"]]
b=['Name','Designation','Age','Salary']
d={}
c=1
for i in a:
    e={}
    for j,s in zip(i,b):
        e[s]=j
    ep='emp'+str(c)
    d[ep]=e
    c+=1
z=open('kij.json','w')
json.dump(d,z)
# Q8.Tumhare pass four employes ki details hai list mai:- ab aapko 4 dictionaries create karni hai jaise ki emp1 emp2 emp3 and emp4. har ek employee ka dictionary main name,designation,age and salary honi chahiye. aur ye sab dictionary ki keys hai jismai maine list main value di hai. Iska use kar ke aapko ek json file create karni hai? Jaise ki niche diya hai. 
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::
