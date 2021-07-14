from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/<name>")
def home(name):
    return render_template("homepage.html", name=name)


@app.route("/loops/<int:number>")
def loops(number):
    return render_template("loops.html", number=number)


@app.route("/multiply/<int:number>")
def multiply(number):
    return render_template("multiply.html", number=number)


# @app.route("/image/<filename>")
# def image(filename):
#     return url_for("static", filename=filename)
#

if __name__ == "__main__":
    app.debug = True
    app.run()
