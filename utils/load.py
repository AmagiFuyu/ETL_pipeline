import pandas as pd

# Google Sheets
import gspread
from gspread_dataframe import set_with_dataframe
from google.oauth2.service_account import Credentials

def save_to_csv(df: pd.DataFrame, filename="products.csv"):
    df.to_csv(filename, index=False)
    print(f"Data berhasil disimpan ke {filename}")

def save_to_google_sheets(df: pd.DataFrame, creds_file="google-sheets-api.json"):
    # ID spreadsheet dari URL
    spreadsheet_id = "1k92AH9CeNIfPGcev74udCj_TgyFNLS1tQ4tWfuQtyns"
    sheet_name = "Sheet1"

    # Autentikasi dengan service account
    scopes = ["https://www.googleapis.com/auth/spreadsheets"]
    credentials = Credentials.from_service_account_file(creds_file, scopes=scopes)
    client = gspread.authorize(credentials)

    # Buka spreadsheet berdasarkan ID
    spreadsheet = client.open_by_key(spreadsheet_id)

    try:
        worksheet = spreadsheet.worksheet(sheet_name)
        worksheet.clear()
    except gspread.WorksheetNotFound:
        worksheet = spreadsheet.add_worksheet(title=sheet_name, rows=str(len(df)), cols=str(len(df.columns)))

    # Tulis DataFrame ke Google Sheets
    set_with_dataframe(worksheet, df)
    print(f"Data berhasil disimpan ke Google Sheets: {spreadsheet.title} - {sheet_name}")