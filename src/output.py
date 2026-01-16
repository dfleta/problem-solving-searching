from src.cli_colors import Colors
from src.world import World
from src.matrix_plotter import MatrixPlotter


def problem_repr(solution, explored, frontier, initial_state, goal_state):
    print("\nPath found:", " -> ".join(solution))
    print()
    # Create a MatrixPlotter instance
    plotter = MatrixPlotter(World.WORLD, solution, explored.get_elements(), frontier.get_elements(), initial_state, goal_state)
    plotter.plot()  # Call the plot method to visualize the states
    print("\nStart state:", end=" ")
    _show_state_colored(initial_state, Colors.RED)
    print("\nGoal State:", end=" ")
    _show_state_colored(goal_state, Colors.YELLOW)
    print("\nSolution: ")
    _show_state_colored(solution, Colors.GREEN)
    print("\nExplored (state g): ")
    _show_state_colored(explored.get_elements(), Colors.BLUE)
    print("\nFrontier: ")
    _show_state_colored(frontier.get_elements(), Colors.PURPLE)
    print()


def _show_state_colored(state, color):
    print(f"{color}{state}{Colors.ENDC}", end=" ")
