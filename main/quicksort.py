

def quicksort(L):
    def tri(l,r):
        if l<r:
            q=partition(L,l,r)
            tri(l,q)
            tri(q+1,r)
    tri(0,len(L))

def partition(l,g,r):
    p = g
    x = l[g]
    for k in range(g+1,r):
        if l[k] < x:
            p+=1
            l[p],l[k] = l[k],l[p]
    l[p],l[g] = l[g],l[p]
    return p

p = [44,5,-43,43,68,9]
quicksort(p)
print(p)