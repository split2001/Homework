import unittest
from runner import *


class RunnerTest(unittest.TestCase):

    def setUp(self):
        self.walker = Runner('bob')
        self.runner = Runner('not_bob')

    def test_walk(self):
        for i in range(10):
            self.walker.walk()
        self.assertEqual(self.walker.distance, 50)

    def test_run(self):
        for i in range(10):
            self.runner.run()
        self.assertEqual(self.runner.distance, 100)

    def test_challenge(self):
        for i in range(10):
            self.walker.walk()
            self.runner.run()
        self.assertNotEqual(self.walker.distance, self.runner.distance)


if __name__ == '__main__':
    unittest.main()
