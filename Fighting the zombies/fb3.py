def num_ways(faces, dices, sum,min,max):
    memo = [[0 for _ in range(max + 1)] for _ in range(dices + 1)]
    for face_value in range(1, faces + 1):
        if face_value <= max:
            memo[1][face_value] = 1
    for dice in range(2, dices + 1):
        for partial_sum in range(1, max + 1):
            for face_value in range(1, faces + 1):
                if face_value < partial_sum:
                    memo[dice][partial_sum] += memo[dice - 1][partial_sum - face_value]
    ans=0
    for i in range(min,max+1):
        if i>=0:
            ans+=memo[dices][i]
    return ans

def containsZ(spell):
    correctSpell=""
    z=0
    if "+" in spell:
        newspell=spell.split("+")
        correctSpell=newspell[0]
        z+=int(newspell[1])
    elif "-" in spell:
        newspell=spell.split("-")
        correctSpell=newspell[0]
        z-=int(newspell[1])
    else:
        correctSpell=spell
        z=0
    correctSpell=correctSpell.split("d")
    sides=int(correctSpell[1])
    times=int(correctSpell[0])
    return times,sides,z

import math
t=int(input())
for i in range(1,t+1):
    ip=raw_input().split()
    h=int(ip[0])
    s=int(ip[1])
    z=0
    maximum=0
    spells=raw_input().split()
    for spell in spells:
        arr=[]
        times,sides,z=containsZ(spell)
        min=h-z
        max=times*sides
        temp=float(num_ways(sides, times, sum,min,max))/(sides**times)
        if temp>maximum:
            maximum=temp
        v = "{:.6f}".format(round(maximum, 6))
    print "Case #%d: %s" % (i, v)