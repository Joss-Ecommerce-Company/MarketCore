#!/usr/bin/env python3
import unittest

from . import (
    TestPasswordManagerCase,
    TestFlaskSQLAlchemy
)

suite = unittest.TestSuite()
suite.addTests([
    unittest.defaultTestLoader.loadTestsFromTestCase(TestPasswordManagerCase),
    unittest.defaultTestLoader.loadTestsFromTestCase(TestFlaskSQLAlchemy)
])

runner = unittest.TextTestRunner()
runner.run(suite)
