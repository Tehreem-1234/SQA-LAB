# Grade Manager

A small Python project for a Software Testing & Quality Assurance lab.
It contains a grade-calculation module, unit tests (pytest), and a
deliberately flawed module (`legacy_utils.py`) so SonarQube has real
issues to detect.

## Run tests with coverage
```
pip install -r requirements.txt
pytest --cov=src --cov-report=xml --cov-report=term
```

## Push to GitHub
```
git init
git add .
git commit -m "Initial commit: grade manager"
git branch -M main
git remote add origin https://github.com/<your-username>/grade-manager.git
git push -u origin main
```

## Analyze with SonarQube (local)
1. Start SonarQube: `docker run -d --name sonarqube -p 9000:9000 sonarqube:community`
2. Open http://localhost:9000 (login admin / admin, then change password).
3. Create a project with key `grade-manager` and generate a token.
4. Run tests (creates coverage.xml), then scan:
```
sonar-scanner -Dsonar.host.url=http://localhost:9000 -Dsonar.token=<YOUR_TOKEN>
```
5. View bugs, vulnerabilities, code smells, duplication and coverage on the dashboard.

## Lab report ideas
- Screenshot the dashboard (Quality Gate, coverage, issues).
- Fix the issues in `legacy_utils.py`, add tests, re-scan, and compare before/after.
