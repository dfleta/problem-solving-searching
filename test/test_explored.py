import pytest
from src.reached import Reached
from src.node import Node
from src.world import Map

@pytest.fixture(name="explored")
def setup():
    return Reached()

def test_add_node(explored):
    nodeA = Node(state="A", parent=None, g=1, h=2)
    nodeB = Node(state="B", parent="A", g=2, h=2)
    nodeC = Node(state="C", parent="B", g=3, h=3)
    explored.add(nodeA)
    explored.add(nodeB)
    explored.add(nodeC)
    assert explored.size() == 3

def test_remove_node(explored):
    node = Node(state="A")
    explored.add(node)
    explored.remove(node)
    assert not explored.contains(node)

def test_remove_invalid_node(explored):
    explored.remove("invalid_node")
    assert explored.size() == 0

def test_contains_node(explored):
    node = Node(state="A")
    explored.add(node)
    assert explored.contains(node)
    node_not_in_explored = Node(state="B")
    assert not explored.contains(node_not_in_explored)

def test_is_empty(explored):
    assert explored.is_empty()
    node = Node(state="A")
    explored.add(node)
    assert not explored.is_empty()

def test_size(explored):
    assert explored.size() == 0
    nodeA = Node(state="A")
    nodeB = Node(state="B")
    explored.add(nodeA)
    explored.add(nodeB)
    assert explored.size() == 2

def test_get_nodes(explored):
    nodeA = Node(state="A")
    nodeB = Node(state="B")
    explored.add(nodeA)
    explored.add(nodeB)
    nodes = explored.get_nodes()
    assert nodeA in nodes
    assert nodeB in nodes
