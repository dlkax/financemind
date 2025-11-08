import os
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from io import StringIO

# Lê o JSON direto da variável de ambiente
creds_json = os.getenv("GOOGLE_CREDENTIALS")
creds_dict = json.load(StringIO(creds_json))

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
client = gspread.authorize(creds)

sheet = client.open("leadsfinancemind").sheet1
