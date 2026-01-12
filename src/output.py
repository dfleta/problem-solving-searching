from src.cli_colors import Colors
from src.world import World


def problem_repr(solution, explored, frontier, initial_state, goal_state):
    print("\nPath found:", " -> ".join(solution))
    print()
    for row in World.WORLD:
        for state in row:
            if state == initial_state:
                _show_state_colored(state, Colors.RED)
            elif state == goal_state:
                _show_state_colored(state, Colors.BRIGHT_YELLOW)
            elif state in solution:
                _show_state_colored(state, Colors.BRIGHT_GREEN)
            elif state in str(explored.get_elements()):
                _show_state_colored(state, Colors.BLUE)
            elif state in str(frontier.get_elements()):
                _show_state_colored(state, Colors.PURPLE)
            else:
                print(state, end=" ")
        print()
    print("\nStart state:", end=" ")
    _show_state_colored(initial_state, Colors.RED)
    print("\nGoal State:", end=" ")
    _show_state_colored(goal_state, Colors.BRIGHT_YELLOW)
    print("\nSolution: ")
    _show_state_colored(solution, Colors.BRIGHT_GREEN)
    print("\nExplored (state g): ")
    _show_state_colored(explored.get_elements(), Colors.BLUE)
    print("\nFrontier: ")
    _show_state_colored(frontier.get_elements(), Colors.PURPLE)
    print()


def _show_state_colored(state, color):
    print(f"{color}{state}{Colors.RESET}", end=" ")
