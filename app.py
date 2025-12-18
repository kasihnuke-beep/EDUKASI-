from flask import Flask, render_template, request, redirect, session
import os

app = Flask(__name__)
app.secret_key = "rahasia"

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# User sederhana (demo)
USER = {
    "admin": "123"
}

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form["username"] in USER and USER[request.form["username"]] == request.form["password"]:
            session["login"] = True
            return redirect("/dashboard")
    return render_template("login.html")

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if not session.get("login"):
        return redirect("/")
    
    if request.method == "POST":
        photo = request.files["photo"]
        photo.save(os.path.join(app.config["UPLOAD_FOLDER"], photo.filename))
        return "Foto berhasil diunggah"

    return render_template("dashboard.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
