# Test cases for the Frontier class
# Also integration test for Set and Node classes

import pytest
from src.frontier import Frontier
from src.node import Node


@pytest.fixture(name="frontier")
def set_up_frontier():
    return Frontier()


def test_add_node(frontier):
    node = Node(state="A", parent=None, g=0, h=0)
    frontier.add(node)
    assert frontier.contains(node)


def test_add_invalid_node(frontier):
    frontier.add("invalid_node")
    assert frontier.size() == 0


def test_add_multiple_nodes(frontier):
    nodeA = Node(state="A", parent=None, g=1, h=2)
    nodeB = Node(state="B", parent="A", g=2, h=2)
    nodeC = Node(state="C", parent="B", g=3, h=3)
    frontier.add(nodeA)
    frontier.add(nodeB)
    frontier.add(nodeC)
    assert frontier.size() == 3


def test_remove_node(frontier):
    node = Node(state="A", parent=None, g=0, h=0)
    frontier.add(node)
    frontier.remove(node)
    assert not frontier.contains(node)


def test_remove_invalid_node(frontier):
    frontier.remove("invalid_node")
    assert frontier.size() == 0


def test_remove_nonexistent_node(frontier):
    nodeA = Node(state="A", parent=None, g=1, h=2)
    nodeB = Node(state="B", parent="A", g=2, h=2)
    nodeC = Node(state="C", parent="B", g=3, h=3)
    frontier.add(nodeA)
    frontier.add(nodeB)
    frontier.add(nodeC)
    node = Node(state="D", parent="C", g=4, h=2)
    frontier.remove(node)
    assert frontier.size() == 3
    assert not frontier.contains(node)


def test_get_best_node(frontier):
    nodeA = Node(state="A", parent=None, g=1, h=3)
    nodeB = Node(state="B", parent="A", g=2, h=1)
    nodeC = Node(state="C", parent="B", g=3, h=3)
    frontier.add(nodeA)
    frontier.add(nodeB)
    frontier.add(nodeC)
    best_node = frontier.get_best_node()
    assert best_node == nodeB
    assert frontier.size() == 2


def test_get_best_node_empty(frontier):
    best_node = frontier.get_best_node()
    assert best_node is None

def test_get_node():
    frontier = Frontier()
    nodeA = Node(state="A", parent=None, g=1, h=3)
    nodeB = Node(state="B", parent="A", g=2, h=1)
    nodeC = Node(state="C", parent="B", g=3, h=3)
    frontier.add(nodeA)
    frontier.add(nodeB)
    frontier.add(nodeC)
    assert frontier.get_node(nodeA) == nodeA
    assert frontier.get_node(nodeB) == nodeB
    assert frontier.get_node(nodeC) == nodeC

def test_update_node(frontier):
    nodeA = Node(state="A", parent=None, g=1, h=3)
    nodeB = Node(state="B", parent="A", g=2, h=1)
    nodeC = Node(state="C", parent="B", g=3, h=3)
    nodeE = Node(state="E", parent="C", g=4, h=2)
    nodeF = Node(state="F", parent="C", g=5, h=1)
    frontier.add(nodeA)
    frontier.add(nodeB)
    frontier.add(nodeC)
    frontier.add(nodeE)
    frontier.add(nodeF)
    nodeD = Node(state="C", parent="B", g=2, h=2)
    frontier.update(nodeD)
    assert frontier.size() == 5
    assert frontier.contains(nodeD)
    assert frontier.get_node(nodeD).g == 2

    assert frontier.get_node(nodeE).parent == "C"
    assert frontier.get_node(nodeE).g == 3
    assert frontier.get_node(nodeF).g == 4
