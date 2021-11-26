from logging import DEBUG
from dotenv import load_dotenv
import os
load_dotenv()
user = os.environ.get("MYSQL_USER")
password = os.environ.get("MYSQL_PASSWORD")
db = os.environ.get("MYSQL_DATABASE")
host = os.environ.get("MYSQL_HOST")

url_connection = f"mysql://{user}:{password}@{host}/{db}"