from flask import Flask, render_template
import database

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html", data=database.get_all())


if __name__ == "__main__":
    app.run(debug=True)
