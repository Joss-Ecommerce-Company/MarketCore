# Tests

- this module contains the tests for various modules of the project

1. running all the tests
```commandline
(.venv) MarketCore $ python3 -m tests
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK

```
2. add tests
```commandline
#import testCase =>> import (TestPasswordManagerCase)

#add case to the suite
suite.addTests([
 ==>>   unittest.defaultTestLoader.loadTestsFromTestCase(TestPasswordManagerCase)
])
```
