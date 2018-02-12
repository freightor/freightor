from .base import *
import os

DEBUG = os.environ.get("DB_DEBUG")
ALLOWED_HOSTS = ["herokuapp.com"]
SECRET_KEY = os.environ.get('SECRET_KEY')
