from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Required for session handling
app.config['TESTING'] = True  # Needed for test client

# ---------------------------
# Login Page
# ---------------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        # For simplicity, accept any username/password
        if username and password:
            session['logged_in'] = True
            return redirect("/feed")
        else:
            return render_template("login.html", error="Enter username and password")
    return render_template("login.html")


# ---------------------------
# Feed Page
# ---------------------------
@app.route("/feed", methods=["GET", "POST"])
def feed():
    if not session.get("logged_in"):
        return redirect("/login")

    if request.method == "POST":
        feedback = request.form.get("feedback")
        # Here, you can save feedback to file/db (optional)
        return render_template("feed.html", message="Feedback submitted!")

    return render_template("feed.html")


# ---------------------------
# Logout (optional)
# ---------------------------
@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    return redirect("/login")


# ---------------------------
if __name__ == "__main__":
    app.run(debug=True)
