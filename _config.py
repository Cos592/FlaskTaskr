import os
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = "flasktaskr.db"
USERNAME = "admin"
PASSWORD = "admin"
WTF_CSRF_ENABLED = True
SECRET_KEY = "9dksfldjldmsklnvkdlkldslfenklneiowfnoewno34n25328583425y4829f"

DATABASE_PATH = os.path.join(basedir+'\\'+DATABASE)