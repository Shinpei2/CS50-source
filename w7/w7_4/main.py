from flask import Flask, render_template, request
import csv

app = Flask(__name__)

# Registerd students
students = []
register_file = "registerd.csv"

@app.route("/", methods=["GET"])
def index():
    print(students)
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
    outfile = open(register_file, "a", newline='', encoding="utf-8")
    writer = csv.writer(outfile)
    writer.writerow([name, dorm, sex])
    outfile.close()
    return render_template("success.html", dorm=dorm, name=name, sex=sex)


@app.route("/registrants", methods=["GET"])
def registrants():
    return render_template("regstrants.html", students=students)


@app.route("/load", methods=["GET"])
def load():
    if len(students) > 0:
        return "既に1人以上のデータが存在します"
    infile = open(register_file, "r", encoding="utf-8")
    reader = csv.reader(infile)
    for row in reader:
        st_data = {"name":row[0], "dorm":row[1], "sex":row[2]}     # 情報の種類に応じて辞書の形は都度変更する
        students.append(st_data)
    infile.close()
    return render_template("load.html") 

    

if __name__ == "__main__":
    app.run(debug = True)