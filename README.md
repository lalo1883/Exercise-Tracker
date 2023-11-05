
---

# Workout Tracker App

Workout Tracker App is a simple Python application that allows users to track their exercises using natural language input and store the workout data in a spreadsheet.

## Prerequisites

Before you begin, ensure you have the following requirements installed:

- Python 3
- Requests library (install using `pip install requests`)

## Getting Started

1. Clone the repository to your local machine:

   ```
   git clone <repository-url>
   ```

2. Navigate to the project directory:

   ```
   cd workout-tracker-app
   ```

3. Run the application:

   ```
   python workout_tracker.py
   ```

## Usage

1. Run the application using the above instructions.

2. When prompted, enter the exercise you have done in natural language format.

3. The application will send a request to the Nutritionix API to get exercise details.

4. The exercise details (duration, calories burned) will be stored in a spreadsheet using the Sheety API.

## Configuration

Replace `'Your api Key'` in the `workout_tracker.py` file with your actual API key from Nutritionix and Sheety.

```python
API_KEY = 'Your api Key'
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License



---

Feel free to modify the content and structure of the README according to your specific project details and requirements.
