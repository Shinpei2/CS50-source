from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():
    name = request.form["name"]     # formから値を取得する
    dorm = request.form["dorm"]     # formから値を取得する
    print(name, dorm)
    if not name or not dorm:
        return "failure"
    return render_template("success.html", dorm=dorm, name=name)
    

if __name__ == "__main__":
    app.run(debug = True)