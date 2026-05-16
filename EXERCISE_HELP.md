# GitHub Copilot Exercise - Help & Answers Guide

Welcome to the comprehensive help guide for the **Getting Started with GitHub Copilot** exercise! This guide provides assistance, example solutions, and troubleshooting tips for each step of the exercise.

## 📚 Table of Contents

- [Overview](#overview)
- [Step 1: Hello Copilot](#step-1-hello-copilot)
- [Step 2: Getting Work Done with Copilot](#step-2-getting-work-done-with-copilot)
- [Step 3: Agent Mode](#step-3-agent-mode)
- [Step 4: Plan Agent](#step-4-plan-agent)
- [Step 5: Pull Request Features](#step-5-pull-request-features)
- [Common Issues & Troubleshooting](#common-issues--troubleshooting)

---

## Overview

This is a hands-on exercise designed to teach you how to use GitHub Copilot effectively. You'll work on a FastAPI web application for Mergington High School's extracurricular activities management system.

### Learning Objectives
- Master different Copilot interaction modes (Ask, Inline, Agent, Plan)
- Fix bugs with AI assistance
- Generate test code
- Use Copilot for PR summaries and code reviews

### Prerequisites
- GitHub account with Copilot access
- Basic understanding of Python and web development

---

## Step 1: Hello Copilot

### 🎯 Goal
Create a GitHub Codespace, get familiar with the project, and create the `accelerate-with-copilot` branch.

### Activities Checklist
- ✅ Create a GitHub Codespace for this repository
- ✅ Verify GitHub Copilot and Python extensions are installed
- ✅ Open Copilot Chat in Ask Mode
- ✅ Ask Copilot about the project structure
- ✅ Run the application and view it in browser
- ✅ Use Terminal Inline Chat to create and publish the branch

### Example Prompts

**For understanding the project:**
```prompt
Please briefly explain the structure of this project.
What should I do to run it?
```

**For creating the branch:**
```prompt
Hey copilot, how can I create and publish a new Git branch called "accelerate-with-copilot"?
```

### Expected Commands
Copilot should suggest something like:
```bash
git checkout -b accelerate-with-copilot
git push -u origin accelerate-with-copilot
```

### Troubleshooting
- **Extensions not installed?** Go to Extensions tab and search for "GitHub Copilot" and "Python"
- **Can't find Toggle Chat icon?** Look at the top-right of VS Code for the chat bubble icon
- **Branch name matters!** Must be exactly `accelerate-with-copilot` (no prefixes/suffixes)

---

## Step 2: Getting Work Done with Copilot

### 🎯 Goal
Fix the duplicate signup bug, add more activities, and commit changes.

### Activities Checklist
- ✅ Identify the bug location using Copilot Ask Mode
- ✅ Fix the duplicate signup validation in `src/app.py`
- ✅ Add 6 new activities using Inline Chat
- ✅ Generate commit message with Copilot
- ✅ Commit and push changes

### Bug Fix Example

**The Bug:** Students can sign up for the same activity multiple times.

**Location:** `src/app.py`, in the `signup_for_activity` function

**Prompt for finding the bug:**
```prompt
#codebase Students are able to register twice for an activity.
Where could this bug be coming from?
```

**Comment to add in code (line 64):**
```python
# Validate student is not already signed up
```

**Expected Copilot suggestion:**
```python
# Validate student is not already signed up
if email in activity["participants"]:
    raise HTTPException(status_code=400, detail="Student is already signed up")
```

### Adding Activities Example

**How to do it:**
1. Highlight the entire `activities` dictionary (lines 23-42)
2. Use `Ctrl + I` (Windows) or `Cmd + I` (Mac) for Inline Chat
3. Use this prompt:

```prompt
Add 2 more sports related activities, 2 more artistic
activities, and 2 more intellectual activities.
```

**Example result:**
```python
activities = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    "Basketball Team": {
        "description": "Competitive basketball training and games",
        "schedule": "Tuesdays and Thursdays, 4:00 PM - 6:00 PM",
        "max_participants": 15,
        "participants": []
    },
    "Swimming Club": {
        "description": "Swimming training and water sports",
        "schedule": "Mondays and Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 20,
        "participants": []
    },
    "Art Studio": {
        "description": "Express creativity through painting and drawing",
        "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 15,
        "participants": []
    },
    "Drama Club": {
        "description": "Theater arts and performance training",
        "schedule": "Tuesdays, 4:00 PM - 6:00 PM",
        "max_participants": 25,
        "participants": []
    },
    "Debate Team": {
        "description": "Learn public speaking and argumentation skills",
        "schedule": "Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 16,
        "participants": []
    },
    "Science Club": {
        "description": "Hands-on experiments and scientific exploration",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 20,
        "participants": []
    }
}
```

### Committing Changes
- Go to Source Control tab
- Stage `app.py` file (click `+` button)
- Click sparkles icon to generate commit message
- Click "Commit" then "Sync Changes"

---

## Step 3: Agent Mode

### 🎯 Goal
Use Agent Mode to add participant lists to activity cards and implement unregister functionality.

### Activities Checklist
- ✅ Switch to Agent Mode
- ✅ Add files as context (`app.js`, `index.html`, `styles.css`)
- ✅ Display participants in activity cards
- ✅ Add delete icons next to participants
- ✅ Implement unregister functionality
- ✅ Fix the auto-refresh bug
- ✅ Commit and push changes

### Prompt for Showing Participants

**Files to add as context:**
- `src/static/app.js`
- `src/static/index.html`
- `src/static/styles.css`

**Prompt:**
```prompt
Hey Copilot, can you please edit the activity cards to add a participants section.
It will show what participants that are already signed up for that activity as a bulleted list.
Remember to make it pretty!
```

### Example JavaScript Changes

**In `src/static/app.js`, update the activity card HTML:**
```javascript
activityCard.innerHTML = `
  <h4>${name}</h4>
  <p>${details.description}</p>
  <p><strong>Schedule:</strong> ${details.schedule}</p>
  <p><strong>Availability:</strong> ${spotsLeft} spots left</p>
  <div class="participants-section">
    <h5>Current Participants:</h5>
    <ul>
      ${details.participants.map(email => `<li>${email}</li>`).join('')}
    </ul>
  </div>
`;
```

### Prompt for Unregister Feature

```prompt
#codebase Please add a delete icon next to each participant and hide the bullet points.
When clicked, it will unregister that participant from the activity.
```

### Backend Endpoint for Unregister

**Add to `src/app.py`:**
```python
@app.delete("/activities/{activity_name}/signup")
def unregister_from_activity(activity_name: str, email: str):
    """Unregister a student from an activity"""
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")
    
    activity = activities[activity_name]
    
    if email not in activity["participants"]:
        raise HTTPException(status_code=404, detail="Student not found in activity")
    
    activity["participants"].remove(email)
    return {"message": f"Unregistered {email} from {activity_name}"}
```

### Prompt for Auto-Refresh Bug

```prompt
I've noticed there seems to be a bug.
When a participant is registered, the page must be refreshed to see the change on the activity.
```

**Expected fix:** Add `fetchActivities()` call after successful signup/unregister.

---

## Step 4: Plan Agent

### 🎯 Goal
Use Plan Agent to design a testing strategy, then implement backend tests with pytest.

### Activities Checklist
- ✅ Switch to Plan Mode
- ✅ Request a plan for adding backend tests
- ✅ Answer clarifying questions
- ✅ Refine the plan with additional requirements
- ✅ Start implementation (switches to Agent Mode)
- ✅ Ensure all tests pass
- ✅ Commit and push changes

### Initial Prompt

```prompt
I want to add backend FastAPI tests in a separate tests directory.
```

### Follow-up Refinements

```prompt
Let's use the AAA (Arrange-Act-Assert) testing pattern to structure our tests
```

```prompt
Make sure we use `pytest` and add it to `requirements.txt` file
```

### Example Test File Structure

**`tests/test_app.py`:**
```python
import pytest
from fastapi.testclient import TestClient
from src.app import app, activities

@pytest.fixture
def client():
    """Create a test client"""
    return TestClient(app)

@pytest.fixture(autouse=True)
def reset_activities():
    """Reset activities data before each test"""
    activities.clear()
    activities.update({
        "Chess Club": {
            "description": "Learn strategies and compete in chess tournaments",
            "schedule": "Fridays, 3:30 PM - 5:00 PM",
            "max_participants": 12,
            "participants": ["michael@mergington.edu"]
        }
    })

def test_get_activities(client):
    """Test GET /activities endpoint"""
    # Arrange - done in fixture
    
    # Act
    response = client.get("/activities")
    
    # Assert
    assert response.status_code == 200
    assert "Chess Club" in response.json()

def test_signup_for_activity(client):
    """Test POST /activities/{activity_name}/signup"""
    # Arrange
    email = "test@mergington.edu"
    
    # Act
    response = client.post(
        "/activities/Chess Club/signup",
        params={"email": email}
    )
    
    # Assert
    assert response.status_code == 200
    assert email in activities["Chess Club"]["participants"]

def test_signup_duplicate_prevention(client):
    """Test that duplicate signups are prevented"""
    # Arrange
    email = "michael@mergington.edu"  # Already signed up
    
    # Act
    response = client.post(
        "/activities/Chess Club/signup",
        params={"email": email}
    )
    
    # Assert
    assert response.status_code == 400
    assert "already signed up" in response.json()["detail"].lower()

def test_signup_nonexistent_activity(client):
    """Test signup for non-existent activity"""
    # Arrange
    email = "test@mergington.edu"
    
    # Act
    response = client.post(
        "/activities/Nonexistent Activity/signup",
        params={"email": email}
    )
    
    # Assert
    assert response.status_code == 404
```

### Update `requirements.txt`

```txt
fastapi
uvicorn
httpx
watchfiles
pytest
```

### Running Tests

```bash
pytest tests/ -v
```

---

## Step 5: Pull Request Features

### 🎯 Goal
Create a PR and use Copilot's PR summary and code review features.

### Activities Checklist
- ✅ Navigate to GitHub repository
- ✅ Create new pull request
- ✅ (Optional) Use Copilot to generate PR summary
- ✅ (Optional) Request Copilot code review
- ✅ Merge the pull request

### Pull Request Details

- **Base branch:** `main`
- **Compare branch:** `accelerate-with-copilot`
- **Title:** `Improve student activity registration system`

### Using Copilot PR Summary

1. In the PR description toolbar, click the **Copilot** icon
2. Select **Summary** action
3. Wait for Copilot to generate a description

### Using Copilot Code Review

1. In the right sidebar, find **Reviewers** section
2. Click **Request** button next to Copilot icon
3. Wait for Copilot to review and comment

### Merge the PR

Once satisfied with the PR, click **Merge pull request** button.

---

## Common Issues & Troubleshooting

### Codespace Issues

**Issue:** Codespace won't start
- **Solution:** Check GitHub Copilot subscription is active
- **Solution:** Try creating a new Codespace

**Issue:** Extensions not working
- **Solution:** Reload window (`Ctrl+Shift+P` → "Reload Window")
- **Solution:** Check extension is enabled in Extensions tab

### Application Issues

**Issue:** App won't run
- **Solution:** Check `requirements.txt` dependencies are installed
- **Solution:** Run `pip install -r requirements.txt`
- **Solution:** Check port 8000 is not in use

**Issue:** Can't see changes on website
- **Solution:** Hard refresh the browser (`Ctrl+Shift+R` or `Cmd+Shift+R`)
- **Solution:** Open in private/incognito window
- **Solution:** Restart the debugger

### Git/Branch Issues

**Issue:** Branch not being detected
- **Solution:** Ensure branch name is exactly `accelerate-with-copilot`
- **Solution:** Check branch is pushed: `git push -u origin accelerate-with-copilot`
- **Solution:** Verify in GitHub: Settings → Branches

**Issue:** Changes not pushing
- **Solution:** Commit changes first in Source Control tab
- **Solution:** Click "Sync Changes" button
- **Solution:** Check git credentials are configured

### Copilot Issues

**Issue:** Copilot not responding
- **Solution:** Accept usage terms if prompted
- **Solution:** Check Copilot subscription is active
- **Solution:** Try different model (Claude, GPT-4, etc.)

**Issue:** Copilot suggestions don't appear
- **Solution:** Wait a moment after typing
- **Solution:** Press `Tab` to accept shadow text
- **Solution:** Use `Ctrl+Enter` to show multiple suggestions

**Issue:** Agent Mode not available
- **Solution:** Update VS Code to latest version
- **Solution:** Update GitHub Copilot extension
- **Solution:** Check feature is available in your region

### Test Issues

**Issue:** Tests failing
- **Solution:** Check pytest is installed: `pip install pytest`
- **Solution:** Verify test file starts with `test_`
- **Solution:** Check import paths are correct

**Issue:** Can't run tests
- **Solution:** Run from terminal: `pytest tests/ -v`
- **Solution:** Check pytest.ini configuration
- **Solution:** Activate virtual environment if using one

---

## Additional Resources

- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pytest Documentation](https://docs.pytest.org/)
- [VS Code Copilot Features](https://code.visualstudio.com/docs/copilot/overview)
- [GitHub Copilot Features](https://docs.github.com/en/copilot/about-github-copilot/github-copilot-features)

---

## Tips for Success

1. **Be specific in prompts:** Clear, detailed instructions get better results
2. **Iterate on responses:** If Copilot doesn't get it right, refine your prompt
3. **Provide context:** Add relevant files to chat context or use `#codebase`
4. **Experiment with models:** Different models have different strengths
5. **Review suggestions:** Always verify Copilot's code before accepting
6. **Use the right mode:** Match the interaction mode to your task
7. **Break down complex tasks:** Start with a plan, then implement step by step

---

## Congratulations! 🎉

You've completed the GitHub Copilot exercise! You now know how to:
- Use different Copilot modes effectively
- Fix bugs with AI assistance
- Generate code and tests
- Leverage Copilot for PR workflows

Keep practicing and exploring Copilot's capabilities in your own projects!
