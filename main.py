from app import app
import os

# Used only to run Flask, so setting by default for development
os.environ["FLASK_ENV"] = os.getenv("FLASK_ENV", "development")
app.run(port=5000)