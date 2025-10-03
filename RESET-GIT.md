# How to reset Git history, initialize and push this project to GitHub

These steps will initialize a fresh git repository in this folder, create an initial commit, and push it to a new GitHub repository. They do not modify your project files (except to add git metadata and commits).

1) Create a new repository on GitHub
- Go to https://github.com/new and create a new empty repository (do not initialize with README or .gitignore unless you want to merge histories). Copy the remote URL (HTTPS or SSH).

2) Initialize a local git repository and make the initial commit

```bash
cd /path/to/your/project  # e.g. /home/saurabh-kumar/Desktop/Prog/hackathon/hackspire/jupyter_project
git init
git add .
git commit -m "chore: initial commit - reset repo"
```

3) Add the GitHub remote and push

Replace <REMOTE_URL> with the URL from step (1):

```bash
git remote add origin <REMOTE_URL>
git branch -M main
git push -u origin main
```

If you want to completely obliterate any existing history (for example from another machine) and create a brand new remote branch, you can force-push (be careful):

```bash
git push -u --force origin main
```

4) Suggested filenames and small refactor
- Keep `app.py` as the Flask entrypoint.
- Keep `templates/index.html` for the UI.
- Name model artifacts clearly: `vectorizer.pkl` and `phishing_model.pkl` (I suggest renaming `Phishing.pkl` to `phishing_model.pkl` to be consistent and lowercase).
- Keep `requirements.txt` and `.gitignore` at the repo root.
- Move notebooks into `notebooks/` or `dataset/notebooks/` if you want to separate code from artifacts.

5) If you'd like me to perform the git init + first commit and push for you, provide the remote repository URL and confirm you want me to run the commands locally.
