import unittest
import lab1_v2
import pytest

class TestMazeSolver(unittest.TestCase):
    def test_simple_open_path_euclidean(self):
        maze = [
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 1, 0, 1, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0]
        ]
        start = (0, 0)
        finish = (4, 4)
        num_steps, viz = lab1_v2.greedy(maze, start, finish)

        actual_viz = {(0, 0): True, (1, 0): True, (2, 0): True, (3, 0): True, (4, 0): True, 
                      (4, 1): True, (4, 2): True, (3, 2): True, (3, 3): True, (3, 4): True, (4, 4): True}
        
        self.assertEqual(viz, actual_viz)


    def test_completely_blocked_path_euclidean(self):
        maze = [
            [0, 1, 1, 1, 0],
            [0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0],
            [0, 1, 1, 1, 0]
        ]
        start = (0, 0)
        finish = (4, 4)
        num_steps, viz = lab1_v2.greedy(maze, start, finish)
   
        actual_viz = -1
        self.assertEqual(viz, actual_viz)


    def test_one_paths_available_euclidean(self):
        maze = [
            [0, 0, 0, 1, 0],
            [1, 1, 0, 1, 0],
            [0, 0, 0, 1, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0]
        ]
        start = (0, 0)
        finish = (4, 4)
        num_steps, viz = lab1_v2.greedy(maze, start, finish)

        actual_viz = {(0, 0): True, (0, 1): True, (0, 2): True, (1, 2): True, (2, 2): True, 
                      (2, 1): True, (2, 0): True, (3, 0): True, (4, 0): True, (4, 1): True, 
                      (4, 2): True, (4, 3): True, (4, 4): True}
        
        self.assertEqual(viz, actual_viz) 


    def test_one_narrow_path_euclidean(self):
        maze = [
            [0, 1, 1, 1, 1],
            [0, 0, 0, 0, 1],
            [1, 1, 1, 0, 1],
            [1, 1, 1, 0, 1],
            [1, 1, 1, 0, 0]
        ]
        start = (0, 0)
        finish = (4, 4)
        num_steps, viz = lab1_v2.greedy(maze, start, finish)
   
        actual_viz = {(0, 0): True, (1, 0): True, (1, 1): True, (1, 2): True, (1, 3): True, 
                      (2, 3): True, (3, 3): True, (4, 3): True, (4, 4): True}
        
        self.assertEqual(viz, actual_viz) 


    def test_start_equals_finish_euclidean(self):
        maze = [
            [0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 0, 1, 0],
            [1, 0, 1, 0, 0],
            [0, 0, 0, 1, 0]
        ]
        start = (2, 2)
        finish = (2, 2)
        num_steps, viz = lab1_v2.greedy(maze, start, finish)
        
        self.assertTrue(viz == {(2, 2): True}) 


    def test_one_horizontal_line_maze_euclidean(self):
        maze = [[0, 0, 0, 0, 0]]
        start = (0, 0)
        finish = (0, 4)

        num_steps, viz = lab1_v2.greedy(maze, start, finish)

        actual_viz = {(0, 0): True, (0, 1): True, (0, 2): True, (0, 3): True, (0, 4): True}
        self.assertEqual(viz, actual_viz)

    
    def test_one_vertical_line_maze_euclidean(self):
        maze = [[0], [0], [0], [0], [0]]
        start = (0, 0)
        finish = (4, 0)

        num_steps, viz = lab1_v2.greedy(maze, start, finish)

        actual_viz = {(0, 0): True, (1, 0): True, (2, 0): True, (3, 0): True, (4, 0): True}
        self.assertEqual(viz, actual_viz)

    def test_large_open_maze_euclidean(self):
        maze = [[0] * 30 for _ in range(30)]
        start = (0, 0)
        finish = (29, 29)
        num_steps, viz = lab1_v2.greedy(maze, start, finish)

        actual_viz = {(0, 0): True, (1, 0): True, (1, 1): True, (2, 1): True, (2, 2): True, 
                      (3, 2): True, (3, 3): True, (4, 3): True, (4, 4): True, (5, 4): True, 
                      (5, 5): True, (6, 5): True, (6, 6): True, (7, 6): True, (7, 7): True, 
                      (8, 7): True, (8, 8): True, (9, 8): True, (9, 9): True, (10, 9): True, 
                      (10, 10): True, (11, 10): True, (11, 11): True, (12, 11): True, 
                      (12, 12): True, (13, 12): True, (13, 13): True, (14, 13): True, (14, 14): True, 
                      (15, 14): True, (15, 15): True, (16, 15): True, (16, 16): True, (17, 16): True, 
                      (17, 17): True, (18, 17): True, (18, 18): True, (19, 18): True, (19, 19): True, 
                      (20, 19): True, (20, 20): True, (21, 20): True, (21, 21): True, (22, 21): True, 
                      (22, 22): True, (23, 22): True, (23, 23): True, (24, 23): True, (24, 24): True, 
                      (25, 24): True, (25, 25): True, (26, 25): True, (26, 26): True, (27, 26): True, 
                      (27, 27): True, (28, 27): True, (28, 28): True, (29, 28): True, (29, 29): True}
        
        self.assertEqual(viz, actual_viz)


    def test_random_obstacles_euclidean(self):
        maze = [
            [0, 1, 0, 1, 0],
            [0, 0, 0, 1, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1],
            [0, 1, 0, 0, 0]
        ]
        start = (0, 0)
        finish = (4, 4)
        num_steps, viz = lab1_v2.greedy(maze, start, finish)

        actual_viz = {(0, 0): True, (1, 0): True, (1, 1): True, (1, 2): True, (2, 2): True, 
                      (3, 2): True, (4, 2): True, (4, 3): True, (4, 4): True}

        self.assertEqual(viz, actual_viz)


    def test_fully_blocked_euclidean(self):
        maze = [
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1]
        ]
        start = (0, 0)
        finish = (4, 4)
        num_steps, viz = lab1_v2.greedy(maze, start, finish)
        self.assertEqual(viz, -1)


    def test_entirely_empty_euclidean(self):
        maze = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        start = (0, 0)
        finish = (4, 4)
        num_steps, viz = lab1_v2.greedy(maze, start, finish)

        actual_viz = {(0, 0): True, (1, 0): True, (1, 1): True, (2, 1): True, (2, 2): True, 
                      (3, 2): True, (3, 3): True, (4, 3): True, (4, 4): True}
        
        self.assertEqual(viz, actual_viz)


    def test_edge_case_1x1_euclidean(self):
        maze = [[0]]
        start = (0, 0)
        finish = (0, 0)
        num_steps, viz = lab1_v2.greedy(maze, start, finish)
        
        self.assertEqual(viz, {(0, 0): True})

    def test_simple_open_path_manhattan(self):
        maze = [
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 1, 0, 1, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0]
        ]
        start = (0, 0)
        finish = (4, 4)
        num_steps, viz = lab1_v2.greedy(maze, start, finish, "manhattan")

        actual_viz = {(0, 0): True, (1, 0): True, (2, 0): True, (3, 0): True, (4, 0): True, 
                      (4, 1): True, (4, 2): True, (3, 2): True, (3, 3): True, (3, 4): True, (4, 4): True}
        
        self.assertEqual(viz, actual_viz)


    # def test_completely_blocked_path_manhattan(self):
    #     maze = [
    #         [0, 1, 1, 1, 0],
    #         [0, 1, 0, 1, 0],
    #         [0, 1, 0, 1, 0],
    #         [0, 1, 0, 1, 0],
    #         [0, 1, 1, 1, 0]
    #     ]
    #     start = (0, 0)
    #     finish = (4, 4)
    #     num_steps, viz = lab1_v2.greedy(maze, start, finish)
   
    #     actual_viz = -1
    #     self.assertEqual(viz, actual_viz)


    # def test_one_paths_available_manhattan(self):
    #     maze = [
    #         [0, 0, 0, 1, 0],
    #         [1, 1, 0, 1, 0],
    #         [0, 0, 0, 1, 0],
    #         [0, 1, 1, 1, 0],
    #         [0, 0, 0, 0, 0]
    #     ]
    #     start = (0, 0)
    #     finish = (4, 4)
    #     num_steps, viz = lab1_v2.greedy(maze, start, finish)

    #     actual_viz = {(0, 0): True, (0, 1): True, (0, 2): True, (1, 2): True, (2, 2): True, 
    #                   (2, 1): True, (2, 0): True, (3, 0): True, (4, 0): True, (4, 1): True, 
    #                   (4, 2): True, (4, 3): True, (4, 4): True}
        
    #     self.assertEqual(viz, actual_viz) 


    # def test_one_narrow_path_manhattan(self):
    #     maze = [
    #         [0, 1, 1, 1, 1],
    #         [0, 0, 0, 0, 1],
    #         [1, 1, 1, 0, 1],
    #         [1, 1, 1, 0, 1],
    #         [1, 1, 1, 0, 0]
    #     ]
    #     start = (0, 0)
    #     finish = (4, 4)
    #     num_steps, viz = lab1_v2.greedy(maze, start, finish)
   
    #     actual_viz = {(0, 0): True, (1, 0): True, (1, 1): True, (1, 2): True, (1, 3): True, 
    #                   (2, 3): True, (3, 3): True, (4, 3): True, (4, 4): True}
        
    #     self.assertEqual(viz, actual_viz) 


    # def test_start_equals_finish_manhattan(self):
    #     maze = [
    #         [0, 1, 0, 1, 0],
    #         [0, 1, 0, 1, 0],
    #         [0, 0, 0, 1, 0],
    #         [1, 0, 1, 0, 0],
    #         [0, 0, 0, 1, 0]
    #     ]
    #     start = (2, 2)
    #     finish = (2, 2)
    #     num_steps, viz = lab1_v2.greedy(maze, start, finish)
        
    #     self.assertTrue(viz == {(2, 2): True}) 


    # def test_one_horizontal_line_maze_manhattan(self):
    #     maze = [[0, 0, 0, 0, 0]]
    #     start = (0, 0)
    #     finish = (0, 4)

    #     num_steps, viz = lab1_v2.greedy(maze, start, finish)

    #     actual_viz = {(0, 0): True, (0, 1): True, (0, 2): True, (0, 3): True, (0, 4): True}
    #     self.assertEqual(viz, actual_viz)

    
    # def test_one_vertical_line_maze_manhattan(self):
    #     maze = [[0], [0], [0], [0], [0]]
    #     start = (0, 0)
    #     finish = (4, 0)

    #     num_steps, viz = lab1_v2.greedy(maze, start, finish)

    #     actual_viz = {(0, 0): True, (1, 0): True, (2, 0): True, (3, 0): True, (4, 0): True}
    #     self.assertEqual(viz, actual_viz)

    # def test_large_open_maze_manhattan(self):
    #     maze = [[0] * 30 for _ in range(30)]
    #     start = (0, 0)
    #     finish = (29, 29)
    #     num_steps, viz = lab1_v2.greedy(maze, start, finish)

    #     actual_viz = {(0, 0): True, (1, 0): True, (1, 1): True, (2, 1): True, (2, 2): True, 
    #                   (3, 2): True, (3, 3): True, (4, 3): True, (4, 4): True, (5, 4): True, 
    #                   (5, 5): True, (6, 5): True, (6, 6): True, (7, 6): True, (7, 7): True, 
    #                   (8, 7): True, (8, 8): True, (9, 8): True, (9, 9): True, (10, 9): True, 
    #                   (10, 10): True, (11, 10): True, (11, 11): True, (12, 11): True, 
    #                   (12, 12): True, (13, 12): True, (13, 13): True, (14, 13): True, (14, 14): True, 
    #                   (15, 14): True, (15, 15): True, (16, 15): True, (16, 16): True, (17, 16): True, 
    #                   (17, 17): True, (18, 17): True, (18, 18): True, (19, 18): True, (19, 19): True, 
    #                   (20, 19): True, (20, 20): True, (21, 20): True, (21, 21): True, (22, 21): True, 
    #                   (22, 22): True, (23, 22): True, (23, 23): True, (24, 23): True, (24, 24): True, 
    #                   (25, 24): True, (25, 25): True, (26, 25): True, (26, 26): True, (27, 26): True, 
    #                   (27, 27): True, (28, 27): True, (28, 28): True, (29, 28): True, (29, 29): True}
        
    #     self.assertEqual(viz, actual_viz)


    # def test_random_obstacles_manhattan(self):
    #     maze = [
    #         [0, 1, 0, 1, 0],
    #         [0, 0, 0, 1, 0],
    #         [1, 1, 0, 0, 0],
    #         [0, 0, 0, 1, 1],
    #         [0, 1, 0, 0, 0]
    #     ]
    #     start = (0, 0)
    #     finish = (4, 4)
    #     num_steps, viz = lab1_v2.greedy(maze, start, finish)

    #     actual_viz = {(0, 0): True, (1, 0): True, (1, 1): True, (1, 2): True, (2, 2): True, 
    #                   (3, 2): True, (4, 2): True, (4, 3): True, (4, 4): True}

    #     self.assertEqual(viz, actual_viz)


    # def test_fully_blocked_manhattan(self):
    #     maze = [
    #         [1, 1, 1, 1, 1],
    #         [1, 1, 1, 1, 1],
    #         [1, 1, 1, 1, 1],
    #         [1, 1, 1, 1, 1],
    #         [1, 1, 1, 1, 1]
    #     ]
    #     start = (0, 0)
    #     finish = (4, 4)
    #     num_steps, viz = lab1_v2.greedy(maze, start, finish)
    #     self.assertEqual(viz, -1)


    # def test_entirely_empty_manhattan(self):
    #     maze = [
    #         [0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0]
    #     ]
    #     start = (0, 0)
    #     finish = (4, 4)
    #     num_steps, viz = lab1_v2.greedy(maze, start, finish)

    #     lab1_v2.visualize_animation(viz, maze)
    #     actual_viz = {(0, 0): True, (1, 0): True, (1, 1): True, (2, 1): True, (2, 2): True, 
    #                   (3, 2): True, (3, 3): True, (4, 3): True, (4, 4): True}
        
    #     self.assertEqual(viz, actual_viz)


    # def test_edge_case_1x1_manhattan(self):
    #     maze = [[0]]
    #     start = (0, 0)
    #     finish = (0, 0)
    #     num_steps, viz = lab1_v2.greedy(maze, start, finish)
        
    #     self.assertEqual(viz, {(0, 0): True})

def run_tests():
    pytest.main(["-s", "/home/yermukhamed/Desktop/EARIN/EARIN-labs/lab1_tests.py"])

if __name__ == "__main__":
    run_tests()
