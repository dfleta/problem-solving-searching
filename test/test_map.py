import pytest
from src.world import World


def test_find_position_existing_state():
    assert World.find_position("A") == (0, 1)
    assert World.find_position("Ñ") == (2, 0)
    assert World.find_position("P") == (3, 4)

def test_find_position_non_existing_state():
    assert World.find_position("NonExistent") is None

def test_find_position_edge_cases():
    assert World.find_position("Y") == (0, 0)
    assert World.find_position("X") == (5, 4)

def test_successors_existing_state():
    assert World.successors("A") == [("E", 1), ("Y", 2), ("B", 2)]
    assert World.successors("Ñ") == [("Z", 1), ("LL", 1), ("I", 2)]

def test_successors_non_visiting_states():
    assert World.successors("F") == [("B", 1), ("E", 2), ("G", 2)]
    assert World.successors("G") == [("C", 1), ("F", 2), ("H", 2)]
    assert World.successors("L") == [("H", 1), ("P", 1)]

def test_successors_non_existing_state():
    assert World.successors("NonExistent") == []

def test_successors_edge_cases():
    assert World.successors("Y") == [("Z", 1), ("A", 2)]
    assert World.successors("X") == [("W", 2)]

def test_successors_unvisitable_state():
    assert World.successors("-") == []

def test_successors_with_unvisitable_neighbors():
    assert World.successors("B") == [("F", 1), ("A", 2), ("C", 2)]
    assert World.successors("L") == [("H", 1), ("P", 1)]
    assert World.successors("S") == [("O", 1), ("W", 1)]
