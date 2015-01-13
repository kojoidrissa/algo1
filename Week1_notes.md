#Week 1 notes

##Merge Sort: Motivation and Example algorithm
###Why Analyze Merge Sort? 
-  Good intro to the Divide/Conquer paradigm
    +  Makes the rational for this paradigm very clear
    +  Improves over Selection, Insertion, Bubble sorts
-  Calibrate your level of prep. If you're comfortable with this, you're ready for the class. If not, do some background prep.
-  Highlights the guiding principles of algo analysis used in this class
    +  worst-case and asymptotic analysis
-  The analysis (recursion tree) generalizes to the "Master Method"

###How it works
-  Take an array(Python list), split it in 1/2
-  recursively sort each 1/2
-  combine the sorted 1/2s

##Merge Sort: Pseudocode
-  Base cases: if `0 <= len(list) <=1`, don't recurse
-  If `len(list) % 2 != 0`, how to split into "halves"?
    +  `a = [0, 1, 2, 3, 4, 5, 6, 7, 8]`
    +  `a1 = a[:(len(a) //2)]`
    +  `a2 = a[len(a1):]`
