# tests/test_weather_forecast_app.py

def test_main_function():
    # This test will check if the main function runs without errors.
    try:
        from weather_forecast_app import main
        main()
        assert True
    except Exception as e:
        print(f"Test failed with error: {e}")
        assert False
