from flask import Flask, render_template

app = Flask("JobScraper")

# url이랑 주고받고 하려면 다음과 같이 작성해주면 된다.
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/<username>")
def potato(username):
    return f"Hello {username} how are you doing?"

app.run(host="127.0.0.1")