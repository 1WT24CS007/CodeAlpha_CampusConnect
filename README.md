# 🎓 CampusConnect

CampusConnect is a **college student social media platform** developed using Django. It provides a common platform where students can connect with other students, share posts, interact through likes and comments, follow other users, view profiles, and participate in college clubs and activities.

## 📌 Project Overview

CampusConnect is designed to improve communication and interaction among college students through a simple and user-friendly web application.

Students can create accounts, log in, create posts, interact with other users, follow students, and explore different college clubs.

## ✨ Features

### 👤 User Management
- User registration
- User login and logout
- Secure password authentication
- User profiles
- Email information
- Password management

### 📝 Posts
- Create new posts
- View posts in the campus feed
- Display posts from different users
- View post creation time

### ❤️ Likes
- Like posts
- Unlike posts
- Prevent duplicate likes from the same user

### 💬 Comments
- Add comments to posts
- Display comments associated with posts

### 👥 Follow System
- Follow other students
- View people to follow
- Track followers
- Track following count

### 🎓 College Clubs
CampusConnect provides different college clubs, including:

- 💻 Coding Club
- ⚽ Sports Club
- 📚 Literary Club
- 🤖 Robotics Club
- 🎨 Cultural Club

Students can view club information and join available clubs.

### 📢 Campus Information
- Events section
- Announcements section
- College-related information

### 🎨 User Interface
- Clean and simple design
- Responsive layout
- Consistent teal-themed interface
- Easy navigation between pages

---

## 🛠️ Technologies Used

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Python
- Django

### Database
- SQLite

### Development Tools
- Visual Studio Code
- Git
- GitHub

---

## 🏗️ Project Structure

```text
CampusConnect/
│
├── campusconnect/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── users/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   └── apps.py
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── home.html
│   ├── profile.html
│   ├── create_post.html
│   ├── events.html
│   ├── announcements.html
│   ├── clubs.html
│   ├── coding.html
│   ├── sports.html
│   ├── literary.html
│   ├── robotics.html
│   ├── cultural.html
│   ├── join_coding.html
│   ├── join_sports.html
│   ├── join_literary.html
│   ├── join_robotics.html
│   ├── join_cultural.html
│   └── join_success.html
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🗄️ Database Models

CampusConnect uses SQLite with Django models.

### Post
Stores posts created by users.

**Fields:**
- User
- Content
- Created date and time

### Like
Stores likes given to posts.

**Fields:**
- User
- Post

A unique constraint prevents the same user from liking the same post multiple times.

### Comment
Stores comments made on posts.

**Fields:**
- User
- Post
- Comment text
- Created date and time

### Follow
Stores relationships between users.

**Fields:**
- Follower
- Following

A unique constraint prevents duplicate follow relationships.

---

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/1WT24CS007/CampusConnect.git
```

### 2. Open the project folder

```bash
cd CampusConnect
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install django
```

If a `requirements.txt` file is available:

```bash
pip install -r requirements.txt
```

### 6. Apply migrations

```bash
python manage.py migrate
```

### 7. Create a superuser

```bash
python manage.py createsuperuser
```

Follow the instructions in the terminal.

### 8. Start the development server

```bash
python manage.py runserver
```

### 9. Open the application

Open the following address in your browser:

```text
http://127.0.0.1:8000/
```

---

## 🔐 Authentication Flow

The application follows this basic authentication flow:

```text
Register
   ↓
Login
   ↓
Home Page
   ↓
Profile / Posts / Clubs
   ↓
Logout
```

---

## 🔄 Application Workflow

```text
User Registration
       ↓
     Login
       ↓
   Home Page
       ↓
 ┌─────┼─────────┬──────────┐
 ↓     ↓         ↓          ↓
Posts Profile  Clubs    Events
 ↓
Like / Comment
 ↓
Follow Users
```

---

## 🎯 Project Objectives

The main objectives of CampusConnect are:

1. To create a digital platform for college students.
2. To provide an easy way for students to communicate.
3. To allow students to share posts and interact with others.
4. To implement a follow system between users.
5. To provide information about college clubs and activities.
6. To practice full-stack web development using Django.
7. To understand database integration using SQLite.

---

## 🌟 Advantages

- Simple and user-friendly interface
- Easy student interaction
- Centralized campus communication
- Supports social networking features
- Provides college club information
- Uses Django's authentication system
- Easy to extend with additional features

---

## 🚀 Future Enhancements

The project can be further improved by adding:

- 🔔 Real-time notifications
- 💬 Real-time chat
- 📸 Image and video sharing
- 🔍 User and post search
- 📱 Mobile application
- 🏫 College-specific communities
- 📅 Event registration
- 🔔 Club notifications
- 👤 Profile picture support
- 🌙 Dark mode
- ☁️ Cloud database and deployment

---

## 📸 Screenshots

Add screenshots of your application here.

### Login Page

```text
Add your Login page screenshot here
```

### Home Page

```text
Add your Home page screenshot here
```

### Profile Page

```text
Add your Profile page screenshot here
```

### Clubs Page

```text
Add your Clubs page screenshot here
```

### Create Post Page

```text
Add your Create Post page screenshot here
```

---

## 🧪 Testing

The following functionalities were tested during development:

| Feature | Status |
|---|---|
| User Registration | ✅ Working |
| User Login | ✅ Working |
| User Logout | ✅ Working |
| User Profile | ✅ Working |
| Create Post | ✅ Working |
| Like Post | ✅ Working |
| Comment on Post | ✅ Working |
| Follow User | ✅ Working |
| Follower Count | ✅ Working |
| Coding Club | ✅ Working |
| Sports Club | ✅ Working |
| Literary Club | ✅ Working |
| Robotics Club | ✅ Working |
| Cultural Club | ✅ Working |
| Club Registration | ✅ Working |

---

## 🎓 Internship Project

**Project Name:** CampusConnect  
**Project Type:** Full Stack Web Development  
**Internship:** CodeAlpha Full Stack Development Internship

### Technologies

```text
Python
Django
HTML
CSS
JavaScript
SQLite
Git
GitHub
```

---

## 👨‍💻 Developer

**GitHub:**  
https://github.com/1WT24CS007

**Repository:**  
https://github.com/1WT24CS007/CampusConnect

---

## 📄 License

This project was developed for educational and internship purposes.

---

## ⭐ Acknowledgement

This project was developed as part of a **Full Stack Development internship** to gain practical experience in frontend development, backend development, database management, authentication, and version control using Git and GitHub.

If you find this project useful, consider giving the repository a ⭐.
