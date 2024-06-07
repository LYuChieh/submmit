n=int(input("Input the total number of students (n>0): "))
s=list(range(1,n+1))
i=0
while len(s)>1:
    i=(i+2)%len(s)
    s.pop(i)
print(s[0])
    
