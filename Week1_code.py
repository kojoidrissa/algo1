#/anaconda/bin/python

##Merge Sort: Pseudocode
#What to do if the array isn't an even number of elements?
#If `len(list) % 2 != 0`, how to split into "halves"?

a = [x for x in range(0,9)]
#re-write above line for `a` of random length; test

a1 = a[:(len(a) //2)]
a2 = a[len(a1):]

#How to recursively sort a1 and a2? I need to figure that out

#Merging a1 and a2, AFTER they've been sorted
##How do I check to make sure I don't go past the end of the sub-arrays?
b =[] #output list; ultimate length = len(a)
i, j = 0, 0 #counters for a1 and a2
for k in len(a):
    if a1[i] < a2[j]:
        b[k] = a1[i]
        i += 1
    elif a2[j] < a1[i]:
        b[k] = a2[j]
        j += 1