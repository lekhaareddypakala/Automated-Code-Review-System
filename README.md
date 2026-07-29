# Automated Code Review System

## Overview

The Automated Code Review System is a Flask-based web application developed to help students improve their Python programming skills by automatically reviewing their code.

The system analyzes submitted Python programs, detects syntax errors, identifies runtime issues, evaluates code quality, provides detailed explanations, and calculates performance marks based on code improvements.

---

## Features

### User Authentication
- User registration and login system
- Personalized dashboard for users
- Secure user session management

### Automated Code Analysis
- Submit Python code directly through the web interface
- Detect syntax errors using Python analysis techniques
- Identify runtime errors during execution
- Provide detailed error explanations

### Error Explanation Module
For every detected issue, the system provides:
- Error description
- Reason behind the error
- Explanation of the problem
- Solution guidance
- Correct example for better understanding

### Code Quality Analysis
The system evaluates code based on:
- Code readability
- Coding practices
- Naming conventions
- Complexity analysis
- Maintainability

### Marks Calculation
- Generates marks based on detected issues and improvements
- Helps students measure their coding progress

### Review History
- Stores previously reviewed programs
- Allows users to track their coding journey
- Maintains review records

### Leaderboard
- Displays user performance rankings
- Encourages continuous learning and improvement

---

## Technologies Used

### Frontend
- HTML
- CSS
- Bootstrap

### Backend
- Python
- Flask

### Database
- MySQL

### Tools
- Visual Studio Code
- MySQL Workbench
- Git & GitHub

### Python Modules
- Flask
- MySQL Connector
- AST (Abstract Syntax Tree)
- Python Runtime Execution Modules

---

## Project Structure

```
Automated-Code-Review-System/

│
├── app.py                  # Flask application
├── config.py               # Database configuration
├── database.sql            # Database schema
├── requirements.txt        # Project dependencies
│
├── analyzers/
│   ├── syntax_checker.py
│   ├── runtime_checker.py
│   ├── quality_checker.py
│   ├── explanation_engine.py
│   ├── marks_calculator.py
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── review.html
│   ├── history.html
│   ├── leaderboard.html
│
├── static/
│   └── css/
│       └── style.css
│
└── .gitignore
```

---

## Installation and Setup

### 1. Clone Repository

```bash
git clone https://github.com/lekhaareddypakala/Automated-Code-Review-System.git
```

### 2. Navigate to Project Directory

```bash
cd Automated-Code-Review-System
```

### 3. Create Virtual Environment

```bash
python -m venv venv
```

### 4. Activate Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

### 5. Install Required Packages

```bash
pip install -r requirements.txt
```

### 6. Database Configuration

- Open MySQL Workbench
- Execute `database.sql`
- Update database credentials in `config.py`

### 7. Run Application

```bash
python app.py
```

Application will run at:

```
http://127.0.0.1:5000/
```

---

## System Workflow

1. User registers and logs into the system.
2. User submits Python code for review.
3. The system performs:
   - Syntax checking
   - Runtime error detection
   - Code quality analysis
4. Errors are explained with solutions.
5. Marks are calculated based on the review.
6. Review history and leaderboard are updated.

---

## Future Enhancements

- Support for multiple programming languages
- AI-based intelligent code suggestions
- Advanced code similarity detection
- Cloud deployment
- Real-time collaborative code review

---

## Author

**Lekhaa Reddy**

Computer Science and Engineering

---

## License

This project is developed for educational and learning purposes.
