# Algorithms and Complexity Analysis

## Introduction to Algorithms

An algorithm is a well-defined computational procedure that takes input and produces output. It's a sequence of steps that transform input into output to solve a computational problem.

**Properties of Good Algorithms:**
- **Correctness**: Produces correct output for all valid inputs
- **Efficiency**: Uses minimal time and space resources
- **Clarity**: Easy to understand and implement
- **Generality**: Solves a class of problems, not just specific instances

## Algorithm Design Paradigms

### Brute Force
- Try all possible solutions
- Guaranteed to find answer if one exists
- Often inefficient but simple to implement
- Useful as baseline for comparison

### Divide and Conquer
- Break problem into smaller subproblems
- Solve subproblems recursively
- Combine solutions to solve original problem
- Examples: Merge sort, quick sort, binary search

### Greedy Algorithms
- Make locally optimal choice at each step
- Hope to find global optimum
- Fast but doesn't always give optimal solution
- Examples: Dijkstra's algorithm, Huffman coding

### Dynamic Programming
- Break problem into overlapping subproblems
- Store solutions to subproblems (memoization)
- Build up to solution of original problem
- Examples: Fibonacci, knapsack problem, shortest path

### Backtracking
- Build solution incrementally
- Abandon solution if it cannot lead to valid result
- Systematically explore all possibilities
- Examples: N-Queens, Sudoku solver, maze solving

## Asymptotic Notation (Big-O Analysis)

### Why Asymptotic Analysis?

We analyze algorithms to:
1. Predict performance as input size grows
2. Compare algorithms independently of hardware
3. Identify bottlenecks
4. Choose the best algorithm for the problem

### Big-O Notation (O)

**Definition**: Upper bound on growth rate - worst case scenario.

f(n) = O(g(n)) means f(n) grows no faster than g(n) for large n.

**Common Time Complexities (from best to worst):**

1. **O(1) - Constant**
   - Performance doesn't depend on input size
   - Examples: Array access, hash table lookup (average), arithmetic operations
   - `result = array[5]`

2. **O(log n) - Logarithmic**
   - Halves the problem size each step
   - Very efficient for large inputs
   - Examples: Binary search, balanced tree operations
   - `while n > 1: n = n // 2`

3. **O(n) - Linear**
   - Performance grows linearly with input size
   - Examples: Linear search, iterating through array, finding min/max
   - `for i in range(n): process(i)`

4. **O(n log n) - Linearithmic**
   - Efficient sorting algorithms
   - Examples: Merge sort, heap sort, quicksort (average)
   - Divide-and-conquer with linear merge

5. **O(n²) - Quadratic**
   - Nested loops over input
   - Examples: Bubble sort, insertion sort, selection sort
   - Simple but inefficient for large inputs
   - `for i in range(n): for j in range(n): process(i,j)`

6. **O(n³) - Cubic**
   - Triple nested loops
   - Example: Naive matrix multiplication
   - `for i: for j: for k: ...`

7. **O(2ⁿ) - Exponential**
   - Doubles with each additional input
   - Quickly becomes infeasible
   - Examples: Recursive fibonacci (naive), subset generation
   - `fib(n) = fib(n-1) + fib(n-2)`

8. **O(n!) - Factorial**
   - Extremely slow
   - Example: Generating all permutations
   - Only feasible for very small inputs (n < 15)

### Big-Omega Notation (Ω)

**Definition**: Lower bound on growth rate - best case scenario.

f(n) = Ω(g(n)) means f(n) grows at least as fast as g(n).

### Big-Theta Notation (Θ)

**Definition**: Tight bound - both upper and lower bound.

f(n) = Θ(g(n)) means f(n) grows at the same rate as g(n).

When Big-O and Big-Omega are the same, we have Θ.

### Rules for Analyzing Complexity

1. **Drop constants**: O(3n) → O(n)
2. **Drop lower-order terms**: O(n² + n) → O(n²)
3. **Different inputs use different variables**: O(n + m), not O(n)
4. **Nested loops multiply**: O(n) * O(m) = O(n*m)
5. **Sequential loops add**: O(n) + O(m) = O(n + m)
6. **Log of any base is O(log n)**: Different bases differ by constant factor

### Analyzing Loops

**Single Loop:**
```
for i in range(n):
    # O(1) operation
Total: O(n)
```

**Nested Loops:**
```
for i in range(n):
    for j in range(n):
        # O(1) operation
Total: O(n²)
```

**Dependent Loops:**
```
for i in range(n):
    for j in range(i):
        # O(1) operation
Total: O(n²)  # (n)(n-1)/2 = O(n²)
```

**Logarithmic Loops:**
```
i = n
while i > 1:
    i = i // 2
Total: O(log n)
```

## Space Complexity

Space complexity measures memory usage as function of input size.

**Components:**
1. **Auxiliary space**: Extra space used by algorithm
2. **Input space**: Space for storing input data

**Examples:**
- O(1): Fixed number of variables
- O(n): Single array of size n
- O(n²): 2D array of size n×n
- O(log n): Recursive call stack for binary search
- O(n): Recursive call stack for linear recursion

**Space-Time Tradeoff:**
- Can often trade space for time (memoization)
- Or time for space (recomputation vs. storage)

## Searching Algorithms

### Linear Search

**Algorithm:**
```
for each element in array:
    if element equals target:
        return index
return not found
```

**Complexity:**
- Time: O(n) worst case, O(1) best case
- Space: O(1)

**Use Case:**
- Unsorted data
- Small datasets
- When simplicity matters

### Binary Search

**Precondition**: Array must be sorted

**Algorithm:**
```
1. Set low = 0, high = n-1
2. While low <= high:
   - mid = (low + high) // 2
   - If array[mid] == target: return mid
   - If array[mid] < target: low = mid + 1
   - Else: high = mid - 1
3. Return not found
```

**Complexity:**
- Time: O(log n)
- Space: O(1) iterative, O(log n) recursive

**Key Insight**: Eliminates half of remaining elements each step

**Applications:**
- Searching in sorted arrays
- Finding insertion point
- Optimizing problems with monotonic property

## Sorting Algorithms

### Bubble Sort

**Algorithm:**
```
Repeatedly step through list:
    Compare adjacent elements
    Swap if in wrong order
Continue until no swaps needed
```

**Complexity:**
- Time: O(n²) average and worst, O(n) best (already sorted)
- Space: O(1)

**Characteristics:**
- Simple but inefficient
- Stable: Preserves relative order of equal elements
- Adaptive: Performs better on nearly sorted data

### Selection Sort

**Algorithm:**
```
For each position i from 0 to n-1:
    Find minimum element in unsorted portion
    Swap with element at position i
```

**Complexity:**
- Time: O(n²) always - even if sorted
- Space: O(1)

**Characteristics:**
- Minimizes number of swaps
- Not adaptive
- Not stable (standard implementation)

### Insertion Sort

**Algorithm:**
```
For each element from position 1 to n-1:
    Compare with elements to the left
    Shift larger elements right
    Insert element in correct position
```

**Complexity:**
- Time: O(n²) worst/average, O(n) best case
- Space: O(1)

**Characteristics:**
- Efficient for small datasets
- Very efficient for nearly sorted data
- Stable
- Online: Can sort list as it receives it
- Used in practice for small subarrays in hybrid algorithms

### Merge Sort

**Algorithm (Divide and Conquer):**
```
1. Divide array into two halves
2. Recursively sort each half
3. Merge sorted halves
```

**Complexity:**
- Time: O(n log n) always
- Space: O(n) - requires auxiliary array

**Characteristics:**
- Stable
- Not in-place (requires extra space)
- Predictable performance
- Good for linked lists
- Used in external sorting

**Recurrence**: T(n) = 2T(n/2) + O(n)

### Quick Sort

**Algorithm:**
```
1. Choose pivot element
2. Partition: elements < pivot on left, >= pivot on right
3. Recursively sort left and right partitions
```

**Complexity:**
- Time: O(n log n) average, O(n²) worst case
- Space: O(log n) stack space

**Characteristics:**
- In-place (mostly)
- Not stable (standard implementation)
- Cache efficient
- Fast in practice
- Worst case occurs with poor pivot selection (already sorted)

**Pivot Selection Strategies:**
- First/last element (simple, bad for sorted data)
- Random element (good average case)
- Median-of-three (better in practice)

### Heap Sort

**Algorithm:**
```
1. Build max heap from array
2. Repeatedly:
   - Swap root with last element
   - Reduce heap size
   - Heapify root
```

**Complexity:**
- Time: O(n log n) always
- Space: O(1)

**Characteristics:**
- In-place
- Not stable
- Predictable performance
- Used in priority queues

### Comparison of Sorting Algorithms

| Algorithm | Best | Average | Worst | Space | Stable |
|-----------|------|---------|-------|-------|--------|
| Bubble | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Selection | O(n²) | O(n²) | O(n²) | O(1) | No |
| Insertion | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Merge | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Quick | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| Heap | O(n log n) | O(n log n) | O(n log n) | O(1) | No |

## Recursion

**Definition**: A function that calls itself, with a base case to stop recursion.

**Components:**
1. **Base case**: Condition where recursion stops
2. **Recursive case**: Function calls itself with modified input
3. **Progress toward base case**: Each call must move closer to base case

### Example: Factorial
```
factorial(n):
    if n <= 1:           # Base case
        return 1
    return n * factorial(n-1)  # Recursive case
```

### Example: Fibonacci
```
fibonacci(n):
    if n <= 1:           # Base case
        return n
    return fibonacci(n-1) + fibonacci(n-2)  # Recursive case
```

### Recursion vs. Iteration

**Recursion Advantages:**
- Elegant and intuitive for certain problems
- Natural for tree/graph traversal
- Simplifies divide-and-conquer algorithms

**Recursion Disadvantages:**
- Function call overhead
- Stack space usage
- Risk of stack overflow
- Can be less efficient (without memoization)

**When to Use:**
- Tree/graph problems
- Divide-and-conquer algorithms
- Backtracking problems
- When recursion makes solution clearer

### Tail Recursion

**Definition**: Recursive call is the last operation in function.

Some compilers optimize tail recursion to iteration (tail call optimization).

```
# Tail recursive
factorial_tail(n, accumulator=1):
    if n <= 1:
        return accumulator
    return factorial_tail(n-1, n * accumulator)

# Not tail recursive
factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)  # Multiplication after call
```

## Master Theorem

For divide-and-conquer recurrences of the form:
T(n) = aT(n/b) + f(n)

Where:
- a = number of subproblems
- n/b = size of each subproblem
- f(n) = cost of dividing and combining

**Three Cases:**

1. If f(n) = O(n^c) where c < log_b(a):
   - T(n) = Θ(n^(log_b(a)))

2. If f(n) = Θ(n^c) where c = log_b(a):
   - T(n) = Θ(n^c log n)

3. If f(n) = Ω(n^c) where c > log_b(a):
   - T(n) = Θ(f(n))

**Example: Merge Sort**
- T(n) = 2T(n/2) + O(n)
- a=2, b=2, f(n)=n
- log_2(2) = 1, so c=1 equals log_b(a)
- Case 2: T(n) = Θ(n log n)

## Problem-Solving Strategies

1. **Understand the problem**
   - What are inputs and outputs?
   - What are constraints?
   - What are edge cases?

2. **Choose appropriate data structure**
   - Match structure to access patterns
   - Consider time-space tradeoffs

3. **Design algorithm**
   - Start with brute force
   - Optimize using design paradigms
   - Consider similar problems solved before

4. **Analyze complexity**
   - Identify loops and recursion
   - Calculate time and space complexity
   - Verify with test cases

5. **Implement and test**
   - Start with simple cases
   - Test edge cases
   - Optimize after correctness confirmed

6. **Optimize if needed**
   - Profile to find bottlenecks
   - Consider algorithmic improvements
   - Balance readability and performance
