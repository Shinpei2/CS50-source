from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        name = request.args.get("foo", "Name")
        name2 = "foo2"
        return render_template("index.html", foo=name, foo2=name2)

    else:
        name = request.form["test"]
        print(request.form["test"])
        return render_template("index.html", foo2=name)


if __name__ == "__main__":
    app.run(debug = True)