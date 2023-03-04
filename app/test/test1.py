from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '993646057.'
app.config['MYSQL_DB'] = 'MyDB'

mysql = MySQL(app)

@app.route('/<1>')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM MyUsers WHERE firstname=%s", (username,))
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)