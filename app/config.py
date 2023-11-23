# config.py
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv('EMAIL')
AUTH_TOKEN = os.getenv('AUTH_TOKEN')