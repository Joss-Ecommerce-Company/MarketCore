#!/usr/bin/env python3
import unittest

from . import (
    TestPasswordManagerCase
)

suite = unittest.TestSuite()
suite.addTests([
    unittest.defaultTestLoader.loadTestsFromTestCase(TestPasswordManagerCase)
])

runner = unittest.TextTestRunner()
runner.run(suite)
