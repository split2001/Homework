import unittest
import test_runner2
import test2


testik = unittest.TestSuite()
testik.addTest(unittest.TestLoader().loadTestsFromTestCase(test2.RunnerTest))
testik.addTest(unittest.TestLoader().loadTestsFromTestCase(test_runner2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(testik)



