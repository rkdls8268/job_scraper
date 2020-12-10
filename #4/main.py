from flask import Flask, render_template, request, redirect
from saramin import get_jobs
app = Flask("JobScraper")

db = {}


# url이랑 주고받고 하려면 다음과 같이 작성해주면 된다.
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/report")
def report():
    word = request.args.get('word')
    if word:
        word = word.lower()
        fromDb = db.get(word)
        if fromDb: # db에 결과가 있으면 scraping 할 필요없이 바로 결과 보여주기
            jobs = fromDb
        else:
            # 입력받은 단어를 get_jobs로 보낸다.
            jobs = get_jobs(word)
            db[word] = jobs
    else:
        return redirect("/")
    return render_template("report.html", searching_by=word, resultsNumber=len(jobs))

app.run(host="127.0.0.1")