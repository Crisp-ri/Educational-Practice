# Educational Practice 🎓

This repository contains a collection of practical Python tasks covering backend development fundamentals, including HTTP requests, REST API creation, security protocols, and authentication.

**Repository:** [https://github.com/Crisp-ri/Educational-Practice](https://github.com/Crisp-ri/Educational-Practice)

## 📂 Project Structure

The project is divided into 5 independent tasks:

* **`task1.py`** — **HTTP Requests**: Demonstrates how to send GET and POST requests using the `requests` library to interact with external APIs (jsonplaceholder).
* **`task2.py`** — **REST API (CRUD)**: A basic Flask server implementing Create, Read, Update, and Delete operations for user management.
* **`task3.py`** — **Environment Variables**: Shows how to securely load configuration data (API keys, DB URLs) from a `.env` file using `python-dotenv`.
* **`task4.py`** — **Cryptography**: Covers essential security concepts using the `cryptography` library:
    * Hashing (SHA-256)
    * Symmetric Encryption (AES)
    * Asymmetric Encryption & Digital Signatures (RSA)
* **`task5.py`** — **JWT Authentication**: Implements a secure Flask login system using JSON Web Tokens (PyJWT) to protect API endpoints.

## ⚙️ Prerequisites

Ensure you have Python installed. It is recommended to use a virtual environment. You will need to install the following dependencies:

```bash
pip install requests flask python-dotenv cryptography pyjwt
