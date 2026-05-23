# GitHub Copilot Quick Reference Guide

A handy reference for using GitHub Copilot effectively during the exercise.

## 🎯 Interaction Modes

| Mode | Icon | Shortcut | Best For |
|------|------|----------|----------|
| **Ask Mode** | 💭 | - | Understanding code, asking questions |
| **Inline Chat** | 💬 | `Ctrl/Cmd + I` | Targeted edits to specific code sections |
| **Agent Mode** | 🤖 | - | Multi-step tasks, autonomous coding |
| **Plan Agent** | 🧭 | - | Planning before implementation |

## ⌨️ Essential Shortcuts

### Windows/Linux
- Open Copilot Chat: `Ctrl + Alt + I`
- Inline Chat: `Ctrl + I`
- Accept suggestion: `Tab`
- Show multiple suggestions: `Ctrl + Enter`
- Toggle Chat panel: Click chat icon in top bar

### Mac
- Open Copilot Chat: `Cmd + Alt + I`
- Inline Chat: `Cmd + I`
- Accept suggestion: `Tab`
- Show multiple suggestions: `Cmd + Enter`
- Toggle Chat panel: Click chat icon in top bar

## 🎨 Writing Effective Prompts

### DO ✅
- **Be specific**: "Add validation to check if email is already in participants list"
- **Provide context**: Use `#codebase`, `@workspace`, or attach files
- **Iterate**: Refine prompts based on results
- **Use examples**: "Like the existing Chess Club, add a Drama Club"
- **State intent**: "I want to fix a bug where students can sign up twice"

### DON'T ❌
- Be vague: "make it better"
- Assume Copilot knows everything: provide context
- Give up after first try: iterate and clarify
- Forget to review: always verify suggestions

## 💡 Common Prompt Patterns

### Understanding Code
```prompt
Explain how [function/file] works
What does this code do?
#codebase How is authentication handled?
```

### Finding Bugs
```prompt
#codebase Students can register twice for an activity. Where could this bug be?
Why is [specific behavior] happening?
```

### Generating Code
```prompt
Add 2 more sports activities following the same structure
Create a function to [specific task]
```

### Refactoring
```prompt
Extract this logic into a separate function
Make this code more readable
Add error handling to this function
```

### Testing
```prompt
Write pytest tests for this endpoint using AAA pattern
Add test cases for edge cases
```

### Documentation
```prompt
Add docstrings to these functions
Explain what this component does for new developers
```

## 🛠️ Chat Participants & Variables

### Participants (use with `@`)
- `@workspace` - Search across workspace
- `@terminal` - Terminal integration
- `@vscode` - VS Code commands

### Variables (use with `#`)
- `#codebase` - Search codebase
- `#file` - Reference specific file
- `#selection` - Current selection
- `#editor` - Active file

### Examples
```prompt
@workspace What test framework is being used?
#codebase Find all API endpoints
#file:app.py Explain the signup function
```

## 🔧 Slash Commands

Use slash commands in chat for common tasks:

- `/explain` - Explain code
- `/fix` - Fix problems
- `/tests` - Generate tests
- `/help` - Show all commands
- `/clear` - Clear chat history

### Example
```prompt
/explain signup_for_activity function
/tests for the activities endpoint
```

## 🎓 Exercise-Specific Prompts

### Step 1: Getting Started
```prompt
Please briefly explain the structure of this project. What should I do to run it?
```
```prompt
Hey copilot, how can I create and publish a new Git branch called "accelerate-with-copilot"?
```

### Step 2: Bug Fix & Data
```prompt
#codebase Students are able to register twice for an activity. Where could this bug be coming from?
```
```python
# Validate student is not already signed up
# (Wait for Copilot suggestion, then press Tab)
```
```prompt
Add 2 more sports related activities, 2 more artistic activities, and 2 more intellectual activities.
```

### Step 3: Agent Mode Features
```prompt
Hey Copilot, can you please edit the activity cards to add a participants section. It will show what participants that are already signed up for that activity as a bulleted list. Remember to make it pretty!
```
```prompt
#codebase Please add a delete icon next to each participant and hide the bullet points. When clicked, it will unregister that participant from the activity.
```
```prompt
I've noticed there seems to be a bug. When a participant is registered, the page must be refreshed to see the change on the activity.
```

### Step 4: Testing with Plan Agent
```prompt
I want to add backend FastAPI tests in a separate tests directory.
```
```prompt
Let's use the AAA (Arrange-Act-Assert) testing pattern to structure our tests
```
```prompt
Make sure we use `pytest` and add it to `requirements.txt` file
```

## 🐛 Troubleshooting Copilot

### Copilot Not Responding
1. Check status bar icon (should be active)
2. Accept usage terms if prompted
3. Verify Copilot subscription
4. Reload window: `Ctrl/Cmd + Shift + P` → "Reload Window"

### No Suggestions Appearing
1. Wait a moment after typing
2. Try `Tab` to accept shadow text
3. Try `Ctrl/Cmd + Enter` for alternatives
4. Check extension is enabled

### Poor Quality Suggestions
1. Provide more context (open related files)
2. Be more specific in prompts
3. Try different phrasing
4. Use different model (Claude, GPT-4, etc.)

### Agent Mode Not Working
1. Update VS Code to latest version
2. Update GitHub Copilot extension
3. Check internet connection
4. Try restarting VS Code

## 📚 Best Practices

### Context Management
- Keep relevant files open in tabs
- Add files to chat context explicitly
- Use `#codebase` for broader searches
- Close irrelevant files to reduce noise

### Iterative Development
1. Start with simple prompt
2. Review suggestion
3. Refine if needed
4. Accept or modify
5. Test the result
6. Iterate as necessary

### Code Review
- Always review Copilot's code
- Test functionality thoroughly
- Verify edge cases
- Check for security issues
- Ensure code style matches project

### Learning from Copilot
- Ask "why" questions
- Request explanations
- Learn patterns, not just solutions
- Experiment with different approaches

## 🎯 Exercise Goals Checklist

- [ ] Create `accelerate-with-copilot` branch
- [ ] Fix duplicate signup bug
- [ ] Add 6 new activities
- [ ] Display participants on activity cards
- [ ] Add unregister functionality
- [ ] Fix auto-refresh bug
- [ ] Create comprehensive test suite
- [ ] Make all tests pass
- [ ] Create and merge PR

## 📖 Additional Resources

- **GitHub Copilot Docs**: https://docs.github.com/en/copilot
- **VS Code Copilot**: https://code.visualstudio.com/docs/copilot/overview
- **Copilot Features**: https://docs.github.com/en/copilot/about-github-copilot/github-copilot-features
- **FastAPI Docs**: https://fastapi.tiangolo.com/
- **Pytest Docs**: https://docs.pytest.org/

## 💬 Getting Help

If you're stuck:
1. Ask Copilot for help with specific question
2. Review the EXERCISE_HELP.md file
3. Check example solutions in `examples/` directory
4. Experiment with different prompts
5. Try a different Copilot model

---

**Remember**: The goal is to learn how to work WITH Copilot, not just to complete the exercise. Take time to understand what Copilot suggests and why!

Happy coding! 🚀
