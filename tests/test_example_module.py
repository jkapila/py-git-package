import unittest
from sourcecode import BaseExceptions, ExampleModule

from .base import BaseTestCase


class TestExampleModule(BaseTestCase):
    """Testing operation of the ExampleModule class"""

    def test_init_example_module(self):
        """Ensures that the twine class can be instantiated with a file"""
        test_data_file = self.path + "test_data/.json"
        try:
            mod = ExampleModule()
            mod = mod.__repr__() + test_data_file
            print(mod)
        except BaseExceptions:
            raise ValueError("An Error is raised here")


if __name__ == "__main__":
    unittest.main()
