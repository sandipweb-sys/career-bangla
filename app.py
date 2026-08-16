# ==================================================
# 1. FLASK IMPORT
# ==================================================

from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3


# ==================================================
# 2. FLASK APP তৈরি
# ==================================================

app = Flask(__name__)

app.secret_key = "career-bangla-secret-key"


# ==================================================
# 3. LOGIN PAGE
# ==================================================

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "GET":
        return render_template("login.html")

    username = request.form["username"]
    password = request.form["password"]

    if username == "admin" and password == "1234":

        session["logged_in"] = True

        return redirect(url_for("admin"))

    return "Invalid username or password"


# ==================================================
# 4. DATABASE তৈরি
# ==================================================

def create_database():

    connection = sqlite3.connect("database.db")

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            message TEXT NOT NULL
        )
    """)

    connection.commit()

    connection.close()


create_database()


# ==================================================
# 5. HOME PAGE
# ==================================================

@app.route("/")
def home():

    return render_template("index.html")


# ==================================================
# 6. ADMIN PAGE
# ==================================================

@app.route("/admin")
def admin():

    # Login করা আছে কিনা check
    if not session.get("logged_in"):
        return redirect(url_for("login"))

    connection = sqlite3.connect("database.db")

    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name, email, message
        FROM contacts
        ORDER BY id DESC
    """)

    contacts = cursor.fetchall()

    connection.close()

    return render_template("admin.html", contacts=contacts)


# ==================================================
# 7. CONTACT FORM DATA RECEIVE
# ==================================================

@app.route("/contact", methods=["POST"])
def contact():

    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")


    # Database-এর সাথে connection
    connection = sqlite3.connect("database.db")

    cursor = connection.cursor()


    # Form-এর data database-এ save
    cursor.execute("""
        INSERT INTO contacts (name, email, message)
        VALUES (?, ?, ?)
    """, (name, email, message))


    # Changes save
    connection.commit()


    # Connection বন্ধ
    connection.close()


    print("Name:", name)
    print("Email:", email)
    print("Message:", message)


    return "Form received successfully!"


# ==================================================
# 8. LOGOUT
# ==================================================

@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("login"))


# ==================================================
# 9. WEBSITE RUN
# ==================================================

if __name__ == "__main__":

    app.run(debug=True)