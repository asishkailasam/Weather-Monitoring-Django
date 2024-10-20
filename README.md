# Real-Time Weather Monitoring System

## Project Overview

This Django-based real-time weather monitoring system retrieves weather data for major metros in India (Delhi, Mumbai, Chennai, Bangalore, Kolkata, Hyderabad) from the OpenWeatherMap API. The system provides weather summaries with rollups and aggregates, supports user-configurable alert thresholds, and includes visualization for trends and alerts.

## Features

- Retrieve real-time weather data every 5 minutes.
- Weather data includes:
  - Main weather condition (e.g., Rain, Clear)
  - Temperature (converted to Celsius)
  - Feels-like temperature
- Daily weather summaries:
  - Average, Maximum, and Minimum temperatures.
  - Dominant weather condition.
- User-configurable alert thresholds for temperature and weather conditions.
- Visualizations for weather summaries, historical trends, and alerts.
- Optional email notifications for triggered alerts.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/weather-monitoring.git
    cd weather-monitoring
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up the Django project:
    ```bash
    python manage.py migrate
    ```

5. Add your OpenWeatherMap API key in the settings file:
    - Open `weather_monitoring/settings.py`.
    - Find the `OPENWEATHERMAP_API_KEY` variable and add your API key:
      ```python
      OPENWEATHERMAP_API_KEY = 'your_api_key_here'
      ```

6. Start the development server:
    ```bash
    python manage.py runserver
    ```

## Celery Setup (For Scheduling Tasks)

1. Install Redis (used as the message broker):
   - On Ubuntu:
     ```bash
     sudo apt install redis-server
     ```
   - On Windows, follow instructions [here](https://redis.io/docs/getting-started/installation/).

2. Start the Redis server:
   ```bash
   redis-server
3.Start Celery worker:
celery -A weather_monitoring worker --loglevel=info

4.Start Celery beat for scheduling:
celery -A weather_monitoring beat --loglevel=info
URL Endpoints
Weather Summary: /weather/summary/
Weather Alerts: /weather/alerts/

Testing
1.Run test cases to verify functionality
python manage.py test

Optional Features
Email Notifications: Set up the email configuration in settings.py if you want to send alerts via email.
EMAIL_HOST_USER = 'your_email@gmail.com'
EMAIL_HOST_PASSWORD = 'your_email_password'


