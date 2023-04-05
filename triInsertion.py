"""ce module permet de faire le tri insertion d'une liste prise en parametre """


def triInsert(L):
    """le principe du tri par insertion est tres simple.
    il scinde un tableau en deux parties: une triee et l'autre non triee. et
    prend chaque element de la partie non triee pour le mettre a sa place dans la partie trie"""
    
    for i in range(1,len(L)):
        x = L[i]
        j = i-1
        while(j>-1 and x<=L[j]):
            L[j+1]=L[j]
            j-=1
        L[j+1]=x

#illustration 

p=[222,4,1,56,8,6-5665,87,0]
triInsert(p)
print(p)