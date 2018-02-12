from .base import *
import os

DEBUG = os.environ.get("DB_DEBUG")
SECRET_KEY = os.environ.get('SECRET_KEY')
