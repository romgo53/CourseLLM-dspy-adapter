# Hierarchical Data Structures and Efficient Organization

## Introduction to Hierarchical Models

### The Natural Hierarchy

Many systems exhibit hierarchical relationships where each element has a parent-child relationship:

- **File systems**: Folders contain files and other folders
- **Organization charts**: Managers and employees
- **Family trees**: Ancestors and descendants
- **Document structure**: Sections, subsections, paragraphs
- **Expression evaluation**: Mathematical operations and operands
- **Decision making**: Branching choices

These relationships naturally form tree-like structures.

## Tree Fundamentals

### Definition

A tree is a hierarchical data structure consisting of nodes connected by edges, with the following properties:

1. **One root**: Exactly one node has no parent (the top)
2. **Unique path**: Exactly one path exists between any two nodes
3. **Acyclic**: No cycles exist
4. **Connected**: All nodes are reachable from root

### Terminology

**Node:** Basic unit containing data and references to children

**Root:** The topmost node with no parent

**Leaf (External Node):** Node with no children

**Internal Node:** Node with at least one child

**Parent:** Node directly above another node

**Child:** Node directly below another node

**Siblings:** Nodes sharing the same parent

**Ancestor:** Any node on the path from a node to root

**Descendant:** Any node in the subtree rooted at a node

**Subtree:** A node and all its descendants

**Edge:** Connection between parent and child

**Path:** Sequence of nodes connected by edges

**Level/Depth of Node:** Number of edges from root to node (root is at level 0)

**Height of Node:** Number of edges on longest path from node to a leaf

**Height of Tree:** Height of root = maximum depth of any node

**Degree of Node:** Number of children

### Example Tree

```
           A (root, level 0, height 3)
          / \
         B   C (level 1, height 2)
        /|   |\
       D E   F G (level 2, height 1)
      /
     H (leaf, level 3, height 0)

Properties:
- Root: A
- Leaves: E, F, G, H
- Internal nodes: A, B, C, D
- Parent of D: B
- Children of B: D, E
- Siblings: D and E, F and G
- Ancestors of H: D, B, A
- Height: 3
- Size (number of nodes): 8
```

## Binary Trees

### Definition

A binary tree is a tree where each node has **at most two children**, typically called left and right.

**Properties:**
- Each node has 0, 1, or 2 children
- Children are distinguished as left and right
- Order matters: left ≠ right

### Node Structure

```
Structure: TreeNode
    data: value stored in node
    left: reference to left child (or null)
    right: reference to right child (or null)
```

### Types of Binary Trees

**Full Binary Tree:**
- Every node has either 0 or 2 children
- No node has exactly 1 child

```
       A
      / \
     B   C
    / \
   D   E
```

**Complete Binary Tree:**
- All levels completely filled except possibly the last
- Last level filled from left to right
- Used in heap implementations

```
       A
      / \
     B   C
    / \ /
   D  E F
```

**Perfect Binary Tree:**
- All internal nodes have 2 children
- All leaves at same level
- Number of nodes: 2^(h+1) - 1 where h is height

```
       A
      / \
     B   C
    / \ / \
   D  E F  G
```

**Degenerate (Skewed) Tree:**
- Each parent has only one child
- Essentially a linked list
- Worst-case for many tree operations

```
A
 \
  B
   \
    C
     \
      D
```

### Mathematical Properties

For a binary tree with n nodes:

**Minimum height:** ⌊log₂(n)⌋ (perfect tree)

**Maximum height:** n - 1 (skewed tree)

**Maximum nodes at level i:** 2^i

**Maximum nodes in tree of height h:** 2^(h+1) - 1

**For complete binary tree:**
- If parent at index i, left child at 2i+1, right child at 2i+2
- If child at index i, parent at ⌊(i-1)/2⌋

## Tree Traversal Methods

### Depth-First Traversals

These traversals explore depth before breadth, differing in when they process the current node relative to its children.

#### In-Order Traversal (Left-Root-Right)

```
InOrder(node):
    if node is not null:
        InOrder(node.left)
        Process node.data
        InOrder(node.right)
```

**Example:**
```
       A
      / \
     B   C
    / \
   D   E

In-order: D, B, E, A, C
```

**Special Property:** For binary search trees, in-order traversal visits nodes in sorted order!

**Use Cases:**
- Getting sorted sequence from BST
- Expression trees (gives infix notation)

#### Pre-Order Traversal (Root-Left-Right)

```
PreOrder(node):
    if node is not null:
        Process node.data
        PreOrder(node.left)
        PreOrder(node.right)
```

**Example:**
```
       A
      / \
     B   C
    / \
   D   E

Pre-order: A, B, D, E, C
```

**Use Cases:**
- Copying trees
- Prefix expressions
- Creating tree from representation
- File system traversal (process directory before contents)

#### Post-Order Traversal (Left-Right-Root)

```
PostOrder(node):
    if node is not null:
        PostOrder(node.left)
        PostOrder(node.right)
        Process node.data
```

**Example:**
```
       A
      / \
     B   C
    / \
   D   E

Post-order: D, E, B, C, A
```

**Use Cases:**
- Deleting trees (delete children before parent)
- Postfix expressions
- Computing directory sizes (process contents before directory)

### Breadth-First Traversal (Level-Order)

Visits nodes level by level, from left to right.

```
LevelOrder(root):
    if root is null:
        return
    
    Create queue Q
    Q.enqueue(root)
    
    while Q is not empty:
        node = Q.dequeue()
        Process node.data
        
        if node.left is not null:
            Q.enqueue(node.left)
        if node.right is not null:
            Q.enqueue(node.right)
```

**Example:**
```
       A
      / \
     B   C
    / \
   D   E

Level-order: A, B, C, D, E
```

**Use Cases:**
- Finding nodes at specific level
- Shortest path in unweighted trees
- Level-wise processing

## Binary Search Trees (BST)

### The Ordering Property

A binary search tree is a binary tree with a special ordering property that enables efficient searching:

**BST Property:** For every node:
- All nodes in left subtree have values **less than** node's value
- All nodes in right subtree have values **greater than** node's value

This property holds for **every** node in the tree, not just the root.

### Example BST

```
         50
        /  \
      30    70
     /  \   / \
   20  40 60  80

Properties:
- 20, 30, 40 < 50 < 60, 70, 80 ✓
- 20 < 30 < 40 ✓
- 60 < 70 < 80 ✓
```

**Not a BST:**
```
         50
        /  \
      30    70
     /  \   / \
   20  55 60  80
      ↑
     Problem! 55 > 50 but in left subtree
```

### Search Operation

The BST property enables efficient search:

```
Search(node, target):
    if node is null:
        return null (not found)
    
    if target == node.data:
        return node (found!)
    
    if target < node.data:
        return Search(node.left, target)  // Search left
    else:
        return Search(node.right, target) // Search right
```

**Example: Searching for 40 in above BST**
```
Start at 50: 40 < 50, go left
At 30: 40 > 30, go right
At 40: Found!

Comparisons: 3
```

**Complexity:**
- Best case: O(log n) - balanced tree
- Average case: O(log n) - random insertions
- Worst case: O(n) - skewed tree

### Insertion Operation

To insert a value, we search for where it should be and place it there:

```
Insert(node, value):
    if node is null:
        return new Node(value)
    
    if value < node.data:
        node.left = Insert(node.left, value)
    else if value > node.data:
        node.right = Insert(node.right, value)
    // else: value already exists (or handle duplicates as needed)
    
    return node
```

**Example: Insert 45 into above BST**
```
Start at 50: 45 < 50, go left
At 30: 45 > 30, go right
At 40: 45 > 40, go right
Right child is null, insert here!

Result:
         50
        /  \
      30    70
     /  \   / \
   20  40 60  80
         \
         45
```

**Complexity:** Same as search - O(log n) average, O(n) worst

### Finding Minimum and Maximum

**Minimum:** Leftmost node
```
FindMin(node):
    if node is null:
        return null
    while node.left is not null:
        node = node.left
    return node
```

**Maximum:** Rightmost node
```
FindMax(node):
    if node is null:
        return null
    while node.right is not null:
        node = node.right
    return node
```

**Complexity:** O(height) = O(log n) average

### Deletion Operation

Most complex operation - three cases:

**Case 1: Node is a leaf (no children)**
- Simply remove the node

**Case 2: Node has one child**
- Replace node with its child

**Case 3: Node has two children**
- Find the in-order successor (minimum value in right subtree)
- Replace node's data with successor's data
- Delete the successor (which has at most one child)

```
Delete(node, value):
    if node is null:
        return null
    
    if value < node.data:
        node.left = Delete(node.left, value)
    else if value > node.data:
        node.right = Delete(node.right, value)
    else: // Found node to delete
        // Case 1 & 2: 0 or 1 child
        if node.left is null:
            return node.right
        if node.right is null:
            return node.left
        
        // Case 3: 2 children
        successor = FindMin(node.right)
        node.data = successor.data
        node.right = Delete(node.right, successor.data)
    
    return node
```

**Example: Delete 30 from BST**
```
Original:
         50
        /  \
      30    70
     /  \   / \
   20  40 60  80

30 has two children, find successor:
Successor = minimum in right subtree = 40

Replace 30 with 40:
         50
        /  \
      40    70
     /     / \
   20    60  80

Delete the original 40 node (leaf).
```

**Complexity:** O(height) = O(log n) average

## BST Applications

### Dictionaries/Maps

Store key-value pairs with efficient lookup:
- Search: O(log n)
- Insert: O(log n)
- Delete: O(log n)

### Sets

Maintain sorted collection of unique elements:
- Contains: O(log n)
- Add: O(log n)
- Remove: O(log n)
- In-order traversal gives sorted sequence

### Range Queries

Find all elements in a range [low, high]:

```
RangeQuery(node, low, high, result):
    if node is null:
        return
    
    // If current value in range, include it
    if low <= node.data <= high:
        result.add(node.data)
    
    // Recurse left if there could be values in range
    if node.data > low:
        RangeQuery(node.left, low, high, result)
    
    // Recurse right if there could be values in range
    if node.data < high:
        RangeQuery(node.right, low, high, result)
```

### Sorted Iteration

In-order traversal provides sorted sequence in O(n) time.

## Balanced Trees (Concept)

### The Problem

If we insert sorted data into a BST, it degenerates into a linked list:

```
Insert 10, 20, 30, 40, 50:

10
 \
  20
   \
    30
     \
      40
       \
        50

Height: 4 (n-1)
Search time: O(n) - No better than linear search!
```

### Self-Balancing Trees

**Concept:** Automatically maintain balance during insertions/deletions to ensure height remains O(log n).

**Common Types:**
- **AVL Trees**: Strictly balanced (height difference ≤ 1)
- **Red-Black Trees**: Looser balance, faster insertion
- **B-Trees**: Multi-way trees, used in databases
- **Splay Trees**: Recently accessed items near root

**Guaranteed Performance:**
- All operations: O(log n)
- No degenerate cases

**Trade-off:**
- More complex implementation
- Additional storage for balance information
- Extra operations during insertion/deletion

## Tree Implementation Patterns

### Recursive Pattern

Most tree operations naturally recursive:

```
TreeOperation(node):
    if node is null:
        return base_case_value
    
    // Process current node
    result = some_operation(node.data)
    
    // Recurse on children
    left_result = TreeOperation(node.left)
    right_result = TreeOperation(node.right)
    
    // Combine results
    return combine(result, left_result, right_result)
```

### Examples Using Pattern

**Count nodes:**
```
CountNodes(node):
    if node is null:
        return 0
    return 1 + CountNodes(node.left) + CountNodes(node.right)
```

**Calculate height:**
```
Height(node):
    if node is null:
        return -1
    return 1 + max(Height(node.left), Height(node.right))
```

**Sum all values:**
```
Sum(node):
    if node is null:
        return 0
    return node.data + Sum(node.left) + Sum(node.right)
```

**Check if BST:**
```
IsBST(node, min, max):
    if node is null:
        return true
    
    if node.data <= min or node.data >= max:
        return false
    
    return IsBST(node.left, min, node.data) and 
           IsBST(node.right, node.data, max)

// Initial call: IsBST(root, -∞, +∞)
```

## Comparison with Other Structures

| Operation | Array | Linked List | BST (balanced) | Hash Table |
|-----------|-------|-------------|----------------|------------|
| Search | O(n) or O(log n)* | O(n) | O(log n) | O(1)** |
| Insert | O(n) | O(1)*** | O(log n) | O(1)** |
| Delete | O(n) | O(n)**** | O(log n) | O(1)** |
| Min/Max | O(n) or O(1)* | O(n) | O(log n) | O(n) |
| Sorted order | O(n log n) | O(n log n) | O(n) | O(n log n) |
| Range query | O(n) | O(n) | O(log n + k) | O(n) |

\* If sorted  
\** Average case  
\*** At beginning  
\**** If position known, otherwise O(n) to find

**BST Advantages:**
- Maintains sorted order
- Efficient search, insert, delete
- Range queries efficient
- In-order traversal gives sorted sequence

**BST Disadvantages:**
- More complex than arrays/lists
- Requires balancing for guaranteed performance
- Extra memory for pointers

## Best Practices

1. **Always maintain BST property** during insertions and deletions
2. **Use balanced trees** for guaranteed O(log n) performance
3. **Choose traversal** based on problem requirements
4. **Consider iterative** implementations for production (avoid stack overflow)
5. **Handle null cases** carefully in recursive functions
6. **Test with edge cases**: empty tree, single node, skewed tree

## Summary

Tree structures provide hierarchical organization with efficient operations when properly balanced. Binary search trees combine the benefits of binary search with dynamic data, enabling O(log n) search, insertion, and deletion in average cases. Understanding traversal methods, the BST property, and balancing concepts is essential for effectively using and implementing tree-based data structures in practice.
