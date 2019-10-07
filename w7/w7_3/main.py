from flask import Flask, render_template, request

app = Flask(__name__)

# Registerd students
students = []

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", students=students)


@app.route("/register", methods=["POST"])
def register():
    # get register-information
    name = request.form["name"]     # 前のページのformから値を取得する
    dorm = request.form["dorm"]     # 前のページのformから値を取得する
    sex = request.form["sex"]       # 前のページのformから値を取得する
    print(name, dorm, sex)
    if not name or not dorm:
        return "failure"
    # append student-data to students-list
    st_data = {"name":name, "dorm":dorm, "sex":sex}     # 情報の種類に応じて辞書の形は都度変更する
    students.append(st_data)

    return render_template("success.html", dorm=dorm, name=name, sex=sex)

@app.route("/registrants", methods=["GET"])
def registrants():
    return render_template("regstrants.html", students=students)

    

if __name__ == "__main__":
    app.run(debug = True)