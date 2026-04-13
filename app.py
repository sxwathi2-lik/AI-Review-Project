from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    review = request.form["review"].lower()

    fake_words = ["worst", "fake", "waste", "bad"]

    result = "Real ✅"
    for word in fake_words:
        if word in review:
            result = "Fake ❌"

    if "good" in review:
        sentiment = "Positive 😊"
    elif "bad" in review:
        sentiment = "Negative 😡"
    else:
        sentiment = "Neutral 😐"

    trust = 80 if result == "Real ✅" else 30

    return render_template("index.html",
                           result=result,
                           sentiment=sentiment,
                           trust=trust)

app.run(host="0.0.0.0", port=10000)
