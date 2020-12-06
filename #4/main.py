from flask import Flask

app = Flask("JobScraper")

# url이랑 주고받고 하려면 다음과 같이 작성해주면 된다.
@app.route("/")
def home():
    return "Hello! welcome to my home!"

@app.route("/contact")
def potato():
    return "Contact me!"

app.run(host="127.0.0.1")