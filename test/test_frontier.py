# Test cases for the Frontier class
# Also integration test for Set and Node classes

import pytest
from src.frontier import Frontier
from src.node import Node


@pytest.fixture(name="frontier")
def set_up_frontier():
    node_A = Node(state="A", parent=None, g=1, h=2)
    node_B = Node(state="B", parent=node_A, g=2, h=2)
    node_C = Node(state="C", parent=node_B, g=3, h=3)
    frontier = Frontier()
    frontier.add(node_A)
    frontier.add(node_B)
    frontier.add(node_C)
    assert frontier.size() == 3
    return frontier


def test_contains(frontier):
    node = Node(state="A", parent=None, g=1, h=2)
    assert frontier.contains(node)


def test_add_node(frontier):
    node = Node(state="D", parent=None, g=0, h=0)
    frontier.add(node)
    assert frontier.contains(node)


def test_add_invalid_node(frontier):
    frontier.add("invalid_node")
    assert frontier.size() == 3


def test_remove_node(frontier):
    node = Node(state="A", parent=None, g=1, h=2)
    frontier.remove(node)
    assert frontier.size() == 2


def test_remove_invalid_node(frontier):
    frontier.remove("invalid_node")
    assert frontier.size() == 3


def test_remove_nonexistent_node(frontier):
    node = Node(state="D", parent=None, g=4, h=2)
    frontier.remove(node)
    assert frontier.size() == 3
    assert not frontier.contains(node)


def test_get_best_node(frontier):
    best_node = frontier.get_best_node()
    assert best_node.state == "A"
    assert frontier.size() == 2


def test_get_best_node_empty(frontier):
    frontier.get_elements().clear()
    assert frontier.get_best_node() is None


def test_get_node(frontier):
    node = Node(state="A", parent=None, g=1, h=2)
    assert frontier.get_node(node).state == "A"


def test_update_node():
    frontier = Frontier()
    node_A = Node(state="A", parent=None, g=1, h=2)
    node_B = Node(state="B", parent=node_A, g=2, h=2)
    node_C = Node(state="C", parent=node_B, g=3, h=3)
    frontier.add(node_A)
    frontier.add(node_B)
    frontier.add(node_C)
    node_E = Node(state="E", parent=node_C, g=4, h=2)
    node_F = Node(state="F", parent=node_C, g=5, h=1)
    frontier.add(node_E)
    frontier.add(node_F)

    # nodo presente en frontera con g mayor
    node_D = Node(state="C", parent=node_B, g=2, h=2)
    frontier.update(node_D)
    # __update_frontier
    assert frontier.size() == 5
    assert frontier.contains(node_D)
    assert frontier.get_node(node_D).g == 2
    # __update_g h
    assert frontier.get_node(node_E).parent.state == "C"
    assert frontier.get_node(node_E).g == 3
    assert frontier.get_node(node_E).f == 5
    assert frontier.get_node(node_F).parent.state == "C"
    assert frontier.get_node(node_F).g == 4
    assert frontier.get_node(node_F).f == 5


def test_no_update_node(frontier):
    frontier = Frontier()
    node_A = Node(state="A", parent=None, g=1, h=2)
    node_B = Node(state="B", parent=node_A, g=2, h=2)
    node_C = Node(state="C", parent=node_B, g=3, h=3)
    frontier.add(node_A)
    frontier.add(node_B)
    frontier.add(node_C)

    # h menor, g igual
    node = Node(state="C", parent=node_B, g=3, h=2)
    frontier.update(node)
    # __update_frontier
    assert frontier.size() == 3
    assert frontier.get_node(node).h == 3
