import unittest

# Discover and run all tests in the tests/ directory
loader = unittest.TestLoader()
suite = loader.discover('tests')

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)

# Exit with a non-zero status if there were test failures
if not result.wasSuccessful():
    exit(1)
