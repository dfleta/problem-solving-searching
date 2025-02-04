from src.world import Map
from src.node import Node
from src.frontier import Frontier
from src.explored import Explored


def a_star_search(start_state, goal_state):
    start_node = Node(start_state, g=0, h=heuristic(start_state, goal_state))
    frontier = Frontier()
    frontier.add(start_node)
    explored = Explored()

    while not frontier.is_empty():

        current_node = frontier.get_best_node()

        if current_node.state == goal_state:
            return frontier, explored, reconstruct_path(current_node)

        explored.add_node(current_node)

        for successor, cost in world.successors(current_node.state):
            g = current_node.g + cost
            # h = heuristic(successor, goal_state)
            h = manhattan_distance(successor, goal_state)
            successor_node = Node(successor, parent=current_node, g=g, h=h)

            if explored.contains_node(successor_node):
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
    x1, y1 = world.find_position(state)
    x2, y2 = world.find_position(goal_state)
    return abs(x1 - x2) + abs(y1 - y2)


def reconstruct_path(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    return path[::-1]


if __name__ == "__main__":
    world = Map()
    start_state = "S"
    goal_state = "F"
    frontier, explored, solution = a_star_search(start_state, goal_state)
    print("Path found:", solution)
    print("Explored:",  list(node for node in explored.get_elements()))
    print("Frontier:",  list(frontier.get_elements()))
