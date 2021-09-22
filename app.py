from flask import Flask,jsonify
import psycopg2

app = Flask(__name__)


@app.route('/createtable')
def create():
    conn = psycopg2.connect(database = "postgres", user = "postgres", password = "postgres", host = "db", port = "5432")
    print("Opened database successfully")

    cur = conn.cursor()
    try:
        cur.execute('''CREATE TABLE accounts (
        user_id serial PRIMARY KEY,
        username VARCHAR ( 50 ) UNIQUE NOT NULL,
        password VARCHAR ( 50 ) NOT NULL,
        email VARCHAR ( 255 ) UNIQUE NOT NULL,
        created_on TIMESTAMP NOT NULL,
        last_login TIMESTAMP );''')
        print("Table created successfully")
        conn.commit()
        conn.close()
        return jsonify({"message":"table created"})
    except:
        conn.close()
        return jsonify({"message":"table already exists"})


@app.route('/deletetable')
def delete():
    conn = psycopg2.connect(database = "postgres", user = "postgres", password = "postgres", host = "db", port = "5432")
    print("Opened database successfully")
    try:
        cur = conn.cursor()
        cur.execute('''DROP TABLE accounts;''')
        print("Table deleted successfully")
        conn.commit()
        conn.close()
        return jsonify({"message":"table deleted"})
    except:
        return jsonify({"message":"no tables found"})


@app.route('/showtables')
def showtables():
    conn = psycopg2.connect(database = "postgres", user = "postgres", password = "postgres", host = "db", port = "5432")
    print("Opened database successfully")

    cur = conn.cursor()
    rs = cur.execute('''SELECT * FROM pg_catalog.pg_tables WHERE schemaname != 'pg_catalog' AND schemaname != 'information_schema';''')
    print(rs)
    print("show tables")
    lst = list(cur)
    conn.commit()
    conn.close()
    return jsonify({"message":lst})

