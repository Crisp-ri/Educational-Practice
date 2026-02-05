import os
import subprocess
import sys
import time

# --- КОНФІГУРАЦІЯ ФАЙЛІВ (Вбудовані у скрипт) ---

# 1. requirements.txt
REQ_TXT = """
flask
psycopg2-binary
"""

# 2. app.py (Код нашого Flask сервера)
APP_PY = """
import os
import time
import psycopg2
from flask import Flask

app = Flask(__name__)

# Налаштування з змінних оточення
DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_NAME = os.environ.get('POSTGRES_DB', 'testdb')
DB_USER = os.environ.get('POSTGRES_USER', 'user')
DB_PASS = os.environ.get('POSTGRES_PASSWORD', 'password')

def get_db_connection():
    retries = 10
    while retries > 0:
        try:
            print(f"Connecting to DB at {DB_HOST}...", flush=True)
            conn = psycopg2.connect(
                host=DB_HOST,
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASS
            )
            return conn
        except psycopg2.OperationalError as e:
            print(f"DB not ready yet, waiting... ({e})", flush=True)
            retries -= 1
            time.sleep(2)
    return None

@app.route('/')
def index():
    conn = get_db_connection()
    if conn:
        cur = conn.cursor()
        cur.execute('SELECT version();')
        db_version = cur.fetchone()
        cur.close()
        conn.close()
        return f'''
        <div style="text-align: center; margin-top: 50px; font-family: sans-serif;">
            <h1 style="color: green;">Успіх! 🚀</h1>
            <p>Flask успішно з'єднався з PostgreSQL.</p>
            <div style="background: #f0f0f0; padding: 10px; display: inline-block; border-radius: 5px;">
                <strong>Версія БД:</strong> {db_version[0]}
            </div>
        </div>
        '''
    else:
        return "<h1 style='color: red;'>Помилка підключення до БД :(</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
"""

# 3. Dockerfile
DOCKERFILE = """
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
EXPOSE 5000
CMD ["python", "app.py"]
"""

# 4. docker-compose.yml
DOCKER_COMPOSE = """
version: '3.8'

services:
  web:
    build: .
    ports:
      - "5000:5000"
    depends_on:
      - db
    environment:
      - DB_HOST=db
      - POSTGRES_DB=mydb
      - POSTGRES_USER=admin
      - POSTGRES_PASSWORD=secret

  db:
    image: postgres:15-alpine
    environment:
      - POSTGRES_DB=mydb
      - POSTGRES_USER=admin
      - POSTGRES_PASSWORD=secret
    volumes:
      - pg_data_volume:/var/lib/postgresql/data

volumes:
  pg_data_volume:
"""

# --- ЛОГІКА СКРИПТА ---

PROJECT_DIR = "docker_flask_demo"

def create_files():
    """Створює папку проекту та записує необхідні файли"""
    if not os.path.exists(PROJECT_DIR):
        os.makedirs(PROJECT_DIR)
        print(f"[+] Створено папку: {PROJECT_DIR}")
    
    files = {
        "requirements.txt": REQ_TXT,
        "app.py": APP_PY,
        "Dockerfile": DOCKERFILE,
        "docker-compose.yml": DOCKER_COMPOSE
    }

    for filename, content in files.items():
        path = os.path.join(PROJECT_DIR, filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content.strip())
        print(f"[+] Записано файл: {filename}")

def run_docker():
    """Запускає docker-compose"""
    print("\n[+] Запуск Docker Compose... (Натисніть Ctrl+C для зупинки)\n")
    try:
        # Змінюємо робочу директорію на папку проекту
        os.chdir(PROJECT_DIR)
        
        # Запускаємо збірку і старт
        subprocess.run(["docker-compose", "up", "--build"], check=True)
    except KeyboardInterrupt:
        print("\n[!] Зупинка контейнерів...")
        subprocess.run(["docker-compose", "down"])
        print("[!] Контейнери зупинено.")
    except FileNotFoundError:
        print("\n[ERROR] Не знайдено команду 'docker-compose'. Переконайтеся, що Docker встановлено.")
    except Exception as e:
        print(f"\n[ERROR] Сталася помилка: {e}")

if __name__ == "__main__":
    print("--- АВТОМАТИЧНИЙ ЗАПУСК DOCKER ПРОЕКТУ ---")
    create_files()
    run_docker()
