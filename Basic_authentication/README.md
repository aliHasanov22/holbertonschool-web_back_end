# 🔐 Basic Authentication API

## 📌 Background

This project focuses on understanding how authentication works in web applications by implementing **Basic Authentication** in a simple API using Python and Flask.

In real-world applications, developers usually rely on existing libraries such as `Flask-HTTPAuth` instead of building authentication systems from scratch. However, this project is designed for learning purposes.

---

## 🎯 Learning Objectives

By completing this project, you should be able to explain:

### 🔹 General Concepts
- What authentication means  
- Difference between authentication and authorization  
- Importance of authentication in APIs  

### 🔹 Technical Concepts
- What Base64 is  
- How to encode a string in Base64  
- What Basic Authentication means  
- How to send the Authorization header  

---

## 🧠 Key Concepts

### 🔑 Authentication
Authentication verifies who a user is.

### 🔤 Base64 Encoding
Example:
username:password → dXNlcm5hbWU6cGFzc3dvcmQ=

### 🔐 Basic Authentication
Authorization: Basic <Base64(username:password)>

---

## 🛠️ Technologies Used
- Python 3.9
- Flask
- Base64
- REST API

---

## ⚙️ Requirements
- Ubuntu 20.04
- Python 3.9
- pycodestyle 2.5

---

## 🚀 Example Request

curl -H "Authorization: Basic dXNlcjpwYXNz" http://localhost:5000/api/v1/protected

---

## ⚠️ Note
Use HTTPS in production. Basic Auth alone is not secure.

---

## ✍️ Author
Ali Hasanov
