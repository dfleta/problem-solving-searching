import argparse

from src.frontier import Frontier
from src.node import Node
from src.output import problem_repr
from src.reached import Reached
from src.world import World


def a_star_search(initial_state, goal_state):
    start_node = Node(
        initial_state,
        parent=None,
        g=0,
        h=manhattan_distance(initial_state, goal_state),
    )
    frontier = Frontier()
    frontier.add(start_node)
    reached = Reached()

    while not frontier.is_empty():
        current_node = frontier.get_best_node()

        if current_node.state == goal_state:
            reached.add(current_node)
            return frontier, reached, solution(current_node)

        reached.add(current_node)

        for successor, cost in World.successors(current_node.state):
            g = current_node.g + cost
            # h = heuristic(successor, goal_state)
            h = manhattan_distance(successor, goal_state)
            successor_node = Node(successor, parent=current_node, g=g, h=h)

            if reached.contains(successor_node):
                continue

            if (
                not frontier.contains(successor_node)
                # or current_node.g < successor_node.g
            ):
                frontier.add(successor_node)
            else:
                frontier.update(successor_node)

    return None


def heuristic(state, goal_state):
    # Implement a heuristic function here
    # x1, y1 = state
    # x2, y2 = goal_state
    # return abs(x1 - x2) + abs(y1 - y2)
    return abs(ord(state[0]) - ord(goal_state[0]))


def manhattan_distance(state, goal_state):
    x1, y1 = World.find_position(state)
    x2, y2 = World.find_position(goal_state)
    return abs(x1 - x2) + abs(y1 - y2)


def solution(node):
    # (lambda path: path[::-1])
    # (list(iter(lambda: node and (node := node.parent) or None, None)))
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    return path[::-1]


def parse_arguments():
    parser = argparse.ArgumentParser(description="A* Search Algorithm")
    parser.add_argument("start_state", help="Initial state", default="Z")
    parser.add_argument("goal_state", help="Goal state", default="N")
    parser.add_argument(
        "-v_c",
        type=int,
        default=1,
        help="Cost for vertical movements",
        required=False,
    )
    parser.add_argument(
        "-h_c",
        type=int,
        default=2,
        help="Cost for horizontal movements",
        required=False,
    )
    return parser.parse_args()


def main():
    args = parse_arguments()
    initial_state = args.start_state
    goal_state = args.goal_state
    World.V_COST = args.v_c
    World.H_COST = args.h_c


    frontier, explored, solution = a_star_search(initial_state, goal_state)
    problem_repr(solution, explored, frontier, initial_state, goal_state)


if __name__ == "__main__":
    main()
