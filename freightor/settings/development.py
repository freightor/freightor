from .base import *
import os

DEBUG = True
SECRET_KEY = os.environ.get('SECRET_KEY')
