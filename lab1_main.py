import lab1_tests
import lab1_v2

if __name__ == "__main__":
    #lab1_tests.main()

        
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

    num_steps, viz = lab1_v2.greedy(maze, start_position, finish_position)

    # Print number of steps in path
    if num_steps != -1:
        print(f"Path from {start_position} to {finish_position} using greedy best-first search is {num_steps} steps.")

    else:
        print(f"No path from {start_position} to {finish_position} exists.")

    # Vizualize algorithm step-by-step even if the path was not found
    #vizualize(viz, maze)
    lab1_v2.visualize_animation(viz, maze)