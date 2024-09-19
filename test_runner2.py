import unittest
from runner2 import *


class TournamentTest(unittest.TestCase):
    is_frozen = True

    def setUp(self):
        self.runner = Runner('Усэйн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_start1(self):
        tour = Tournament(90, self.runner, self.runner3)
        result = tour.start()
        self.all_results['Тест1'] = result
        self.assertTrue(max(self.all_results.keys()), self.runner3)

    @unittest.skipIf(is_frozen == True,'Тесты в этом кейсе заморожены')
    def test_start2(self):
        tour2 = Tournament(90, self.runner2, self.runner3)
        result = tour2.start()
        self.all_results['Тест2'] = result
        self.assertTrue(max(self.all_results.keys()), self.runner3)

    @unittest.skipIf(is_frozen == True,'Тесты в этом кейсе заморожены')
    def test_start3(self):
        tour3 = Tournament(90, self.runner, self.runner2, self.runner3)
        result = tour3.start()
        self.all_results['Тест3'] = result
        self.assertTrue(max(self.all_results.keys()), self.runner3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f'{key}:{value}\n')


if __name__ == '__main__':
    unittest.main()
