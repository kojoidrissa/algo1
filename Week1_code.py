#/anaconda/bin/python

##Merge Sort: Pseudocode
#What to do if the array isn't an even number of elements?
#If `len(list) % 2 != 0`, how to split into "halves"?

a = [x for x in range(0,9)]
#re-write above line for `a` of random length; test

a1 = a[:(len(a) //2)]
a2 = a[len(a1):]