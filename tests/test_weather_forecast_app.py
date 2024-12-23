# tests/test_weather_forecast_app.py

import pytest

def test_main_function():
    # This test will check if the main function runs without errors.
    try:
        from weather_forecast_app import main
        main()  # Run the main function to see if there are any errors
        assert True  # If no errors occur, the test is successful
    except Exception as e:
        pytest.fail(f"Test failed with error: {e}")
