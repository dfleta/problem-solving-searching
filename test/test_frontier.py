import pytest
from src.frontier import Frontier
from src.node import Node
from src.world import Map

@pytest.fixture(name="frontier")
def set_up_frontier():
    return Frontier()

@pytest.fixture
def map():
    return Map()

def test_add_node(frontier):
    node = Node(state="A", parent=None, g=0, h=0)
    frontier.add(node)
    assert node in frontier.get_elements()

def test_remove_node(frontier):
    node = Node(state="A", parent=None, g=0, h=0)
    frontier.add(node)
    frontier.remove(node)
    assert node not in frontier.get_elements()

def test_get_best_node(frontier):
    node1 = Node(state="A", parent=None, g=1, h=2)
    node2 = Node(state="B", parent=None, g=2, h=1)
    frontier.add(node1)
    frontier.add(node2)
    best_node = frontier.get_best_node()
    assert best_node == node2

def test_get_best_node_empty(frontier):
    best_node = frontier.get_best_node()
    assert best_node is None

def test_add_invalid_node(frontier):
    frontier.add("invalid_node")
    assert len(frontier.get_elements()) == 0

def test_remove_invalid_node(frontier):
    frontier.remove("invalid_node")
    assert len(frontier.get_elements()) == 0

def test_add_multiple_nodes(frontier):
    node1 = Node(state="A", parent=None, g=1, h=2)
    node2 = Node(state="B", parent=None, g=2, h=1)
    node3 = Node(state="C", parent=None, g=3, h=3)
    frontier.add(node1)
    frontier.add(node2)
    frontier.add(node3)
    assert node1 in frontier.get_elements()
    assert node2 in frontier.get_elements()
    assert node3 in frontier.get_elements()

def test_remove_nonexistent_node(frontier):
    node = Node(state="A", parent=None, g=0, h=0)
    frontier.remove(node)
    assert node not in frontier.get_elements()
