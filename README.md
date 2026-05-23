# Getting Started with GitHub Copilot

<img src="https://octodex.github.com/images/Professortocat_v2.png" align="right" height="200px" />

Hey MoneyMan421!

Mona here. I'm done preparing your exercise. Hope you enjoy! 💚

Remember, it's self-paced so feel free to take a break! ☕️

[![](https://img.shields.io/badge/Go%20to%20Exercise-%E2%86%92-1f883d?style=for-the-badge&logo=github&labelColor=197935)](https://github.com/MoneyMan421/skills-getting-started-with-github-copilot/)

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

© 2025 GitHub • [Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md) • [MIT License](https://gh.io/mit)

## License

This project is licensed under the MIT License.  
See the [LICENSE](LICENSE) file for details.
