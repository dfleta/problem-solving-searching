import pytest
from src.world import Map

@pytest.fixture(name="test_map")
def map_instance():
    return Map()

def test_find_position_existing_state(test_map):
    assert test_map.find_position("A") == (0, 1)
    assert test_map.find_position("Ñ") == (2, 0)
    assert test_map.find_position("P") == (3, 4)

def test_find_position_non_existing_state(test_map):
    assert test_map.find_position("NonExistent") is None

def test_find_position_edge_cases(test_map):
    assert test_map.find_position("Y") == (0, 0)
    assert test_map.find_position("X") == (5, 4)

def test_successors_existing_state(test_map):
    assert test_map.successors("A") == [("E", 1), ("Y", 2), ("B", 2)]
    assert test_map.successors("Ñ") == [("Z", 1), ("LL", 1), ("I", 2)]

def test_successors_non_visiting_states(test_map):
    assert test_map.successors("F") == [("B", 1), ("E", 2), ("G", 2)]
    assert test_map.successors("G") == [("C", 1), ("F", 2), ("H", 2)]
    assert test_map.successors("L") == [("H", 1), ("P", 1)]

def test_successors_non_existing_state(test_map):
    assert test_map.successors("NonExistent") == []

def test_successors_edge_cases(test_map):
    assert test_map.successors("Y") == [("Z", 1), ("A", 2)]
    assert test_map.successors("X") == [("W", 2)]

def test_successors_unvisitable_state(test_map):
    assert test_map.successors("-") == []

def test_successors_with_unvisitable_neighbors(test_map):
    assert test_map.successors("B") == [("F", 1), ("A", 2), ("C", 2)]
    assert test_map.successors("L") == [("H", 1), ("P", 1)]
    assert test_map.successors("S") == [("O", 1), ("W", 1)]
