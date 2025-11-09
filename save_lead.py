import os
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def save_lead(name, email, phone):
    """Salva lead na planilha do Google Sheets"""
    try:
        # Carregar credenciais da variável de ambiente
        creds_json = os.getenv("GOOGLE_CREDENTIALS")
        
        if not creds_json:
            raise ValueError("GOOGLE_CREDENTIALS não encontrada nas variáveis de ambiente")
        
        # Converter string JSON para dicionário
        creds_dict = json.loads(creds_json)
        
        # Configurar credenciais
        scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive"
        ]
        
        creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
        client = gspread.authorize(creds)
        
        # Abrir planilha
        sheet = client.open("leadsfinancemind").sheet1
        
        # Adicionar lead
        sheet.append_row([name, email, phone])
        
        return {"success": True, "message": "Lead salvo com sucesso!"}
        
    except Exception as e:
        import traceback
        traceback.print_exc()
        return {"success": False, "message": str(e)}