from flask import Flask, render_template, request, redirect, send_file
from saramin import get_jobs
from exporter import save_to_file

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
    return render_template("report.html", searching_by=word, results_number=len(jobs), jobs=jobs)

@app.route("/export")
def export():
    # try를 실행하다 에러가 나면 except 실행
    try:
        word = request.args.get('word')
        if not word:
            raise Exception() # throw 개념
        # 만약 word가 존재하면 exception 안 던지고 아래 코드 수행
        word = word.lower()
        jobs = db.get(word)
        if not jobs:
            raise Exception()
        save_to_file(jobs, word)
        return send_file(f"{word}_jobs.csv") # 파일명 exporter.py에서 지정한 것이랑 똑같이
    except:
        return redirect("/")

app.run(host="127.0.0.1")