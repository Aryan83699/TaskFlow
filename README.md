# Smart To-Do Calendar

<p align="left">
  <img src="https://readme-typing-svg.demolab.com?font=Poppins&size=24&pause=1000&color=2563EB&center=false&vCenter=true&width=700&lines=Calendar-Based+Task+Management;Flask+%2B+SQLite+%2B+MongoDB;Email+OTP+Authentication;Interactive+Task+Planner" />
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge\&logo=flask)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge\&logo=sqlite\&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge\&logo=mongodb\&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge\&logo=javascript\&logoColor=black)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge\&logo=html5\&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge\&logo=css3\&logoColor=white)

</p>

---

## Overview

Smart To-Do Calendar is a full-stack web application that enables users to manage daily tasks directly from an interactive calendar.

The application provides secure authentication using Email OTP verification, stores user credentials in SQLite, and manages tasks in MongoDB. Users can add, view, update, and delete tasks without reloading the page using the Fetch API.

---

## Features

* User Registration
* Email OTP Verification
* Secure Login Authentication
* Session Management
* Interactive Calendar UI
* View Tasks by Date
* Add New Tasks
* Update Task Status
* Delete Tasks


---

## Technology Stack

### Backend

* Python
* Flask
* SQLAlchemy
* PyMongo

### Frontend

* HTML
* CSS
* JavaScript
* FullCalendar.js

### Database

* SQLite (Authentication)
* MongoDB Atlas (Task Storage)

### Additional Tools

* Gmail SMTP
* python-dotenv
* Flask Sessions

---

## Project Structure

```text
Smart-ToDo-Calendar/
│
├── static/
│   ├── css/
│   ├── js/
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

### SQLite

| Field    | Type    |
| -------- | ------- |
| id       | Integer |
| email    | String  |
| password | String  |

### MongoDB

```json
{
    "user_id": 1,
    "task": "Learn MongoDB",
    "date": "2026-06-23",
    "completed": false
}
```

---

## Screenshots

Add screenshots here.

```
screenshots/
├── login.png
├── register.png
├── otp.png
├── calendar.png
├── view-task.png
├── insert-task.png
└── update-task.png
```

---

## Installation

```bash
git clone https://github.com/your-username/Smart-ToDo-Calendar.git

cd Smart-ToDo-Calendar

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

* Password Hashing
* Forgot Password
* Task Categories
* Priority Levels
* Search & Filters
* Reminder Notifications
* Dark Mode
* User Profile
* REST API
* Docker Deployment

---

## Author

**Aryan Singh**

B.Sc. Information Technology

This project was developed to demonstrate full-stack web development using Flask, SQLAlchemy, MongoDB, JavaScript, and AJAX.
