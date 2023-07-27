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
