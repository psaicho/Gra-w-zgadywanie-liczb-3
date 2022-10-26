from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def game():
    if request.method == "GET":
        method = "GET"
        return render_template('Guess.html', method=method)
    else:
        method = "POST"
        choice = request.form["choice"]
        min = int(request.form["min"])
        max = int(request.form["max"])
        guess = int((max - min) / 2 + min)
        if choice == 'YOUWIN':
            return render_template('Guess.html', method=method, choice=choice)
        else:
            if choice == "TOBIG":
                max = guess
            elif choice == "TOSMALL":
                min = guess
            elif choice == "START":
                guess = guess
            guess = int((max - min) / 2 + min)
            return render_template('Guess.html', method=method, \
                                   guess=guess, min=min, max=max, choice=choice)


if __name__ == "__main__":
    app.run(debug=True, port=5020)
