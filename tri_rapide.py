
def triRapide(L):
    def tri(g,d):
        if g<d:
            p = partition(L,g,d)
            tri(g,p)
            tri(p+1,d)
    tri(0,len(L))

def partition(L,g,d):
    p =g
    x = L[g]
    for k in range(g+1,d):
        if L[k]<x:
            p+=1
            L[p],L[k] = L[k],L[p]
    L[p],L[g] = L[g],L[p]
    return p

#illustration

p=[4,5665,76,0,-233234,65,7,8,5656]
triRapide(p)
print(p)
   
 