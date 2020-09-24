# Enter your code here. Read input from STDIN. Print output to STDOUT
j=int(input())
l=[]
strl=""
n=j
#for x in range(n):
#   name=str(input())
                    #  l.append(name) #takes name as input //testcase
#print(l)          #prints name list
#print(n)          #no. of test cases
while(n!=0):
    name=str(input())
    l.append(name)
    n=n-1

for x in range(len(l)):
    strl="".join(l[x])
    var1="" 
    var2=""
    for i in range(len(strl)):
        if i%2==0:
            #print("even",strl[i],end=" ")
            var1=var1+strl[i]
        else:
            #print("odd",strl[i])
            var2=var2+strl[i]
    print(var1,end=" ")
    print(var2)







