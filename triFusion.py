

def triFusion(L):
    """ fonction permettant d'effectuer le tri par fusion d'une liste 
    prise en parametre.
    principe: on scinde une liste de n element en des des liste contenant
    chacune un element et en suite on fusionne les differente liste en rangeant
    les element dans l'ordre croissant"""
    n = len(L)
    if(n<2):
        return L
    else:
        m = n//2
        return fusion(triFusion(L[:m]),triFusion(L[m:]))


def fusion(t1,t2):
    i ,j,m,n = 0,0,len(t1),len(t2)
    t =[]
    while(i<m and j<n):
        if t1[i]<t2[j]:
            t.append(t1[i])
            i+=1
        else:
            t.append(t2[j])
            j+=1
    if i==m:
        t.extend(t2[j:])
    else :t.extend(t1[:i])
    return t


#illustration

p=[5,768,95,-5454,2,0,65]
r = triFusion(p)
print(r)