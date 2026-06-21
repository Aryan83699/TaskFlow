# TaskFlow

<p align="left">
  <img src="https://readme-typing-svg.demolab.com?font=Poppins&size=24&pause=1000&color=2563EB&center=false&vCenter=true&width=700&lines=Calendar-Based+Task+Management;Flask+%2B+SQLite+%2B+MongoDB;Email+OTP+Authentication;Interactive+Task+Planner" />
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

</p>

---

# 🌐 Live Demo

<p align="left">

<a href="https://taskflow-2-ysnv.onrender.com/" target="_blank">
  <img src="https://img.shields.io/badge/Live_Demo-Render-46E3B7?style=for-the-badge&logo=render&logoColor=white" />
</a>

</p>

## Overview

TaskFlow is a full-stack web application that enables users to organize and manage daily tasks through an interactive calendar interface.

The application provides secure Email OTP authentication, stores user credentials in SQLite, and manages task data in MongoDB Atlas. Users can seamlessly create, view, update, and delete tasks without page reloads using the Fetch API and asynchronous requests.

---

## Features

- User Registration
- Email OTP Verification
- Secure Login Authentication
- Session Management
- Interactive Calendar Interface
- View Tasks by Date
- Add New Tasks
- Update Task Status
- Delete Tasks

---

## Technology Stack

### Backend

- Python
- Flask
- SQLAlchemy
- PyMongo

### Frontend

- HTML5
- CSS3
- JavaScript
- FullCalendar.js

### Database

- SQLite (User Authentication)
- MongoDB Atlas (Task Storage)

### Additional Tools

- Gmail SMTP
- python-dotenv
- Flask Sessions
- Fetch API

---

## Project Structure

```text
TaskFlow/
│
├── static/
│   ├── css/
│   ├── js/
│   ├── videos/
│   └── images/
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── verify.html
│   └── tasks.html
│
├── app.py
├── requirements.txt
├── users.db
├── .env
└── README.md
```

---

## Database Design

### SQLite (Authentication)

| Field | Type |
|------|------|
| id | Integer |
| email | String |
| password | String |

---

### MongoDB Atlas (Tasks)

```json
{
    "user_id": 1,
    "task": "Learn MongoDB",
    "date": "2026-06-23",
    "completed": false
}
```

---

# 📸 Screenshots


<img width="1603" height="872" alt="Screenshot 2026-06-21 155336" src="https://github.com/user-attachments/assets/4feaf480-b11d-4a00-8df9-7725e3fa390d" />
<br><br>
<img width="1676" height="860" alt="Screenshot 2026-06-21 155323" src="https://github.com/user-attachments/assets/415a8df7-2a61-421b-a745-fe823d3f6d2f" />
<br><br>
<img width="1547" height="853" alt="Screenshot 2026-06-21 155302" src="https://github.com/user-attachments/assets/7fa69bda-5da2-4723-aab0-74bdaf0bb266" />


---

## Installation

Clone the repository.

```bash
git clone https://github.com/your-username/TaskFlow.git

cd TaskFlow
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Create a `.env` file.

```env
SERVER_EMAIL=your_email@gmail.com

APP_PASS=your_gmail_app_password

MONGODB_URI=your_mongodb_connection_string
```

Run the application.

```bash
python app.py
```

---

## Future Enhancements

- Password Hashing
- Forgot Password
- Task Categories
- Priority Levels
- Search & Filters
- Reminder Notifications
- Dark Mode
- User Profile
- REST API
- Docker Support
- Calendar Event Colors
- Recurring Tasks

---

## Author

**Aryan Singh**

