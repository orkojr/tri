

def triselect(p):
    for i in range(0,len(p)-1):
        pos = i
        for j in range(i+1,len(p)):
            if p[pos]>p[j]:
                pos = j
        p[i],p[pos] = p[pos],p[i]


p =[43,54,-433443,54,678,00,12,9]
triselect(p)
print(p)