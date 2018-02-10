from .base import *
import os

DEBUG = False
ALLOWED_HOSTS = ["herokuapp.com"]
SECRET_KEY = os.environ.get('SECRET_KEY')
