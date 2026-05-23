# Getting Started with GitHub Copilot

<img src="https://octodex.github.com/images/Professortocat_v2.png" align="right" height="200px" />

Hey MoneyMan421!

Mona here. I'm done preparing your exercise. Hope you enjoy! 💚

Remember, it's self-paced so feel free to take a break! ☕️

[![](https://img.shields.io/badge/Go%20to%20Exercise-%E2%86%92-1f883d?style=for-the-badge&logo=github&labelColor=197935)](https://github.com/MoneyMan421/skills-getting-started-with-github-copilot/...)

---

## Development Setup

To set up your development environment and enable testing and auto-reloading:

1. Install the development requirements:

    ```bash
    pip install -r requirements-dev.txt
    ```

    This will install all dependencies listed in both `requirements.txt` and extra tools for development like `pytest` and `watchfiles`.

2. **Run tests:**

    ```bash
    pytest
    ```

3. **Use auto-reloader (optional):**

    If you want to automatically reload your app during development (e.g., with FastAPI and uvicorn), you can use watchfiles as a reload backend:

    ```bash
    uvicorn app:app --reload --reload-dir .
    ```

---

## Project .gitignore

This project uses a `.gitignore` file to prevent certain temporary files, OS-generated files, compiled binaries, logs, and package archives from being accidentally committed to version control. This helps keep the repository clean and avoids sharing artifacts that do not belong in source code.

<details>
<summary>Click to expand the <code>.gitignore</code> contents used for this repo</summary>

```gitignore
*.temp*

# Compiled source #
###################
*.com
*.class
*.dll
*.exe
*.o
*.so

# Packages #
############
# it's better to unpack these files and commit the raw source
# git has its own built in compression methods
*.7z
*.dmg
*.gz
*.iso
*.jar
*.rar
*.tar
*.zip

# Logs and databases #
######################
*.log
*.sql
*.sqlite

# OS generated files #
######################
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db
.actrc*

__pycache__/
```
</details>

© 2025 GitHub • [Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md) • [MIT License](https://gh.io/mit)

## License

This project is licensed under the MIT License.  
See the [LICENSE](LICENSE) file for details.

