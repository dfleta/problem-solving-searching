import pytest
from src.world import World
from a_star import manhattan_distance

def test_manhattan_distance_same_position():
    assert manhattan_distance("A", "A") == 0

def test_manhattan_distance_adjacent_positions():
    assert manhattan_distance("A", "B") == 1
    assert manhattan_distance("A", "E") == 1

def test_manhattan_distance_diagonal_positions():
    assert manhattan_distance("A", "F") == 2

def test_manhattan_distance_obstacle_positions():
    assert manhattan_distance("N", "F") == 2
    assert manhattan_distance("S", "F") == 4
    assert manhattan_distance("V", "F") == 4

def test_manhattan_distance_opposite_corners():
    assert manhattan_distance("Y", "X") == 9
