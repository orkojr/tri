def partition(A,p,r):
    x= A[r]
    i = p-1
    for j in range(p,len(A)-1):
        if A[j] < x:
            i = i+1
            A[i],A[j] = A[j],A[i]
    A[i+1],A[r] = A[r],A[i+1]
    return i+1

def triRapide(A,p,r):
    if p<r :
        q = partition(A,p,r)
        triRapide(A,p,q-1)
        triRapide(A,q+1,r)

#implementation

p = [1,436,4,-2,56,23,4,0] 
triRapide(p,0,7)
print (p)
# permuter(p,2,1)
# print(p)
#for j in range(0,8):print(1)
