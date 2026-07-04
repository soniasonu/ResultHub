# ResultHub

A simple application to add students, check pass/fail results, and view passed students — built in two versions: a terminal-based CLI app and a Flask web app with SQLite database.

This project demonstrates the same core logic implemented two different ways, showing how business logic can be separated from the user interface.

## Features

- Add student name and marks
- View all students
- Check individual student result (Pass/Fail)
- View list of all passed students
- Delete a student record (web version)
- Persistent storage using SQLite database

## Technologies Used

- Python
- Flask
- SQLite
- HTML/CSS
- Jinja2 templating

## Project Structure

```
ResultHub/
├── README.md
├── terminal_version/
│   └── student_result_manager.py
└── web_version/
    ├── app.py
    ├── students.db
    └── templates/
        ├── index.html
        ├── result.html
        └── passed.html
```

## How to Run

### Terminal Version

```bash
cd terminal_version
python student_result_manager.py
```

### Web Version

```bash
cd web_version
pip install flask
python app.py
```

Then open `http://127.0.0.1:5000` in your browser.

## What I Learned

- Python dictionaries, loops, and conditionals
- Flask routing (`@app.route`) and HTTP methods (GET/POST)
- Jinja2 templating (`{% if %}`, `{% for %}`, `{{ }}`)
- Reading form data with `request.form`
- Working with SQLite — creating tables, inserting, querying, and deleting records
- Debugging real errors: template loading, folder structure, variable name mismatches
- Converting a CLI program's logic into a web application

## Future Improvements

- Add grade system (A/B/C/D) instead of just Pass/Fail
- Support multiple subjects per student
- Add search functionality
- Deploy live using Render