from src.world import World
from src.node import Node
from src.frontier import Frontier
from src.reached import Reached


def a_star_search(start_state, goal_state):
    start_node = Node(start_state, g=0, h=heuristic(start_state, goal_state))
    frontier = Frontier()
    frontier.add(start_node)
    reached = Reached()

    while not frontier.is_empty():

        current_node = frontier.get_best_node()

        if current_node.state == goal_state:
            return frontier, reached, solution(current_node)

        reached.add(current_node)

        for successor, cost in World.successors(current_node.state):
            g = current_node.g + cost
            # h = heuristic(successor, goal_state)
            h = manhattan_distance(successor, goal_state)
            successor_node = Node(successor, parent=current_node, g=g, h=h)

            if reached.contains(successor_node):
                continue

            if not frontier.contains(successor_node) or g < successor_node.g:
                frontier.add(successor_node)

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
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    return path[::-1]


if __name__ == "__main__":
    START_STATE = "S"
    GOAL_STATE = "F"
    frontier, explored, solution = a_star_search(START_STATE, GOAL_STATE)
    print("Path found:", " -> ".join(solution))
    print("Explored:", list(node for node in explored.get_elements()))
    print("Frontier:", list(frontier.get_elements()))
