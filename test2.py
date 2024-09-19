import unittest
from runner import *


class RunnerTest(unittest.TestCase):
    is_frozen = False

    def setUp(self):
        self.walker = Runner('bob')
        self.runner = Runner('not_bob')

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        for i in range(10):
            self.walker.walk()
        self.assertEqual(self.walker.distance, 50)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        for i in range(10):
            self.runner.run()
        self.assertEqual(self.runner.distance, 100)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        for i in range(10):
            self.walker.walk()
            self.runner.run()
        self.assertNotEqual(self.walker.distance, self.runner.distance)


if __name__ == '__main__':
    unittest.main()
