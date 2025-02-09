from a_star import manhattan_distance
from a_star import solution
from a_star import a_star_search
from src.node import Node


def test_manhattan_distance_same_position():
    assert manhattan_distance("A", "A") == 0


def test_manhattan_distance_adjacent_positions():
    assert manhattan_distance("A", "B") == 1
    assert manhattan_distance("A", "E") == 1


def test_manhattan_distance_diagonal_positions():
    assert manhattan_distance("A", "F") == 2


def test_manhattan_distance_obstacle_between_positions():
    assert manhattan_distance("N", "F") == 2
    assert manhattan_distance("S", "F") == 4
    assert manhattan_distance("V", "F") == 4


def test_manhattan_distance_opposite_corners():
    assert manhattan_distance("Y", "X") == 9


def test_solution_single_node():
    node = Node("A")
    assert solution(node) == ["A"]


def test_solution_four_nodes():
    node_D = Node("D")
    node_C = Node("C", parent=node_D)
    node_B = Node("B", parent=node_C)
    node_A = Node("A", parent=node_B)
    assert solution(node_A) == ["D", "C", "B", "A"]


def test_a_star_searh_same_initial_goal_node():
    _, _, path = a_star_search(initial_state="S", goal_state="S")
    assert path == ["S"]


def test_a_star_search():
    _, _, path = a_star_search(initial_state="S", goal_state="F")
    assert path == ["S", "O", "P", "L", "H", "G", "F"]


def test_a_star_search_update_old_nodes():
    _, _, path = a_star_search(initial_state="Z", goal_state="N")
    assert path == ["Z", "E", "F", "G", "H", "L", "P", "O", "N"]
