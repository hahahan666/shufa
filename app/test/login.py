from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL

app = Flask(__name__)
# 定义一个字典存储账号、密码和角色信息
users = {'teacher1': {'password': '123456', 'role': 'teacher'},
         'student1': {'password': '654321', 'role': 'student'}}
# 定义一个路由处理登录请求
@app.route('/login', methods=['GET', 'POST'])
def login():
    # 如果是GET请求，返回登录界面模板
    if request.method == 'GET':
        return render_template('login.html')
    # 如果是POST请求，获取表单中的账号和密码
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # 判断账号是否存在
        if username in users:
            # 判断密码是否正确
            if password == users[username]['password']:
                # 判断角色是教师还是学生，并跳转到相应的页面
                if users[username]['role'] == 'teacher':
                    return redirect('/teacher')
                elif users[username]['role'] == 'student':
                    return redirect('/student')
            else:
                # 密码错误，返回错误信息
                return render_template('login.html', error='密码错误')
        else:
            # 账号不存在，返回错误信息
            return render_template('login.html', error='账号不存在')
# 定义一个路由处理教师界面请求
@app.route('/teacher')
def teacher():
    # 返回教师界面模板
    return render_template('teacher.html')
# 定义一个路由处理学生界面请求
@app.route('/student')
def student():
    # 返回学生界面模板
    return render_template('student.html')

            # 判断账号是否存在
                # 判断角色是教师还是学生，并跳转到相应的页面
    if users[username]['role'] == 'teacher':
                    # 拼接URL参数


                  # 跳转到新的URL
                  #return render_template('index.html' + params)
        return redirect('/teacher')
    elif users[username]['role'] == 'student':
                  return redirect('/student')