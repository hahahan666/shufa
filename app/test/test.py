from flask import Flask, request, redirect
from flask import render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index1.html")

@app.route("/redirect", methods=["POST"])
def redirect_page():
    identity = request.form.get("identity")
    if identity == "student":
        return redirect("/student")
    elif identity == "teacher":
        return redirect("/teacher")
    else:
        return "请选择身份"

@app.route("/student")
def student_page():
    return "这是学生页面"

@app.route("/teacher")
def teacher_page():
    return "这是教师页面"

app.run(debug=True)