from flask import render_template, Flask, request
import pickle
import re

app = Flask(__name__)

vector = pickle.load(open("vectorizer.pkl", "rb"))
model = pickle.load(open("Phishing.pkl", "rb"))

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Safely get the 'url' field from the submitted form
        url = request.form.get('url', '').strip()

        # If no URL provided, render the template with an error message
        if not url:
            return render_template("index.html", prediction="Please provide a URL")

        # cleaned_url = re.sub(r'http[s]?://(www\.)?', '', url)
        cleaned_url = url
        print(cleaned_url)

        predict=model.predict(vector.transform([cleaned_url]))[0]
        print(predict)

        if (predict=='bad'):
            predict="Phishing"
        else:
            predict="Legitimate"
        return render_template("index.html", prediction=predict)

    return render_template("index.html") 

if __name__=="__main__":
    app.run(debug=True)