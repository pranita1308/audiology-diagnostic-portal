#!C:/Python312/python.exe

import cgi
import sqlite3
import datetime

print("Content-Type: text/html\n")

# Connect to SQLite database (or create if not exists)
conn = sqlite3.connect('quiz.db')
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS quiz_results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        score INTEGER,
        total INTEGER,
        submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')

# Get form data
form = cgi.FieldStorage()
name = form.getvalue("name", "Anonymous")
email = form.getvalue("mail", "Not provided")

correct_answers = {
    "q1": "Paris",
    "q2": "Mars",
    "q3": "Au",
    "q4": "Heart",
    "q5": "Carbon Dioxide",
    "q6": "Africa"
}

score = 0
total = len(correct_answers)

# Calculate score
for q, correct in correct_answers.items():
    if form.getvalue(q) == correct:
        score += 1

# Insert into database
cursor.execute('''
    INSERT INTO quiz_results (name, email, score, total)
    VALUES (?, ?, ?, ?)
''', (name, email, score, total))

conn.commit()
conn.close()

# Show result
print(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Quiz Submitted</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background: #f0f4f8;
            margin: 0;
            padding: 0;
        }}
        .container {{
            max-width: 600px;
            margin: 80px auto;
            background: #ffffff;
            border-radius: 10px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            padding: 40px;
            text-align: center;
        }}
        h2 {{
            color: #2c3e50;
        }}
        p {{
            font-size: 18px;
            color: #34495e;
            margin-bottom: 20px;
        }}
        strong {{
            color: #27ae60;
        }}
        .btn {{
            display: inline-block;
            margin-top: 20px;
            padding: 12px 25px;
            background-color: #2980b9;
            color: #fff;
            text-decoration: none;
            border-radius: 5px;
            font-weight: bold;
        }}
        .btn:hover {{
            background-color: #1f6391;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h2>Thank you, {name}!</h2>
        <p>Your score: <strong>{score}</strong> out of <strong>{total}</strong></p>
        <p>Your result has been successfully saved in our system.</p>
        <a class="btn" href="questions.py">Take Quiz Again</a>
    </div>
</body>
</html>
""")

