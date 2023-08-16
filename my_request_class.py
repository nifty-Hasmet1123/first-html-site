import requests

class MyRequest():
    def __init__(self, url):
        self.url = url
        self._response = None

    def _validate_if_response_is_success(self):
        response = requests.get(self.url, timeout = 20)

        if response.ok:
            self._response = response.text
            return "Success"
        return "Failed"
    
    def request_text(self):
        validator = self._validate_if_response_is_success()

        if validator == "Success":
            return self._response
        elif validator == "Failed":
            return requests.HTTPError({"error": "Failed request"})      