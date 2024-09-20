import logging
import unittest
from runnerwithexeptions import *

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',  encoding='utf-8',
                        format='%(asctime)s -' '%(levelname)s - %(funcName)s - %(message)s')


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            for i in range(10):
                walker = Runner('bob', -5)
                walker.walk()
            self.assertEqual(walker.distance, 50)
            logging.info('test_walk" выполнен успешно')
        except ValueError:
            logging.warning("Неверная скорость для Runner", exc_info=True)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            for i in range(10):
                runner = Runner(True, 20)
                runner.run()
            self.assertEqual(runner.distance, 100)
            logging.info('test_run выполнен успешно')
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        for i in range(10):
            walker = Runner('bob')
            runner = Runner('ne bob')
            walker.walk()
            runner.run()
        self.assertNotEqual(walker.distance, runner.distance)



