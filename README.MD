# Recruitment task

## General

This repo contains source code for recruitment task. The task was to implement data structures to represent binary
trees. Implemented structures needed to have methods for:

1) Calculate sum of values in a subtree
2) Calculate mean
3) Calculate median

Unit tests were also desired. Implemented structures are called Node and Tree.

Node is a single node in a tree containing a single int number and left/right children, which can be other Nodes or
None. Tree constructor as takes a Node structure or None as an input. This class implements methods to calculate sum,
mean and median in full tree or specified subtree. Apart from that we can also print a tree.

Error handling is included for calculating mean/median from an empty tree(i.e. where the root in tree is None or has a
single Node with None value) - exception is raised. Situations where there is a loop in the tree (i.e. the tree is a
graph and not a tree) are considered - the node will be taken into calculations only once.

The graph traversal is implemented using iterative DFS algorithm.

## How to run:

Just clone the repo, needed structures are located in `BinaryTree.py` and related unit tests
in `tests/test_BinaryTree.py`. For detailed usage please see `Code Example` chapter.

## Code Example

```
t = Node(5, Node(3, Node(2), Node(5)), Node(7, Node(1), Node(0, Node(2), Node(8, None, Node(5)))))
tree = Tree(t)

print("Full tree:")
tree.print_tree(True)
print("Subtree:")
tree.print_tree(False, tree.root.right)
print()

print("Sum of full tree: ", tree.get_sum(True))
print("Sum of subtree: ", tree.get_sum(False, tree.root.right))
print("Mean of full tree: ", tree.get_mean(True))
print("Mean of subtree: ", tree.get_mean(False, tree.root.right))
print("Median of full tree: ", tree.get_median(True))
print("Median of subtree: ", tree.get_median(False, tree.root.right))
```

Output:

```
Full tree:
         2
     3
         5
 5
         1
     7
             2
         0
             8
                 5
Subtree:
     1
 7
         2
     0
         8
             5

Sum of full tree:  38
Sum of subtree:  23
Mean of full tree:  3.8
Mean of subtree:  3.8333333333333335
Median of full tree:  4.0
Median of subtree:  3.5
```

## Dependencies

`
pytest==6.1.2
`

## Remarks:

1. I am using different types of type hints in code(Unions) and docstrings(pipes |). Pycharms has a problem rendering
   Unions in docstrings and then complains about wrong type, so I used pipes to fix that.


