import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'contproject'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or '7eQOPcvS9Cr3G6KNPvWbk9V339+8i1vsc2LPuMXGLX6CMZkxjbAypYptpddH4DDzmsV/19I/nIH4aaNn5PMc6g=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'projcontainer'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'sqldataproj.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'Project'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'admin1'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'Database1'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET = "fp.uq1SBgyb_O7Ak0J0TLr~p~Kz-~2jGk6"
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    # if not CLIENT_SECRET:
    #     raise ValueError("Need to define CLIENT_SECRET environment variable")

    AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

    CLIENT_ID = "6e8a6b68-63a8-471b-ad07-17b953f30aba"

    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session
