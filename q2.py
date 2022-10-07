def SelectionSort(slist):
    l = len(slist)
    for k in range(l):
        mini = k
        for j in range(k + 1, l):
            if slist[mini] > slist[j]:
                mini = j
        if mini != k :
            temp = slist[k]
            slist[k] = slist[mini]
            slist[mini] = temp
    return slist

slist1 = [9,2,6,4,7]

print("Proir to selection sort: ", slist1)
print("After selection sort: ", SelectionSort(slist1))
