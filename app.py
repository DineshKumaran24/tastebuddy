from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = "secret123"  # required for session

USERNAME = "admin"
PASSWORD = "123"

# Store feedback
posts = []

@app.route("/")
def home():
    return redirect("/login")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == USERNAME and password == PASSWORD:
            session["logged_in"] = True
            return redirect("/feed")
        else:
            return "Invalid login!"
    return render_template("login.html")

@app.route("/feed", methods=["GET", "POST"])
def feed():
    if not session.get("logged_in"):
        return redirect("/login")
    if request.method == "POST":
        username = request.form["username"]
        item = request.form["item"]
        feedback = request.form["feedback"]
        rating = request.form["rating"]
        posts.append({"username": username, "item": item, "feedback": feedback, "rating": rating})
    return render_template("feed.html", posts=posts)

@app.route("/logout", methods=["POST"])
def logout():
    session["logged_in"] = False
    return redirect("/login")

if __name__ == "__main__":
    app.run(debug=True)
