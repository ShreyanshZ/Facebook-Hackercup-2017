import math
t=int(input())
for i in range(1,t+1):
    n=int(input())
    berated=False
    turn=0
    arr=[]
    for k in range(0,n):
        arr.append(int(input()))
        arr.sort(reverse=True)
    while berated==False:
        k, count = (0,0)
        if arr[k]>=50:
            arr.pop(0)
        else:
            count=int(math.ceil(50.0/arr[k]))
            if count>len(arr):
                berated=True
                break
            else:
                arr.pop(0)
                for j in range(1,count):
                    arr.pop()
        if len(arr)==0:
            berated=True
        turn+=1
    print "Case #%d: %d" % (i, turn)