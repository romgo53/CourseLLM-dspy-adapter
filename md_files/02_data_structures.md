# Data Structures

## Introduction

A data structure is a way of organizing and storing data to enable efficient access and modification. The choice of data structure significantly impacts program performance and complexity.

## Abstract Data Types (ADT)

An ADT is a mathematical model that defines:
- A set of values
- A set of operations on those values
- The behavior of those operations

ADTs specify **what** operations do, not **how** they are implemented.

## Arrays and Lists

### Arrays

**Definition**: A collection of elements of the same type stored in contiguous memory locations.

**Characteristics:**
- Fixed size (in many languages)
- Random access: O(1) time to access any element
- Memory efficient: No overhead per element
- Index-based: Elements accessed by position (0-indexed typically)

**Operations:**
- Access: O(1)
- Search: O(n) for unsorted, O(log n) for sorted (binary search)
- Insertion: O(n) - may require shifting elements
- Deletion: O(n) - may require shifting elements

**Use Cases:**
- When size is known in advance
- When frequent random access is needed
- When memory efficiency is critical

### Dynamic Arrays (Lists)

**Definition**: Arrays that can grow or shrink in size dynamically.

**How They Work:**
- Start with initial capacity
- When full, allocate larger array (typically 2x size)
- Copy elements to new array
- Amortized O(1) insertion at end

**Python Lists:**
- Heterogeneous: Can store different types
- Dynamic sizing
- Built-in methods: append, insert, remove, pop, sort, etc.

**Common Operations:**
- append(): Add element to end - O(1) amortized
- insert(i, x): Insert at position - O(n)
- remove(x): Remove first occurrence - O(n)
- pop(): Remove last element - O(1)
- pop(i): Remove at position - O(n)
- index(x): Find position of element - O(n)

### Multi-dimensional Arrays

**Definition**: Arrays of arrays, creating matrices or higher-dimensional structures.

**2D Arrays (Matrices):**
- Accessed with two indices: array[row][column]
- Row-major vs. column-major order
- Used for grids, tables, images, graphs

## Strings

**Definition**: Sequences of characters, often implemented as arrays of characters.

**Immutability:**
- In many languages (Python, Java), strings are immutable
- Operations create new strings rather than modifying existing ones
- Efficiency consideration: Use StringBuilder/StringBuffer for many modifications

**Common Operations:**
- Concatenation: Joining strings
- Substring: Extracting portion of string
- Search: Finding character or substring
- Replace: Substituting characters or substrings
- Split: Breaking string into parts
- Case conversion: Upper/lower case

**String Complexity:**
- Access: O(1)
- Concatenation: O(n) for immutable strings
- Substring: O(k) where k is length of substring
- Search: O(n*m) naive, O(n+m) with KMP algorithm

## Tuples

**Definition**: Immutable ordered collections of elements (often heterogeneous).

**Characteristics:**
- Cannot be modified after creation
- Can contain different data types
- Hashable (can be dictionary keys)
- More memory efficient than lists

**Use Cases:**
- Fixed collections of related values
- Function return values (multiple values)
- Dictionary keys
- When immutability is desired for safety

## Stacks

**Definition**: Last-In-First-Out (LIFO) data structure.

**Core Operations:**
- **push(item)**: Add item to top - O(1)
- **pop()**: Remove and return top item - O(1)
- **peek()**: View top item without removing - O(1)
- **isEmpty()**: Check if stack is empty - O(1)

**Implementation:**
- Array-based: Fixed or dynamic size
- Linked list-based: Dynamic size, no waste

**Applications:**
- Function call stack (recursion)
- Expression evaluation and conversion
- Undo mechanisms
- Backtracking algorithms
- Bracket matching
- Depth-First Search (DFS)

**Example: Balanced Parentheses**
```
Algorithm:
1. For each character in expression:
   - If opening bracket: push to stack
   - If closing bracket: 
     - If stack empty: unbalanced
     - Pop from stack and check if matches
2. After processing all: stack should be empty
```

## Queues

**Definition**: First-In-First-Out (FIFO) data structure.

**Core Operations:**
- **enqueue(item)**: Add item to rear - O(1)
- **dequeue()**: Remove and return front item - O(1)
- **front()**: View front item without removing - O(1)
- **isEmpty()**: Check if queue is empty - O(1)

**Implementation:**
- Array-based: Circular buffer to avoid waste
- Linked list-based: Dynamic size, efficient

**Applications:**
- Breadth-First Search (BFS)
- Job scheduling
- Print queue
- Buffer for data streams
- Level-order tree traversal

**Circular Queue:**
- Uses modulo arithmetic to wrap around
- Efficient use of fixed-size array
- Front and rear pointers

## Priority Queues

**Definition**: Queue where elements have priorities, highest priority element dequeued first.

**Operations:**
- **insert(item, priority)**: Add with priority - O(log n)
- **extractMax()/extractMin()**: Remove highest/lowest priority - O(log n)
- **peek()**: View highest priority item - O(1)

**Implementation:**
- Heap (most efficient): Binary heap, Fibonacci heap
- Sorted array: O(n) insertion, O(1) extraction
- Unsorted array: O(1) insertion, O(n) extraction

**Applications:**
- Dijkstra's shortest path algorithm
- Huffman coding
- Task scheduling with priorities
- Event-driven simulation
- A* pathfinding algorithm

## Dictionaries (Hash Tables/Maps)

**Definition**: Data structure storing key-value pairs with fast lookup.

**Characteristics:**
- Keys must be unique
- Keys must be hashable (immutable types)
- Unordered (in most implementations)
- Average O(1) for insert, delete, lookup

**Hash Function:**
- Maps keys to array indices
- Should distribute keys uniformly
- Deterministic: Same key always gives same hash

**Collision Handling:**

1. **Chaining:**
   - Each slot contains linked list
   - Multiple keys with same hash stored in list
   - Simple but can degrade to O(n)

2. **Open Addressing:**
   - Find next available slot
   - Linear probing, quadratic probing, double hashing
   - Better cache performance

**Load Factor:**
- Ratio of entries to table size
- When too high, resize and rehash
- Trade-off between space and time

**Applications:**
- Database indexing
- Caches (memoization)
- Symbol tables in compilers
- Counting frequencies
- Detecting duplicates

## Sets

**Definition**: Unordered collection of unique elements.

**Operations:**
- **add(item)**: Insert element - O(1) average
- **remove(item)**: Delete element - O(1) average
- **contains(item)**: Check membership - O(1) average
- **union**: Combine two sets
- **intersection**: Common elements
- **difference**: Elements in first but not second
- **isSubset**: Check if subset relationship

**Implementation:**
- Hash-based: Fast operations
- Tree-based: Ordered, O(log n) operations

**Applications:**
- Removing duplicates
- Membership testing
- Mathematical set operations
- Graph algorithms (visited nodes)

## Linked Lists

**Definition**: Linear data structure where elements (nodes) are not stored contiguously but linked via pointers.

**Node Structure:**
- Data field(s)
- Pointer to next node (singly linked)
- Pointer to previous node (doubly linked)

**Types:**

1. **Singly Linked List:**
   - Each node points to next
   - Can only traverse forward
   - Less memory overhead

2. **Doubly Linked List:**
   - Each node points to next and previous
   - Can traverse both directions
   - Easier deletion
   - More memory overhead

3. **Circular Linked List:**
   - Last node points to first
   - No null pointers
   - Useful for round-robin scheduling

**Operations:**
- **Insertion at beginning**: O(1)
- **Insertion at end**: O(n) singly, O(1) doubly with tail pointer
- **Insertion in middle**: O(n)
- **Deletion at beginning**: O(1)
- **Deletion in middle/end**: O(n)
- **Search**: O(n)
- **Access by index**: O(n)

**Advantages:**
- Dynamic size
- Efficient insertion/deletion (once position found)
- No memory waste

**Disadvantages:**
- No random access
- Extra memory for pointers
- Poor cache locality

**Applications:**
- Implementation of stacks and queues
- Music playlists
- Browser history (forward/back)
- Undo/redo functionality

## Comparison: Arrays vs. Linked Lists

| Feature | Array | Linked List |
|---------|-------|-------------|
| Access | O(1) | O(n) |
| Search | O(n) | O(n) |
| Insertion (start) | O(n) | O(1) |
| Insertion (end) | O(1)* | O(n)/O(1)** |
| Deletion (start) | O(n) | O(1) |
| Memory | Contiguous, may waste space | Non-contiguous, extra for pointers |
| Size | Fixed/grows by copying | Dynamic |

*Amortized for dynamic arrays  
**O(1) with tail pointer

## Space-Time Tradeoffs

Different data structures offer different trade-offs:

- **Arrays**: Fast access, slow insertion/deletion
- **Linked Lists**: Slow access, fast insertion/deletion (at known position)
- **Hash Tables**: Fast everything (average), more memory
- **Trees**: Balanced performance, ordered data

Choosing the right data structure depends on:
1. Most frequent operations
2. Data size
3. Memory constraints
4. Whether data needs to be ordered
5. Performance requirements

## Best Practices

1. **Choose appropriate structure**: Match structure to access patterns
2. **Consider memory**: Some structures have overhead
3. **Think about growth**: Will data size change?
4. **Benchmark**: Test with realistic data and operations
5. **Know your language**: Understand built-in implementations
6. **Complexity matters**: Understand big-O for your use case
