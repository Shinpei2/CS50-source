from flask import Flask, render_template, request

app = Flask(__name__)

infile = open("large", "r")
dictionary = [word.rstrip() for word in infile.readlines()]

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    w = request.form["w"]
    print(w, type(w))
    results = [word for word in dictionary if word.startswith(w)]
    # print(results)
    return render_template("search.html", w=w, results=results)


if __name__ == "__main__":
    app.run(debug = True)