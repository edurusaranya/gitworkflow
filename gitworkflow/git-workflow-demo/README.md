# Git Workflow Demo

A simple Python calculator project demonstrating a complete Git branching workflow, automated testing, and CI/CD with GitHub Actions.

## Project Structure

```
git-workflow-demo/
├── .github/
│   └── workflows/
│       └── ci.yml          # GitHub Actions CI pipeline
├── src/
│   ├── __init__.py
│   └── calculator.py        # Core application logic
├── tests/
│   ├── __init__.py
│   └── test_calculator.py   # Unit tests
├── .gitignore
├── requirements.txt
└── README.md
```

## Setup

```bash
git clone https://github.com/<your-username>/git-workflow-demo.git
cd git-workflow-demo
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Running the App

```bash
python src/calculator.py
```

## Running Tests

```bash
pytest tests/ -v
```

## Git Branching Workflow

This project follows a simplified **Gitflow** strategy.

### Branches

- `main` – production-ready, stable code only
- `develop` – integration branch for ongoing development
- `feature/*` – new features, branched from `develop`
- `bugfix/*` – bug fixes, branched from `develop`
- `hotfix/*` – urgent production fixes, branched from `main`

### Workflow Steps

1. **Create the repository on GitHub** and clone it locally:
   ```bash
   git clone https://github.com/<your-username>/git-workflow-demo.git
   cd git-workflow-demo
   ```

2. **Initialize and push the project** (first time):
   ```bash
   git init
   git add .
   git commit -m "Initial commit: project setup"
   git branch -M main
   git remote add origin https://github.com/<your-username>/git-workflow-demo.git
   git push -u origin main
   ```

3. **Create a develop branch**:
   ```bash
   git checkout -b develop
   git push -u origin develop
   ```

4. **Start a new feature**:
   ```bash
   git checkout develop
   git pull origin develop
   git checkout -b feature/add-power-operation
   ```

5. **Work, commit, and push**:
   ```bash
   git add .
   git commit -m "feat: add power operation to calculator"
   git push -u origin feature/add-power-operation
   ```

6. **Open a Pull Request** on GitHub: `feature/add-power-operation` → `develop`.
   - CI runs automatically (lint + tests)
   - Request review, address comments, then merge

7. **Release to production**:
   ```bash
   git checkout main
   git pull origin main
   git merge develop
   git tag -a v1.0.0 -m "Release v1.0.0"
   git push origin main --tags
   ```

8. **Hotfix example**:
   ```bash
   git checkout main
   git checkout -b hotfix/fix-divide-bug
   # fix the bug
   git add .
   git commit -m "fix: handle division by zero correctly"
   git checkout main
   git merge hotfix/fix-divide-bug
   git push origin main
   git checkout develop
   git merge hotfix/fix-divide-bug
   git push origin develop
   ```

### Commit Message Convention

This project uses [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` – new feature
- `fix:` – bug fix
- `docs:` – documentation changes
- `test:` – adding or updating tests
- `refactor:` – code change that neither fixes a bug nor adds a feature
- `chore:` – maintenance tasks

## Continuous Integration

Every push and pull request to `main` or `develop` triggers the GitHub Actions workflow (`.github/workflows/ci.yml`), which:

1. Installs dependencies across Python 3.9, 3.10, and 3.11
2. Lints code with `flake8`
3. Runs the test suite with `pytest`

## License

MIT
