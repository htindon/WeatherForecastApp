# tests/test_weather_forecast_app.py

import pytest
import requests
import weather_forecast_app

def test_main_function():
    # This test will check if the main function runs without errors.
    try:
        weather_forecast_app.main()  # Run the main function to see if there are any errors
        assert True  # If no errors occur, the test is successful
    except Exception as e:
        pytest.fail(f"Test failed with error: {e}")

# Here we will mock the API call as we're not testing the actual API yet
def test_weather_data_structure():
    # Assuming our API response should have these keys
    expected_keys = ["temperature", "humidity", "description"]

    weather_data = weather_forecast_app.get_weather_data()

    # Check if the response contains all the expected keys
    for key in expected_keys:
        assert key in weather_data, f"Key {key} is missing from the weather data"
