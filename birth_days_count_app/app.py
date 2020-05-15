from flask import Flask
from flask import render_template
from flask import request
from days_from_birth import calc

app = Flask(__name__)

@app.route("/calc", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        birth_date = request.form["birth"]
        days = calc(birth_date)
        return render_template("result.html", days=days)
    else:
        return render_template("form.html")
