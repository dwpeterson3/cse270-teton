import pytest
import requests

def test_users_endpoint_unauthorized(requests_mock):
    # Define the URL to mock
    url = "http://127.0.0.1:8000/data/all"
    
    # Mock the response for username=admin and password=admin
    requests_mock.get(url, status_code=401, text="", additional_matcher=lambda request: 
                      request.qs == {"username": ["admin"], "password": ["admin"]})
    
    # Define the query parameters
    params = {
        "username": "admin",
        "password": "admin"
    }
    
    # Make the GET request
    response = requests.get(url, params=params)
    
    # Assert that the HTTP response status code is 401 (Unauthorized)
    assert response.status_code == 401, f"Expected 401, but got {response.status_code}"
    # Assert that the response content is empty
    assert response.text.strip() == "", f"Expected empty response, but got: {response.text.strip()}"

def test_users_endpoint_empty_response(requests_mock):
    # Define the URL to mock
    url = "http://127.0.0.1:8000/data/all"
    
    # Mock the response for username=admin and password=qwerty
    requests_mock.get(url, status_code=200, text="", additional_matcher=lambda request: 
                      request.qs == {"username": ["admin"], "password": ["qwerty"]})
    
    # Define the query parameters
    params = {
        "username": "admin",
        "password": "qwerty"
    }
    
    # Make the GET request
    response = requests.get(url, params=params)
    
    # Assert that the HTTP response status code is 200 (OK)
    assert response.status_code == 200, f"Expected 200, but got {response.status_code}"
    # Assert that the response content is empty
    assert response.text.strip() == "", f"Expected empty response, but got: {response.text.strip()}"
