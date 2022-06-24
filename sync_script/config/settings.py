import os
from pathlib import Path


##################################################################
# Google Sheets settings
##################################################################
BASE_DIR = Path(__file__).parents[0]
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
SERVICE_ACCOUNT_FILE = os.path.join(BASE_DIR, 'credentials.json')
SAMPLE_SPREADSHEET_ID = '1VuNKORnuTib8k1mMIjqrEms6VungKDuveLvJFMCza4c'
SAMPLE_RANGE_NAME = 'TestList!A1:D'


##################################################################
# Database settings
# ##################################################################

DATABASE = "numbers"
USER = "numbers_admin"
PASSWORD = "140944"
HOST = "db"
PORT = "5432"
