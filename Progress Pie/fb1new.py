import math
def distance(x,y):
	return math.sqrt(x*x+y*y)

input=open('input1.txt','r')
output=open('output1.txt','w')
n=int(input.readline().strip())
for i in range(0,n):
	l=map(int, input.readline().split())
	r=distance(l[1]-50,l[2]-50)
	#print r
	if r>50:
		#print i+1
		output.write('Case #'+str(i+1)+': white\n')
	else:
		p=l[0]*360.0/100
		at=math.degrees(math.atan2(l[2]-50,l[1]-50))
        print "at",at
        at=(90-at)%360
        if at <= p:
            output.write('Case #'+str(i+1)+': black\n')
        else:
            output.write('Case #'+str(i+1)+': white\n')