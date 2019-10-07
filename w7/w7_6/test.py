infile = open("large", "r")
dictionary = [word.rstrip() for word in infile.readlines()]
print(dictionary)




@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    w = request.form.get("w")
    # results = [word for word in dictionary if word.startswith(w)]
    return render_template("index.html", w=w)


if __name__ == "__main__":
    app.run(debug = True)