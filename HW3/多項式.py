f=input("Input polynomial: ")
n=int(input("Input the value of x: "))
f=f.replace("-","+-").replace("-x","-1*x")
a=f.split("+")
if a.count("")>0:
    a.remove("")
else:
    a=f.split("+")
s=[]
i=0
while i<len(a):
    t=a[i].split("*")
    if len(t)==1:
        if t[0].find("^")==True:
            s.append(n**float(t[0].replace("x^",'').replace("x",str(n)).strip()))
        else:
            s.append(float(t[0].replace("x",str(n))))
    else:
        s.append(float(t[0].replace("x",str(n)))*(n**int(t[1].replace("x^","").replace("^x","1").replace("x","1").strip())))
    i=i+1
print(sum(s))


