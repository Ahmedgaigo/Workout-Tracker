# Workout-Tracker
This script appears to be a Python code that tracks and logs workouts using the Nutritionix API and Sheety API. Here's a breakdown of what the code does:

1. It imports the necessary modules: `requests` for making HTTP requests and `datetime` for working with dates and times.

2. It defines several constants like `GENDER`, `WEIGHT`, `HEIGHT`, and `AGE` that represent the user's personal information.

3. It sets up the endpoints for the Nutritionix API (`exercise_endpoint`) and the Sheety API (`sheety_endpoint`).

4. It prompts the user to input the exercise they did.

5. It prepares the exercise parameters by creating a dictionary (`exercise_param`) containing the query, user information, and API keys.

6. It sets up the headers for the Nutritionix API request, including the `APP_ID` and `API_KEY`.

7. It sends a POST request to the exercise endpoint of the Nutritionix API, passing the exercise parameters and headers.

8. It retrieves the response from the Nutritionix API and converts it to JSON format.

9. It gets the current date and time using `datetime.now()`.

10. It extracts the exercise details from the response and iterates over each exercise.

11. For each exercise, it creates a dictionary (`sheety_param`) containing the workout details like date, time, exercise name, duration, and calories.

12. It sends a POST request to the Sheety API's workout endpoint, passing the workout details as JSON in the request body.

13. It prints the response from the Sheety API.

The Nutritionix API employs Natural Language Processing(NLP) techniques to analyze the query and determine the exercise being performed. It then returns a response containing exercise details such as the exercise name, duration, and calories burned.
