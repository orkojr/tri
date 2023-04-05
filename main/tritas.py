def sommeG(node: int)->int:
    """fonction qui retourne le file gauche de node."""
    return node * 2 + 1


def sommeD(node: int)->int:
    """fonction qui retourne le file droit de node."""
    return node * 2 + 2

def pile_up_max(A:list , p:int,size:int):
    """fonction entasser max"""
    left = sommeG(p)
    right = sommeD(p)
    max_i = p
    if left <= size and A[left] >= A[max_i]:
        max_i = left
    if right <= size and A[right] >= A[max_i]:
        max_i = right
    if max_i != p :
        A[max_i],A[p] = A[p],A[max_i]
        pile_up_max(A,max_i,p)
def heapConstruction(A:list , size: int):
    """fonction de construction des tas max"""
    i = size // 2
    while i> -1:
        pile_up_max(A,i,size)
        i-=1

def heapsort(A:list,size:int):
    """fonction qui permet de creer les tas tries."""
    heapConstruction(A,size)
    i = size
    while i>0 :
        A[0],A[i] = A[i],A[0]
        size -=1
        pile_up_max(A,0,size)
        i-=1


p = [43,343,-1,0,4,10,-4]
heapsort(p,len(p)-1)
print(p)
