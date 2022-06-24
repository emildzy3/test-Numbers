
from googleapiclient.errors import HttpError

from config.settings import SERVICE_ACCOUNT_FILE, SCOPES, SAMPLE_SPREADSHEET_ID, SAMPLE_RANGE_NAME
from googleapiclient.discovery import build
from google.oauth2 import service_account

from exceptions import CantGetData


def _get_data() -> tuple:
    """Service for getting raw data from Google Sheets"""
    result = _connect_Gsheets()
    data = result['values'][1:]
    result_tuple = []
    for element in data:
        result_tuple.append(element)
    return tuple(result_tuple)


def _connect_Gsheets():
    try:
        credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    except FileNotFoundError:
        raise CantGetData
    service = build('sheets', 'v4', credentials=credentials).spreadsheets().values()
    try:
        result = service.get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                             range=SAMPLE_RANGE_NAME).execute()
        return result
    except HttpError:
        raise CantGetData
