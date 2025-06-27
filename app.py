from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def calculator():
    expression = ""
    result = ""

    if request.method == "POST":
        expression = request.form["expression"]
        button = request.form["button"]

        if button == "C":
            expression = ""
        elif button == "=":
            try:
                result = str(eval(expression))
                expression = result
            except Exception:
                result = "Hiba"
                expression = "Hiba"
        else:
            expression += button

    return render_template("index.html", expression=expression)


if __name__ == "__main__":
    app.run(debug=True)
