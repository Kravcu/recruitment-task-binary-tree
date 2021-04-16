import statistics

from BinaryTree import Node, Tree, IllegalArgumentCombinationError
import pytest


@pytest.mark.parametrize("a,b,c", [
    (None, None, None),
    (5, None, None),
    (5, Node(1), None),
    (1, None, Node(5)),
    (5, Node(1), Node(2)),
])
def test_Node_NoExceptionWhenCorrectValuesOnInit(a, b, c):
    node = Node(a, b, c)


@pytest.mark.parametrize("a,b,c", [
    (5, 3, 2),
    (1, 1, None),
    (2, None, 1),
    (None, 1, None),
    (None, None, 1),
    (None, Node(None), 1),
    (5, Node(None), 1),
    ("foo", "bar", "baz"),
    (1, "bar", "baz"),
    (1, "bar", Node(None)),
])
def test_Node_RaisesTypeErrorWhenInvalidChildrenOnInit(a, b, c):
    with pytest.raises(TypeError):
        node = Node(a, b, c)


@pytest.mark.parametrize("a,b,c", [
    (None, Node(5), None),
    (None, None, Node(3)),
])
def test_Node_RaisesIllegalArgumentCombinationErrorOnInit(a, b, c):
    with pytest.raises(IllegalArgumentCombinationError):
        node = Node(a, b, c)


@pytest.mark.parametrize("a,b,c", [
    (1, None, None),
    (None, None, None),
    (1, None, Node(3)),
    (1, Node(5), None),
    (1, Node(5), Node(3)),
])
def test_Node_AssignsCorrectValuesOnInit(a, b, c):
    node = Node(a, b, c)
    assert node.value == a, "Incorrect value field"
    assert node.left is b, "Incorrect left field"
    assert node.right is c, "Incorrect right field"


@pytest.mark.parametrize("a", [
    ('foo'),
    (1),
    ([])
])
def test_Tree_RaisesTypeErrorWhenInvalidRootOnInit(a):
    with pytest.raises(TypeError):
        tree = Tree(a)


@pytest.mark.parametrize("tree,tree_sum,tree_avg,tree_median", [
    (Node(1), 1, 1, 1),
    (Node(1, Node(2), Node(4)), 7, 7 / 3, 2),
    (Node(1, Node(2, Node(4, Node(7)), Node(9)), Node(3, Node(5), Node(6))), 37, 4.625, 4.5),
    (Node(5, Node(3, Node(2), Node(5)), Node(7, Node(1), Node(0, Node(2), Node(8, None, Node(5))))), 38, 3.8, 4.0)
])
def test_Tree_CalculateValuesFullTree(tree, tree_sum, tree_avg, tree_median):
    t = Tree(tree)
    assert t.get_sum(full_tree=True) == tree_sum, "Incorrect sum"
    assert t.get_mean(full_tree=True) == tree_avg, "Incorrect average"
    assert t.get_median(full_tree=True) == tree_median, "Incorrect median"


@pytest.mark.parametrize("tree,tree_sum,tree_avg,tree_median", [
    (Node(1, Node(2, Node(4, Node(7)), Node(9)), Node(3, Node(5), Node(6))), 14, 14 / 3, 5),
    (Node(5, Node(3, Node(2), Node(5)), Node(7, Node(1), Node(0, Node(2), Node(8, None, Node(5))))), 23, 23 / 6, 3.5)
])
def test_Tree_CalculateValuesSubTree(tree, tree_sum, tree_avg, tree_median):
    t = Tree(tree)
    assert t.get_sum(full_tree=False, sub_tree=t.root.right) == tree_sum, "Incorrect sum"
    assert t.get_mean(full_tree=False, sub_tree=t.root.right) == tree_avg, "Incorrect average"
    assert t.get_median(full_tree=False, sub_tree=t.root.right) == tree_median, "Incorrect median"


@pytest.mark.parametrize("a", [
    (None),
    (Node(None))
])
def test_Tree_RaisesStatisticsErrorOnEmptyTree(a):
    t = Tree(a)
    assert t.get_sum(full_tree=True) == 0, "Incorrect sum"
    with pytest.raises(statistics.StatisticsError):
        t.get_median(full_tree=True)
        t.get_mean(full_tree=True)
