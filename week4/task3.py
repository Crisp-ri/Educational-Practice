import os
from dotenv import load_dotenv

load_dotenv()

db_url = os.getenv("DB_URL")
api_key = os.getenv("API_KEY")

print(db_url)
print(api_key)
