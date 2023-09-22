"""Unit Testing for Test data loader
"""
# test_data_loader.py
import sys
import unittest

sys.path.append('/workspaces/docker_python')
from weather_model.src.data_loader import load_humidity_data, load_temperature_data

class TestDataLoader(unittest.TestCase):
    """Unit Testing class

    Args:
        unittest (_type_): _description_
    """
    def test_load_humidity_data(self):
        """Test the load humity data 
        """
        # Test case for load_humidity_data function
        # You can write test cases to verify the behavior of this function
        # For example, test if it loads data correctly and if the shape is as expected
        humidity_data = load_humidity_data()
        self.assertIsNotNone(humidity_data)  # Check if data is not None
        self.assertEqual(humidity_data.shape, (1588, 4))  # Replace with actual expected shape

if __name__ == '__main__':
    unittest.main()