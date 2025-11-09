import os
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def save_lead(name, email, phone):
    """Salva lead na planilha do Google Sheets"""
    try:
        creds_json = os.getenv("GOOGLE_CREDENTIALS")

        if not creds_json:
            raise ValueError("Variável de ambiente GOOGLE_CREDENTIALS não encontrada")

        creds_dict = json.loads(creds_json)

        scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive"
        ]

        creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
        client = gspread.authorize(creds)

        sheet = client.open("leadsfinancemind").sheet1
        sheet.append_row([name, email, phone])

        return {"success": True, "message": "Lead salvo com sucesso!"}

    except Exception as e:
        import traceback
        traceback.print_exc()
        return {"success": False, "message": str(e)}
