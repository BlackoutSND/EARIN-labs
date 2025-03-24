import unittest
import lab1_v2

class TestMazeSolver(unittest.TestCase):
    def test_simple_open_path(self):
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
        lab1_v2.visualize_animation(viz, maze)
        print(num_steps)
        self.assertEqual(8,num_steps)

    def test_completely_blocked_path(self):
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
        #print(num_steps)
        self.assertEqual(num_steps==-1)

    def test_multiple_paths_available(self):
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
        print(num_steps)
        self.assertEqual(num_steps==13) 

    def test_one_narrow_path(self):
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
        print(num_steps)
        self.assertTrue(num_steps==9) 

    def test_start_equals_finish(self):
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
        print(num_steps)
        self.assertTrue(num_steps==1) 

    def test_one_line_maze(self):
        maze = [[0, 0, 0, 0, 0]]
        start = (0, 0)
        finish = (0, 4)

        num_steps, viz = lab1_v2.greedy(maze, start, finish)
        self.assertEqual(num_steps, 4)

    def test_large_open_maze(self):
        maze = [[0] * 30 for _ in range(30)]
        start = (0, 0)
        finish = (29, 29)
        num_steps, viz = lab1_v2.greedy(maze, start, finish)
        print(num_steps)
        self.assertEqual(num_steps, 58)

    def test_random_obstacles(self):
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
        print(num_steps)
        self.assertGreater(num_steps, 0)

    def test_fully_blocked(self):
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
        print(num_steps)
        self.assertEqual(num_steps, -1)

    def test_entirely_empty(self):
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
        print(num_steps)
        self.assertEqual(num_steps, 8)

    def test_edge_case_1x1(self):
        maze = [[0]]
        start = (0, 0)
        finish = (0, 0)
        num_steps, viz = lab1_v2.greedy(maze, start, finish)
        print(num_steps)
        self.assertEqual(num_steps, 0)

def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMazeSolver)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    run_tests()
