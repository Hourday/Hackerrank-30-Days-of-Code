# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
v=[]
for x in range(n):
    k=input()
    v.append(k.split(" "))
v=dict(v)
 
while True:
    try:
        i=input() 
        if i in v:
            print(i+"="+v.get(i))
        else:
            print ("Not found")
    except EOFError:
        break
    #except Exception:
     #   print ("Some exception occured")
