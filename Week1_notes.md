#Week 1 notes

##Ideas I need to review or get familiar with
-  Data structures
    +  Trees, especially Binary Trees
    +  Heaps
    +  Hash Tables
-  Math: I've got [Mathematics for Computer Science](mathcs.pdf), which the instructor recommended.

##Merge Sort: Motivation and Example algorithm
###Why Analyze Merge Sort? 
-  Good intro to the Divide/Conquer paradigm
    +  Makes the rational for this paradigm very clear
    +  Improves over Selection, Insertion, Bubble sorts
-  Calibrate your level of prep. If you're comfortable with this, you're ready for the class. If not, do some background prep.
    +  See `Ideas I need to review or get familiar with` above.
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

##Asymptotic Analysis: The Gist
###Why?
- Vocab for the design and analysis of algorithmic performance
    + Programs run in O(n) time; "Big O" notation
- Suppress constant factors and lower-order terms **KEY 7 WORDS!!**
    + leading constant factors: HIGHLY dependent on the implementation environment; too much granularity for us
    + lower order terms: become less relevant as `n` approaches `Infinity`, which are the interesting problems
- Example: Merge Sort
    + Run time is 6n * log2n + 6n
    + dropping LCF (the first 6) and lower order term (final 6n) ==> nlog<sub>2</sub>n
    + ==> running time is O(nlog<sub>2</sub>n) (Big O of n logn)
- Example: Single Loop
    + Is an integer, `t` contained in an Array, `A`?
    + Go through list, checking if `t == A[i]`
        * If so, return `True`, else `False`
    + Running time: O(n)
- Example: Two Loops in Sequence
    + Given Arrays `A` & `B` and integer `t`, is `t` in either array?
        + Loop through A
        + Loop through B
        + Return False if not found
    - Running time: O(n); would be 2n, but the LdCF is dropped
* Example: Two Nested Loops
    - Do arrays A & B have a number in common?
    - Running time: O(n<sup>2</sup>)
* Example: Two Nested Loops II
    - is there a duplicate in Array A?
    - i = counter for A; j = i+1
    - For i in A
        - For j in A
            - Compare A[i] to A[j]
    + Running time: O(n<sup>2</sup>); Really n<sup>2</sup>/2, but the LdCF (.5) gets dropped

##Big O Notation
A mathematical proof was shown. Which basically highlighted my diminished math skills. :-(

##Basic Examples
I'm going to have to look at the typed/printed notes. This guy's handwriting is almost IMPOSSIBLE to read.
