from flask import Flask, render_template, request, redirect
from saramin import get_jobs
app = Flask("JobScraper")

# url이랑 주고받고 하려면 다음과 같이 작성해주면 된다.
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/report")
def report():
    word = request.args.get('word')
    if word:
        word = word.lower()
        # 입력받은 단어를 get_jobs로 보낸다.
        jobs = get_jobs(word)
    else:
        return redirect("/")
    return render_template("report.html", searching_by=word)

app.run(host="127.0.0.1")