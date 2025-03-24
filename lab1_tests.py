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
        self.assertTrue(8,num_steps)

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
        lab1_v2.visualize_animation(viz, maze)
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
        lab1_v2.visualize_animation(viz, maze)
        self.assertTrue(num_steps==1) 

if __name__ == "__main__":
    unittest.main()

def run_tests():
    suite = unittest.TestLoader().loadTestsFromModule(TestMazeSolver)
    unittest.TextTestRunner(verbosity=2).run(suite)