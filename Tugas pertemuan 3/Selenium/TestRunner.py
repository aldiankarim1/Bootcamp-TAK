import unittest
from unittest.suite import TestSuite
import RegisterCase
import LoginCase
import CheckoutCase

if __name__ == "__main__":
    # create test suite from classes
    suite = TestSuite()

    # call test
    tests = unittest.TestLoader()

    # add test to suite
    suite.addTest(tests.loadTestsFromModule(RegisterCase))
    suite.addTest(tests.loadTestsFromModule(LoginCase))
    suite.addTest(tests.loadTestsFromModule(CheckoutCase))

    # run the test suite
    runner = unittest.TextTestRunner()
    runner.run(suite)
