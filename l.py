#!C:/Python312/python.exe
import cgi
import cgitb
cgitb.enable()
print("Content-Type: text/html\n")

form = cgi.FieldStorage()
email = form.getvalue('email')
password = form.getvalue('password')

print('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>User Login - Audiology Center</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', sans-serif;
            background-image: url('https://images.unsplash.com/photo-1588776814546-ec7e267f8f32?auto=format&fit=crop&w=1600&q=80');
            background-size: cover;
            background-position: center;
        }
        .container {
            width: 400px;
            margin: 80px auto;
            background: rgba(255, 255, 255, 0.9);
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 0 15px rgba(0,0,0,0.2);
        }
        h2 {
            text-align: center;
            color: #2c3e50;
        }
        .input-group {
            margin: 15px 0;
        }
        .input-group label {
            display: block;
            color: #333;
            font-weight: bold;
        }
        .input-group input {
            width: 100%;
            padding: 10px;
            margin-top: 5px;
            border: 1px solid #ccc;
            border-radius: 8px;
        }
        .btn {
            width: 100%;
            background: #3498db;
            color: white;
            padding: 12px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 16px;
        }
        .btn:hover {
            background: #2980b9;
        }
        .options {
            margin-top: 15px;
            text-align: center;
        }
        .options a {
            text-decoration: none;
            color: #2980b9;
        }
        .show-password {
            margin-top: 10px;
            display: flex;
            align-items: center;
            font-size: 14px;
        }
        .show-password input {
            margin-right: 8px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>User Login</h2>
        <form method="post" action="userloginbackend.py">
            <div class="input-group">
                <label for="email">Email</label>
                <input type="email" name="email" required placeholder="Enter your email">
            </div>
            <div class="input-group">
                <label for="password">Password</label>
                <input type="password" name="password" id="password" required placeholder="Enter your password">
            </div>
            <div class="show-password">
                <input type="checkbox" onclick="togglePassword()"> Show Password
            </div>
            <button type="submit" class="btn">Login</button>
            <div class="options">
                <p><a href="userregister.py">Create an account</a> | <a href="userrecover.py">Forgot Password?</a></p>
            </div>
        </form>
    </div>

    <script>
        function togglePassword() {
            var field = document.getElementById("password");
            field.type = field.type === "password" ? "text" : "password";
        }
    </script>
</body>
</html>
''')
