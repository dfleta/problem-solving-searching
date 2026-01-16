import matplotlib.pyplot as plt
import numpy as np
from src.world import World

class MatrixPlotter:
    def __init__(self, world, solution, explored, frontier, initial_state, goal_state):
        self.world = world
        self.solution = solution
        self.explored = explored
        self.frontier = frontier
        self.initial_state = initial_state
        self.goal_state = goal_state

    def plot(self):
        # Create a numeric matrix representation (0 for obstacles, 1 for accessible)
        rows = len(self.world)
        cols = len(self.world[0]) if rows > 0 else 0
        matrix = np.zeros((rows, cols))
        
        # Mark accessible cells as 1, obstacles as 0
        for row in range(rows):
            for col in range(cols):
                if self.world[row][col] != "-":
                    matrix[row][col] = 1
        
        fig, ax = plt.subplots(figsize=(10, 8))
        
        # Display the world map
        ax.imshow(matrix, cmap='Greys', interpolation='nearest', alpha=0.3)
        
        # Extract positions from explored nodes and mark them
        explored_positions = set()
        for node in self.explored:
            pos = World.find_position(node.state)
            if pos:
                explored_positions.add(pos)
                ax.scatter(pos[1], pos[0], color='blue', s=100, marker='o', alpha=0.6, label='Explored' if len(explored_positions) == 1 else '')
        
        # Extract positions from frontier nodes and mark them
        frontier_positions = set()
        for node in self.frontier:
            pos = World.find_position(node.state)
            if pos:
                frontier_positions.add(pos)
                ax.scatter(pos[1], pos[0], color='purple', s=100, marker='s', alpha=0.6, label='Frontier' if len(frontier_positions) == 1 else '')
        
        # Mark the solution path
        solution_positions = []
        for state in self.solution:
            pos = World.find_position(state)
            if pos:
                solution_positions.append(pos)
                ax.scatter(pos[1], pos[0], color='green', s=100, marker='*', alpha=0.8, label='Solution' if len(solution_positions) == 1 else '')
        
        # Draw lines connecting the solution path
        if solution_positions:
            solution_positions_array = np.array(solution_positions)
            ax.plot(solution_positions_array[:, 1], solution_positions_array[:, 0], color='green', linewidth=2, alpha=0.5)
        
        # Mark initial and goal states
        initial_pos = World.find_position(self.initial_state)
        goal_pos = World.find_position(self.goal_state)
        
        if initial_pos:
            ax.scatter(initial_pos[1], initial_pos[0], color='red', s=200, marker='o', edgecolors='darkred', linewidth=2, label='Start', zorder=5)
        
        if goal_pos:
            ax.scatter(goal_pos[1], goal_pos[0], color='yellow', s=200, marker='o', edgecolors='orange', linewidth=2, label='Goal', zorder=5)
        
        ax.set_title('Pathfinding Visualization (A* Algorithm)', fontsize=14, fontweight='bold')
        ax.set_xlabel('Column')
        ax.set_ylabel('Row')
        ax.set_xticks(range(cols))
        ax.set_yticks(range(rows))
        ax.grid(True, alpha=0.3)
        
        # Remove duplicate labels
        handles, labels = ax.get_legend_handles_labels()
        by_label = dict(zip(labels, handles))
        ax.legend(by_label.values(), by_label.keys(), loc='upper right')
        
        plt.tight_layout()
        plt.show()
