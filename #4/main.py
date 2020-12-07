from flask import Flask, render_template, request

app = Flask("JobScraper")

# url이랑 주고받고 하려면 다음과 같이 작성해주면 된다.
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/report")
def report():
    word = request.args.get('word')
    return render_template("report.html", searching_by=word)

app.run(host="127.0.0.1")