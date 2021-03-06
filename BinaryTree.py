from typing import Union
from collections import deque
import statistics


class IllegalArgumentCombinationError(Exception):
    def __init__(self, message):
        super().__init__(message)


class Node:
    """
        Represents single Node of a binary tree. Has an optional int value and two optional nested Node children.
    """

    def __init__(self, value, left_branch=None, right_branch=None):
        if not self._is_correct_arg(value, int):
            raise TypeError("Expected 'value' to be instance of 'int' or None")
        if not self._is_correct_arg(left_branch, Node) or not self._is_correct_arg(right_branch, Node):
            raise TypeError("Expected 'left_branch, right_branch' to be instance of 'Node' or None")
        if value is None and (left_branch is not None or right_branch is not None):
            raise IllegalArgumentCombinationError("Node children cannot exist if root is None")

        self._left_child: Union[Node, None] = left_branch
        self._right_child: Union[Node, None] = right_branch
        self._root: Union[None, int] = value

    def _is_correct_arg(self, arg, cls) -> bool:
        """
        Function to check if argument is None or instance of cls
        Args:
            arg (Object): object to check
            cls (Object): wanted class type

        Returns:
            bool: True if arg is None or instance of cls
        """
        return arg is None or isinstance(arg, cls)

    @property
    def value(self):
        return self._root

    @property
    def left(self):
        return self._left_child

    @property
    def right(self):
        return self._right_child


class Tree:
    """
        Represents binary tree consisting of nested Nodes objects.
    """

    def __init__(self, root_node: Union[Node, None]):
        if not (root_node is None or isinstance(root_node, Node)):
            raise TypeError('Root node has to be an instance of Node or None')
        self._root: Union[Node, None] = root_node

    @property
    def root(self):
        return self._root

    def _print_tree_recursive(self, node, level=0) -> None:
        """
        Recursive function to print tree
        Args:
            node (Node|None): currently visited node
            level (int): indentation level

        Returns:
            None
        """
        spacing: int = 4
        if node is not None:
            self._print_tree_recursive(node.left, level + 1)
            print(' ' * spacing * level, node.value)
            self._print_tree_recursive(node.right, level + 1)

    def print_tree(self, full_tree: bool = True, node=None) -> None:
        """
        Prints readable representation of a tree
        Args:
            full_tree (bool): if True prints self.root tree, else tree specified by node
            node (Node|None): subtree to print if full_tree is false

        Returns:
            None

        Raises:
            TypeError: when full_tree is false and specified subtree is None or instance of Node class
        """
        if full_tree:
            node = self.root
        else:
            if node is not None and not isinstance(node, Node):
                raise TypeError
        self._print_tree_recursive(node)

    def _get_subtree_values(self, node=None) -> deque:
        """
        Function to traverse all the nodes in tree and return their values.
        It implements iterative DFS algo to traverse all nodes and gather their values in a deque(which has O(1) append
         time unlike list which has O(n)).
         Every node is checked against the visited list to make sure there are no duplicated values.

        Args:
            node (Node|None):

        Returns:
            deque.Deque containing all values from nodes in a tree (without Nones)
        """
        if node is None:
            return deque()

        nodes_to_check = deque()
        nodes_to_check.append(node)
        node_values = deque()
        visited = set()
        while len(nodes_to_check):
            current_node = nodes_to_check.pop()
            if id(current_node) not in visited:
                visited.add(id(current_node))
                if current_node.value is not None:
                    node_values.append(current_node.value)
                if current_node.left is not None:
                    nodes_to_check.append(current_node.left)
                if current_node.right is not None:
                    nodes_to_check.append(current_node.right)
        return node_values

    def get_sum(self, full_tree: bool = True, sub_tree=None) -> float:
        """
        Calculates sum of elements in a tree. Each value in a tree is used for calculation only once.
        Args:
            full_tree (bool): if True  self.root tree is used for calculation, else tree specified by sub_tree
            sub_tree (Node|None): subtree to use for calculation if full_tree is False

        Returns:
            Sum of elements in a tree or 0 when tree is empty or has a single Node with None value
        """
        if full_tree:
            sub_tree = self.root
        return sum(self._get_subtree_values(sub_tree))

    def get_mean(self, full_tree: bool = True, sub_tree=None) -> float:
        """
        Calculates mean of elements in a tree. Each value in a tree is used for calculation only once.
        Args:
            full_tree (bool): if True  self.root tree is used for calculation, else tree specified by sub_tree
            sub_tree (Node|None): subtree to use for calculation if full_tree is False

        Returns:
            Mean of elements in a tree

        Raises:
            statistics.StatisticsError: when tree has no elements(i.e. is None) or has a single element that has
            value None
        """
        if full_tree:
            sub_tree = self.root
        try:
            return statistics.mean(self._get_subtree_values(sub_tree))
        except statistics.StatisticsError:
            raise statistics.StatisticsError('Cannot calculate mean from an empty Tree')

    def get_median(self, full_tree: bool = True, sub_tree=None) -> float:
        """
        Calculates median of elements in a tree. Each value in a tree is used for calculation only once.
        Args:
            full_tree (bool): if True  self.root tree is used for calculation, else tree specified by sub_tree
            sub_tree (Node|None): subtree to use for calculation if full_tree is False

        Returns:
            Median of elements in a tree

        Raises:
            statistics.StatisticsError: when tree has no elements(i.e. is None) or has a single element that has
            value None
        """
        if full_tree:
            sub_tree = self.root
        try:
            return statistics.median(self._get_subtree_values(sub_tree))
        except statistics.StatisticsError:
            raise statistics.StatisticsError('Cannot calculate median from an empty Tree')
