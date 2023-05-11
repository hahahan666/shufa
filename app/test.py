from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/search', methods=['POST'])
def search():
    keyword = request.form.get('keyword')
    con = pymysql.connect(host='localhost', user='root', password='993646057.', database='work')
    cur = con.cursor()
    sql = "select * from student where name like '%{}%'".format(keyword)
    cur.execute(sql)
    data = cur.fetchall()
    cur.close()
    con.close()
    return render_template('result.html', data=data)

if __name__ == '__main__':
   app.run(debug=True, host='127.0.0.1', port='8080')