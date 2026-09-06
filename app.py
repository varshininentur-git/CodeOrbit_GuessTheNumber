from flask import Flask, redirect, render_template, request, session, url_for
import random

app = Flask(__name__)
# Flask uses this key to sign the session cookie.
app.secret_key = "beginner-number-game-secret-key"


def start_new_game():
    """Create the session values needed for a fresh round."""
    session["secret_number"] = random.randint(1, 100)
    session["attempts"] = 0
    session["game_over"] = False


@app.route("/", methods=["GET", "POST"])
def index():
    # Start a game automatically when the player first opens the page.
    if "secret_number" not in session:
        start_new_game()

    message = None
    message_type = None

    if request.method == "POST":
        # The Play Again button starts a new round and clears the old result.
        if request.form.get("action") == "new_game":
            start_new_game()
            return redirect(url_for("index"))

        # Do not accept more guesses after the round has been won.
        if session.get("game_over"):
            message = "Start a new game to keep playing."
            message_type = "info"
        else:
            guess_text = request.form.get("guess", "").strip()

            # Convert the form text safely so letters do not crash the app.
            try:
                guess = int(guess_text)
            except ValueError:
                message = "Please enter a valid number."
                message_type = "error"
            else:
                if guess < 1 or guess > 100:
                    message = "Please enter a number between 1 and 100."
                    message_type = "error"
                else:
                    session["attempts"] += 1

                    if guess < session["secret_number"]:
                        message = "Too low! Try again."
                        message_type = "hint"
                    elif guess > session["secret_number"]:
                        message = "Too high! Try again."
                        message_type = "hint"
                    else:
                        message = "Congratulations! You guessed the number!"
                        message_type = "success"
                        session["game_over"] = True

    return render_template(
        "index.html",
        message=message,
        message_type=message_type,
        attempts=session.get("attempts", 0),
        game_over=session.get("game_over", False),
    )


if __name__ == "__main__":
    app.run(debug=True)
