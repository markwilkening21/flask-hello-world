import psycopg2

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgres://mjw_render_db_user:IS6C2Ha9NYTLbzlWSzC26O4AQxX1EEZT@dpg-cj1c682ip7vkfo6sktig-a/mjw_render_db")
    conn.close()
    return "Database Connection Successful"

@app.route('/db_create')
def creating():
    conn = psycopg2.connect("postgres://mjw_render_db_user:IS6C2Ha9NYTLbzlWSzC26O4AQxX1EEZT@dpg-cj1c682ip7vkfo6sktig-a/mjw_render_db")
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Basketball(
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Created"
