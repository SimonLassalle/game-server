from typing import List, Dict
from flask import Flask
import mysql.connector
import json

app = Flask(__name__)
app.debug = True

def getUsers() -> List[Dict]:
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
    results = [{name: color} for (_, name, color) in cursor]
    cursor.close()
    connection.close()

    return results


@app.route('/')
def index() -> str:
    return json.dumps({'users': getUsers()})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
