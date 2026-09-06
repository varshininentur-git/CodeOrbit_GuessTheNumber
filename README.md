# 🎯 Guess the Number

A simple and interactive **Guess the Number web game** built using Python, Flask, HTML, and CSS. The application generates a random number between 1 and 100, and the player tries to guess it using hints such as **"Too high!"** or **"Too low!"**.

## ✨ Features

* 🎲 Generates a random number between 1 and 100
* 🔢 Allows the user to enter guesses
* ⬆️ Displays **"Too high!"** when the guess is too high
* ⬇️ Displays **"Too low!"** when the guess is too low
* 🎉 Displays a congratulations message when the correct number is guessed
* 📊 Tracks the number of attempts
* 🔄 Allows the user to play multiple rounds
* 🚫 Validates numbers outside the 1–100 range
* ⚠️ Handles invalid user input
* 🎨 Clean and responsive web interface
* 🌐 Built as a Flask web application

## 🛠️ Technologies Used

| Technology    | Purpose                            |
| ------------- | ---------------------------------- |
| Python        | Game logic                         |
| Flask         | Web framework                      |
| HTML5         | Webpage structure                  |
| CSS3          | Styling                            |
| Random Module | Generate the secret number         |
| Flask Session | Maintain game data between guesses |

## 📁 Project Structure

```text
CodeOrbit-Task2/
│
├── app.py
├── requirements.txt
├── .gitignore
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── README.md
```

## ⚙️ How It Works

1. The application generates a random number between **1 and 100**.
2. The player enters a guess.
3. The application compares the guess with the secret number.
4. If the guess is too low, the application displays **"Too low! Try again."**
5. If the guess is too high, the application displays **"Too high! Try again."**
6. If the guess is correct, the application displays a congratulations message.
7. The number of attempts is tracked throughout the round.
8. After winning, the player can click **Play Again** to start a new round.

## 🎮 How to Play

Enter a number between **1 and 100**.

For example:

```text
Enter your guess: 50
```

If the secret number is higher:

```text
Too low! Try again.
Attempts: 1
```

If the secret number is lower:

```text
Too high! Try again.
Attempts: 2
```

Continue guessing until you find the correct number.

When you guess correctly:

```text
🎉 Congratulations!
You guessed the number!

Total attempts: 5
```

Click **Play Again** to start a new round.

## 🚨 Error Handling

The application handles invalid inputs.

### Invalid Input

If the user enters text instead of a number:

```text
Please enter a valid number.
```

### Number Outside the Range

If the user enters a number below 1 or above 100:

```text
Please enter a number between 1 and 100.
```

The application handles these errors without crashing.

## 🎲 Random Number Generation

Python's built-in `random` module is used to generate the secret number.

```python
random.randint(1, 100)
```

This generates a random integer between 1 and 100.

## 📊 Attempt Tracking

The application keeps track of how many guesses the player has made during the current round.

For example:

```text
Guess 1 → Too low
Guess 2 → Too high
Guess 3 → Too low
Guess 4 → Correct!

Total attempts: 4
```

## 🔄 Multiple Rounds

After successfully guessing the number, the player can click **Play Again**.

A new random number is generated and the attempt counter is reset.

This allows the user to play the game multiple times.

## 💻 Installation

Clone the repository:

```bash
git clone <your-repository-url>
```

Go into the project folder:

```bash
cd CodeOrbit-Task2
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate the virtual environment:

```bash
source .venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

Start the Flask application:

```bash
python3 app.py
```

You should see:

```text
* Running on http://127.0.0.1:5000
```

Open the following address in your browser:

```text
http://127.0.0.1:5000
```

## 🧪 Example

```text
        GUESS THE NUMBER

Guess a number between 1 and 100.

        [     50     ]

          [ GUESS ]

        Too low!

        Attempts: 1
```

After guessing correctly:

```text
        🎉 Congratulations!

You guessed the number!

        Total attempts: 6

        [ PLAY AGAIN ]
```

## 🎯 Learning Objectives

This project demonstrates:

* Python programming
* Flask web development
* HTML forms
* CSS styling
* Random number generation
* Conditional statements
* User input handling
* Exception handling
* Attempt counting
* Flask sessions
* Connecting a Python backend with an HTML frontend

## 🚀 Future Improvements

Possible future improvements include:

* Add difficulty levels
* Add a limited number of attempts
* Add a score system
* Add a timer
* Add a leaderboard
* Add sound effects
* Add animations
* Add dark mode
* Add JavaScript for a more interactive experience
