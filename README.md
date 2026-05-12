📝 Notes API (Django REST Framework)

A simple Notes API built with Django REST Framework that supports JWT authentication, user-based access control, and role-based permissions (User, Staff, Superuser).

🚀 Features

🔐 JWT Authentication (Login & Token Refresh)
👤 Custom User Model (email-based authentication)
📝 CRUD operations for Notes
📌 Pin / Unpin notes feature
🔎 Search, Filter, and Ordering support
👥 Role-based access:
Normal Users → Access only their own notes
Staff → Access and manage multiple users' data (limited control)
Superuser → Full control over all data
📄 Profile system (One-to-One with User)

🛠 Tech Stack

Python
Django
Django REST Framework
Simple JWT
Django Filters
