import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b"J\x02\x1e\xcd\xc1\xcbJ'\xd8\x97\xd0w\x08\xa6ey"
    
    MONGODB_SETTINGS = { 'db' : 'UTA_Enrollment' }