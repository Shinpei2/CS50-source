import csv
from flask import Flask, jsonify, redirect, render_template, request

# Configure application
app = Flask(__name__)

# Reload templates when they are changed
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.after_request
def after_request(response):
    """Disable caching"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET"])
def get_index():
    return redirect("/form")


@app.route("/form", methods=["GET"])
def get_form():
    return render_template("form.html")


@app.route("/form", methods=["POST"])
def post_form():
    # get post-data from form's-value
    name = request.form["name"]
    emp_id = request.form["emp_id"]
    sex = request.form["sex"]
    hometown = request.form["hometown"]
    department = request.form["department"]
    # print(name, emp_id, sex, hometown, department)

    # if form isn't filled, redirect user to error.html
    if not name or not emp_id or not sex or not hometown or not department:
        return render_template("error.html", message="Form isn't filled!")

    # write information in CSV
    file_name = "survey.csv"
    outfile = open(file_name, "a", newline='', encoding="utf-8")
    writer = csv.writer(outfile)
    writer.writerow([name, emp_id, sex, hometown, department])
    outfile.close()

    return redirect("/sheet")


@app.route("/sheet", methods=["GET"])
def get_sheet():
    # read csv-file and create Reader-object
    file_name = "survey.csv"
    infile = open(file_name, "r", encoding="utf-8")
    reader = csv.reader(infile)

    # append member to members-list
    members = []
    for row in reader:
        member = {'name':row[0], 'emp_id':row[1], 'sex':row[2], 'hometown':row[3], 'department':row[4]}
        members.append(member)

    infile.close()
    return render_template("sheet.html", members=members)
