from typing import List, Dict
from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)
app.debug = True

def getUsers():
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'game',
        'auth_plugin': 'mysql_native_password'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM users')
    results = {}
    for (_id, name, color) in cursor:
        results[_id] = {'name':name, 'color':color}
    cursor.close()
    connection.close()

    return results

def addUser(data_user):
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'game',
        'auth_plugin': 'mysql_native_password'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    add_user = ("INSERT INTO users "
               "(name, color) "
               "VALUES (%s, %s)")
    cursor.execute(add_user, data_user)
    connection.commit()
    cursor.close()
    connection.close()

    return "ok"

def rmUser(data_user):
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'game',
        'auth_plugin': 'mysql_native_password'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    rm_user = ("DELETE FROM users WHERE ID = %s")
    cursor.execute(rm_user, (data_user,))
    connection.commit()
    cursor.close()
    connection.close()

    return "ok"

@app.route('/')
def index():
    return jsonify({'users': getUsers()})

@app.route('/add/<string:name>/<string:color>')
def add(name, color):
    data = (name, color)
    return addUser(data)

@app.route('/rm/<int:_id>')
def rm(_id):
    return rmUser(_id)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
