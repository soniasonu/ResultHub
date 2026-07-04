from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

DB_NAME = "students.db"

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute(""" 
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE, 
                mark INTEGER NOT NULL
            )
        """)
    conn.commit()
    conn.close()

@app.route("/")
def home():
    conn = get_db_connection()
    rows = conn.execute("SELECT * FROM students").fetchall()
    conn.close()

    students = {row["name"]: row["mark"] for row in rows}
    return render_template("index.html", students=students)

@app.route("/add", methods=["POST"])
def add():
    name = request.form["name"].strip()  
    mark = int(request.form["mark"])
    
    conn = get_db_connection()
    conn.execute(
        "INSERT OR REPLACE INTO students (name, mark) VALUES (?, ?)",
        (name, mark)
    )
    conn.commit()
    conn.close()
    return redirect(url_for("home"))

@app.route("/result/<path:name>")  
def result(name):
    conn = get_db_connection()
    row = conn.execute(
        "SELECT * FROM students WHERE name = ?", (name,)
    ).fetchone()
    conn.close()

    if row is None:
        return "Student not found!"
    
    mark = row["mark"]
    passed = mark >= 50
    return render_template("result.html", name=name, mark=mark, passed=passed)

@app.route("/passed")
def passed():
    conn = get_db_connection()
    rows = conn.execute(
        "SELECT * FROM students WHERE mark >= 50"
    ).fetchall()
    conn.close()

    passed_students = {row["name"]: row["mark"] for row in rows}
    return render_template("passed.html", students=passed_students)

@app.route("/delete/<path:name>")  
def delete(name):
    conn = get_db_connection()
    conn.execute("DELETE FROM students WHERE name = ?", (name,))
    conn.commit()
    conn.close()
    return redirect(url_for("home"))

if __name__ == "__main__":
    init_db()
    app.run(debug=True)