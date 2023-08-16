from my_request_class import MyRequest
from unittest.mock import Mock, patch
import unittest

class MyRequestTest(unittest.TestCase):
    @patch("requests.get")
    def test_validation_of_response_if_successful(self, mock_get):
        url_path = "https://www.britannica.com/topic/list-of-games-2072482"

        mock_get.return_value.ok = True
        my_instance = MyRequest(url_path)
        self.assertEqual(
            my_instance._validate_if_response_is_success(),
            "Success"
        )
    
    @patch("requests.get")
    def test_validation_of_response_if_not_successful(self, mock_get):
        url_path = "https://www.britannica.com/topic/list-of-games-2072482"

        mock_get.return_value.ok = False
        my_instance = MyRequest(url_path)
        self.assertEqual(
            my_instance._validate_if_response_is_success(),
            "Failed"
        )

    @patch("requests.get")
    def test_request_text_if_success(self, mock_get):
        url_path = "https://www.example.com"
        
        mock_response = Mock()
        mock_response.ok = True
        mock_response.text = "Mock response text"
        mock_get.return_value = mock_response
        
        my_instance = MyRequest(url_path)
        result = my_instance.request_text()
        
        self.assertEqual(result, "Mock response text")

    # @patch("requests.get")
    # @patch("requests.HTTPError")
    # def test_request_text_if_failed(self, mock_error, mock_get):
    #     url_path = "https://www.example.com"
        
    #     mock_response = Mock()
    #     mock_response.ok = False
    #     mock_get.return_value = mock_response
        
    #     # Configure the mock_error to be raised when calling the constructor of HTTPError
    #     mock_error_instance = Mock()
    #     mock_error.return_value = mock_error_instance
        
    #     my_instance = MyRequest(url_path)
        
    #     # Manually raise the HTTPError instance
    #     mock_error_instance.side_effect = requests.HTTPError("Failed request")
        
    #     with self.assertRaises(requests.HTTPError):
    #         my_instance.request_text()