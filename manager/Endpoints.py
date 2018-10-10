from enum import Enum

base = 'http://localhost:8000/courser/api/'

class Endpoints(Enum):
    AUTHOR = base + 'author'
    COURSE = base + 'course'
