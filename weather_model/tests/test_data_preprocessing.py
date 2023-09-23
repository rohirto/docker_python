"""
Test Module for data Preprocessing

Make this tests from Experimenting in the notebook and chatgpt
"""
import sys
import unittest
import pandas as pd

sys.path.append('/workspaces/docker_python')
from weather_model.src.data_preprocessing import data_evaluation, preprocess_data

class TestDataProcessing(unittest.TestCase):
    """Unit testing class for Data processing 

    Args:
        unittest (_type_): _description_
    """
    def test_shape(self):
        """Test the shape
        """
        data = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Age': [25, 30]})
        expected_output = "Shape: (2, 2)"

        # Redirect stdout to capture the print output
        with self.assertLogs() as cm_n:
            data_evaluation(data)

        self.assertIn(expected_output, cm_n.output)

    def test_head(self, n_n=5):
        """_summary_

        Args:
            n_n (count, optional): Count of head. Defaults to 5.
        """
        data = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Age': [25, 30]})
        expected_output = "Head:\n   Name  Age\n0  Alice   25\n1    Bob   30"
        
        with self.assertLogs() as cm_n:
            data_evaluation(data)
        
        self.assertIn(expected_output, cm_n.output)

    def test_summary_statistics(self):
        data = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Age': [25, 30]})
        expected_output = "Summary Statistics:\n            Age\ncount   2.000000\nmean   27.500000\nstd     3.535534\nmin    25.000000\n25%    26.250000\n50%    27.500000\n75%    28.750000\nmax    30.000000"
        
        with self.assertLogs() as cm:
            data_evaluation(data)
        
        self.assertIn(expected_output, cm.output)

    def test_columns(self):
        data = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Age': [25, 30]})
        expected_output = "Columns:\nIndex(['Name', 'Age'], dtype='object')"
        
        with self.assertLogs() as cm:
            data_evaluation(data)
        
        self.assertIn(expected_output, cm.output)

if __name__ == '__main__':
    unittest.main()