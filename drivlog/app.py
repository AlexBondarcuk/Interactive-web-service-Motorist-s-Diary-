# app.py 

from flask import Flask, render_template

import psycopg2

from config import DATABASE

app = Flask(__name__)


def connect_to_db():
    try:

        conn = psycopg2.connect(

            dbname=DATABASE['name'],

            user=DATABASE['user'],

            password=DATABASE['password'],

            host=DATABASE['host'],

            port=DATABASE['port']

        )

        return conn

    except Exception as e:

        return str(e)


@app.route('/')
def index():
    conn = connect_to_db()

    if isinstance(conn, str):

        db_status = f"Failed to connect to database: {conn}"

    else:

        db_status = "Successfully connected to the database!"

        conn.close()

    return render_template('index.html', db_status=db_status)


if __name__ == '__main__':
    app.run(debug=True)