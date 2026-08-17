from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/calculate", methods=["POST"])
def calculate():
    electricity = float(request.form["electricity"])
    transport = float(request.form["transport"])
    cooking = float(request.form["cooking"])

    electricity_emission = electricity * 0.82
    transport_emission = transport * 0.12
    cooking_emission = cooking * 2.3

    total = electricity_emission + transport_emission + cooking_emission

    return render_template(
        "index.html",
        total=round(total, 2)
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)