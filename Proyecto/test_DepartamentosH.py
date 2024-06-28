import unittest
from unittest.mock import patch
import TotalDepartamentos
import DepartamentosH

class TestDepartamentosH(unittest.TestCase):

    @patch('builtins.input', side_effect=["admin", "admin123", "1", "04011999", "N"])
    def test_valid_credentials_and_option_1(self, mock_input):
        with patch('os.system') as mock_os:
            DepartamentosH.main()
            mock_os.assert_called_with('cls' if os.name == 'nt' else 'clear')
    
    @patch('builtins.input', side_effect=["admin", "admin123", "2", "04011999", "N"])
    def test_valid_credentials_and_option_2(self, mock_input):
        with patch('os.system') as mock_os:
            DepartamentosH.main()
            mock_os.assert_called_with('cls' if os.name == 'nt' else 'clear')
    
    @patch('builtins.input', side_effect=["admin", "wrong_password"])
    def test_invalid_credentials(self, mock_input):
        with patch('os.system') as mock_os:
            DepartamentosH.main()
            mock_os.assert_not_called()
    
    @patch('builtins.input', side_effect=["admin", "admin123", "3"])
    def test_invalid_option(self, mock_input):
        with patch('os.system') as mock_os:
            DepartamentosH.main()
            mock_os.assert_not_called()

if __name__ == '__main__':
    unittest.main()