from collections import OrderedDict
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np



def visualize_animation(viz, maze):
    if type(viz) is int:
        return
    fig, ax = plt.subplots()
    
    viz_list = list(viz.keys())
    path_set = set()
    
    def update(step):
        nonlocal path_set
        temp_maze = np.array(maze)
        
        if step == 0:
            path_set.clear()
        
        display_maze = np.ones_like(temp_maze, dtype=np.float32) 
        display_maze[temp_maze == 1] = 0.0 
        
        img = np.dstack([display_maze, display_maze, display_maze])  
        
        if step < len(viz_list):
            path_set.add(viz_list[step])
        
        for y, x in path_set:
            img[y, x] = [1, 0, 0]
        
        ax.clear()
        ax.imshow(img)
        ax.set_title(f"Step: {step + 1}")
        ax.set_xticks([])
        ax.set_yticks([])
    
    ani = animation.FuncAnimation(fig, update, frames=len(viz_list), interval=500, repeat=True)
    plt.show()



def greedy(maze, start, finish):
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
    init_val = heuristic(start, finish)
    frontier = []
    frontier.append((init_val, start))
    explored = {}
    while frontier:
        frontier = sorted(frontier, key=lambda x: x[0])
        current = frontier.pop(0)[1]
        explored[current] = True

        if current == finish:
            return len(explored), explored
        x_mod = [-1, 1, 0, 0]
        y_mod = [0, 0, -1, 1]
        for i in range(0, 4):
            if not current[0]+x_mod[i] >= 0:
                continue
            if not current[0]+x_mod[i] >= 0:
                continue
            if not current[0]+x_mod[i] < len(maze[0]):
                continue
            if not current[1] + y_mod[i] >= 0:
                continue
            if not current[1]+y_mod[i] < len(maze[1]):
                continue
            if not maze[current[0]+x_mod[i]][current[1] + y_mod[i]] == 0:
                continue
            if not (current[0]+x_mod[i], current[1] + y_mod[i]) not in explored:
                continue
            if not (current[0]+x_mod[i], current[1] + y_mod[i]) not in frontier:
                continue
            frontier.append((heuristic((current[0]+x_mod[i], current[1]+y_mod[i]), finish), (current[0]+x_mod[i], current[1]+y_mod[i])))
    return (-1,-1)
    

def heuristic(position, finish):
    return pow(position[0] - finish[0], 2) + pow(position[1] - finish[1], 2)
    # return abs(position[0] - finish[0]) + abs(position[1] - finish[1])


def vizualize(viz, maze):
    if type(viz) is int:
        return
    counter = 1
    for val in viz:
        print(f"Step: {counter}" )
        for i in range(len(maze)):
            if(i == val[0]):
                maze[i][val[1]] = 8
            print(maze[i])
        print("\n")
        counter+=1

    """
    Vizualization function. Shows step by step the work of the search algorithm

    Parameters:
    - viz: everything required for step-by-step vizualization
    """

