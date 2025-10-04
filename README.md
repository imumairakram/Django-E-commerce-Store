# 🛍️ Django E-Commerce Platform

![Django](https://img.shields.io/badge/Framework-Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![HTML](https://img.shields.io/badge/Frontend-HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/Style-CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Bootstrap](https://img.shields.io/badge/UI-Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

---

## 🧾 Overview

A fully functional **E-Commerce Web Application** built with **Django** and **Python**.  
It allows users to browse products, add them to their cart, and place orders — with a clean, professional, and responsive UI.

This project is ideal for beginners learning Django’s **Models–Views–Templates (MVT)** architecture and for developers exploring full-stack web app development using **Django Admin** and relational databases.

---

## 🚀 Features

✅ User Authentication (Sign Up / Login / Logout)  
✅ Product Listing with Images, Prices, and Details  
✅ Add to Cart & Manage Cart Items  
✅ Secure Checkout & Order Placement  
✅ Order Management through Admin Panel  
✅ Responsive Frontend (Bootstrap Integrated)  
✅ Order History for Logged-in Users  

---

## 🧱 Tech Stack

| Layer | Technology |
|-------|-------------|
| **Frontend** | HTML5, CSS3, Bootstrap |
| **Backend** | Python (Django Framework) |
| **Database** | SQLite (default) / PostgreSQL |
| **Version Control** | Git & GitHub |
| **Admin Panel** | Django Admin |
| **Environment** | Virtualenv / Anaconda |

---

## ⚙️ Installation & Setup Guide

Follow these steps to set up and run the project locally:

```bash
# 1️⃣ Clone the repository
git clone https://github.com/imumairakram/django-e-commerce-store.git
cd ecommerce-django

# 2️⃣ Create a virtual environment
python -m venv venv
venv\Scripts\activate   # (Windows)
# source venv/bin/activate  # (Mac/Linux)

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Run database migrations
python manage.py makemigrations
python manage.py migrate

# 5️⃣ Create a superuser for admin access
python manage.py createsuperuser

# 6️⃣ Start the development server
python manage.py runserver
