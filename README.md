# Phishing Website Detection

This small Flask app classifies a given URL as phishing or legitimate using a pre-trained model.

Suggested repository structure and filenames
- `app.py` — Flask application (already present)
- `templates/index.html` — Main UI with the POST form (already present)
- `requirements.txt` — Python dependencies (this file)
- `README.md` — Project overview and run instructions (this file)
- `vectorizer.pkl`, `Phishing.pkl` — model artifacts (already present)
- `dataset/` — raw data and notebooks

Run locally
1. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python app.py
```

Open http://127.0.0.1:5000 in your browser.

Resetting Git history and pushing to GitHub
----------------------------------------
If you want to completely reset git history and push to a fresh GitHub repo, see the `RESET-GIT.md` instructions below in this repo.
