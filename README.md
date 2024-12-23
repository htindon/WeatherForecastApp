# WeatherForecastApp
 A Python Weather App that provides weather information using an API, with test-driven development and modular structure.

## Overview

This project is a simple **Weather Application** built with Python that provides users with current weather information based on their location. The app interacts with a third-party weather API to fetch weather data, which is then displayed in a user-friendly format.

This application is built with a test-driven development (TDD) approach, using Python to ensure functionality, scalability, and code reliability. Throughout the development process, I will be documenting the steps taken and reflecting on challenges and learning experiences.

## Why I'm Building This App

As an aspiring developer, I want to build a practical application that showcases my programming skills while also allowing me to practice best development practices such as test-driven development, version control (via Git and GitHub), and working with third-party APIs.

The Weather App is a project that will help me:

- Learn how to interact with external APIs.
- Practice building a user-friendly application with a command-line interface (CLI).
- Implement test-driven development (TDD) to ensure quality and reliability.
- Build a solid foundation for my personal portfolio to showcase future work.

This is the first in a series of projects that I will create to improve my rusty coding skills and contribute to my GitHub portfolio.

## Features

- **Current Weather Info**: Displays temperature, humidity, weather conditions, and wind speed.
- **Location-Based Forecast**: Users can enter a city name to get weather information for that location.
- **Unit Conversion**: The app will allow the user to toggle between Celsius and Fahrenheit units.
- **Error Handling**: Clear error messages when invalid data is provided or when there's an issue fetching the weather data.

## Technologies Used

- **Python**: Main language used for development.
- **Requests**: For interacting with the weather API.
- **Pytest**: For unit testing and ensuring reliable code.
- **Git**: For version control and managing the project on GitHub.
- **OpenWeather API**: The free API used to fetch weather data.

## Installation & Setup

To run this project locally, follow these steps:

1. Clone the repository to your local machine.
   ```bash
   git clone https://github.com/yourusername/weatherforecastapp.git
   ```
2. Install required dependencies from requirements.txt
   ```bash
	pip install -r requirements.txt
   ```
3. Run the app via the command line.
   ```bash
	python weather_forecast_app.py
   ```
4. Enjoy the weather updates!