# 🧾 Flask + PostgreSQL Sales Data App (Dockerized)

A lightweight, containerized web application that allows users to enter sales data via a Flask form and store it in a PostgreSQL database. Includes pgAdmin for database management and Docker Compose for orchestration.

---

## 🚀 Features

- Submit customer name, amount, and date via web form
- Validates:
  - ✅ Name: letters only
  - ✅ Amount: numeric (float allowed)
  - ✅ Date: format `dd/mm/yyyy`
- Automatically inserts records into PostgreSQL
- Use pgAdmin to browse, query, and manage the database

---

## 🧱 Tech Stack

- Python + Flask
- PostgreSQL 13
- pgAdmin 4 (browser GUI)
- Docker + Docker Compose

---

## 📁 Folder Structure

flask_sales_app/
├── docker-compose.yaml
├── flask_app/
│ ├── Dockerfile
│ └── app.py
└── README.md
