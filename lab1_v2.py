from collections import OrderedDict

def greedy(maze, start, finish):
    init_val = heuristic(start, finish)
    frontier = []
    frontier.append((init_val, start))
    explored = {}
    while frontier:
        sorted(frontier, key=lambda x: x[0])
        current = frontier.pop(0)
        if current[1] == finish:
            return len(explored), explored
        explored[current[1]] = True
        if(current[1][0]-1 >= 0 and maze[current[1][0]-1][current[1][1]] == 0 and (current[1][0]-1, current[1][1]) not in explored and (current[1][0]-1, current[1][1]) not in frontier):
            frontier.append((heuristic((current[1][0]-1, current[1][1]), finish), (current[1][0]-1, current[1][1])))
        if(current[1][0]+1 < len(maze) and maze[current[1][0]+1][current[1][1]] == 0 and (current[1][0]+1, current[1][1]) not in explored and (current[1][0]+1, current[1][1]) not in frontier):
            frontier.append((heuristic((current[1][0]+1, current[1][1]), finish), (current[1][0]+1, current[1][1])))
        if(current[1][1]-1 >= 0 and maze[current[1][0]][current[1][1]-1] == 0 and (current[1][0], current[1][1]-1) not in explored and (current[1][0], current[1][1]-1) not in frontier):
            frontier.append((heuristic((current[1][0], current[1][1]-1), finish), (current[1][0], current[1][1]-1)))
        if(current[1][1]+1 < len(maze[0]) and maze[current[1][0]][current[1][1]+1] == 0 and (current[1][0], current[1][1]+1) not in explored and (current[1][0], current[1][1]+1) not in frontier ):
            frontier.append((heuristic((current[1][0], current[1][1]+1), finish), (current[1][0], current[1][1]+1)))
    return (-1,-1)
    """
    Greedy best-first search

    Parameters:
    - maze: The 2D matrix that represents the maze with 0 represents empty space and 1 represents a wall
    - start: A tuple with the coordinates of starting position
    - finish: A tuple with the coordinates of finishing position

    Returns:
    - Number of steps from start to finish, equals -1 if the path is not found
    - Viz - everything required for step-by-step vizualization
    
    """
    # Write your code here
def heuristic(position, finish):
    return (finish[0] + finish[1]) - (position[0] +position[1])
def vizualize(viz):
    """
    Vizualization function. Shows step by step the work of the search algorithm

    Parameters:
    - viz: everything required for step-by-step vizualization
    """


# Example usage:
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0]
]

start_position = (0, 0)
finish_position = (4, 4)

num_steps, viz = greedy(maze, start_position, finish_position)

# Print number of steps in path
if num_steps != -1:
    print(f"Path from {start_position} to {finish_position} using greedy best-first search is {num_steps} steps.")

else:
    print(f"No path from {start_position} to {finish_position} exists.")

# Vizualize algorithm step-by-step even if the path was not found
vizualize(viz)