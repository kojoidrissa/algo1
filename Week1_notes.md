#Week 1 notes

##Merge Sort: Motivation and Example algorithm
###Why Analyze Merge Sort? 
-  Good intro to the Divide/Conquer paradigm
    +  Makes the rational for this paradigm very clear
    +  Improves over Selection, Insertion, Bubble sorts
-  Calibrate your level of prep. If you're comfortable with this, you're ready for the class. If not, do some background prep.
    +  I need to research Trees and another data structure
-  Highlights the guiding principles of algo analysis used in this class
    +  worst-case and asymptotic analysis
-  The analysis (recursion tree) generalizes to the "Master Method"

###How it works
-  Take an array(Python list), split it in 1/2
-  recursively sort each 1/2
-  combine the sorted 1/2s
    +  traverse them in parallel and put the results into a new, sorted array

##Merge Sort: Pseudocode
-  Base cases: if `0 <= len(list) <=1`, don't recurse
-  If `len(list) % 2 != 0`, how to split into "halves"?
    +  see [Week1_code.py](Week1_code.py) for solution
-  The "hard" part, merging the results of the sorted sub-arrays

##Merge Sort: Analysis
-  Use a Recursion Tree to analyze the claim that Merge sort will use `6n * log2n + 6n` steps to sort a list of n objects.
    +  There are log2n levels in the binary tree. Counting the root, this gives us (log2n + 1) levels
    +  The number of sub-problems at each level (j) is 2^j
    +  The size of each sub-problem (the 'n' for each) is n/2^j
    +  For each item in a sub-problem, 6 lines of code (or operations) need to be run
    +  So, work per level = sub-problems/level * work/sub-problem
        *  2^j * 6(n/2^j) ===> 6n, independent of level
    +  Thus, the total work = work per level * levels
        *  6n * (log2n + 1) ==> 6n * log2n + 6n

##Guiding Principles for Analysis of Algorithms
1.  Worst Case Analysis: The analysis is an UPPER bound on how long it will take the algorithm to run. It also has the benefit of being easier, mathematically.
    1. This is opposed to "Average Case Analysis", which uses assumptions about the frequency of various input types, or "Benchmarks", where you agree up front on certain typical inputs. These both require domain knowledge.
2. We won't worry much about small constant factors or lower-order terms. Why?
    4. Easier mathematically
    5. constants depend on the implementation language and method
    3. We'll lose very little predictive power by using the 2nd principle.
3. Asymptotic analysis: focus on large input sizes (as n tends towards infinity)
    4. justification: we focus on large n-values because those are the only problems where speed and performance matter. If you're only sorting 10 or 100 items, it doesn't really matter. However, as computers get faster, the data we want to analyze gets **larger**.
    5. This also allows your problem-solving power to grow linearly with computer power.

###Fast Algorithm definition
An algorithm who's worst-case running time grows slowly with input size.  The 'sweet spot' provides mathematical tractability AND predictive power.

