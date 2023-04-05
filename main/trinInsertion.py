def triInsertion(tab):
    i = 1
    
    while(i<=len(tab)-1):
        x = tab[i]
        j = i-1
        while(j>=0 and x< tab[j]):
            tab[j+1] = tab[j]
            j = j-1
        tab[j+1]=x
        i= i+1


#illustration

tab = [22,2,4,-34,2,6,78,33]
triInsertion(tab)
print(tab)
