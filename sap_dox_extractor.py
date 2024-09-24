import os
import requests
import json
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Load config.json
with open('config.json') as config_file:
    config = json.load(config_file)

SAP_DOX_URL = config["sap_dox_url"]
TOKEN_URL = config["token_url"]
CLIENT_ID = config["client_id"]
CLIENT_SECRET = config["client_secret"]

DOCUMENTS_DIR = 'documents/'

def get_access_token():
    # Retrieve OAuth token from SAP Document Info Extraction
    data = {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }
    response = requests.post(TOKEN_URL, data=data)
    response_data = response.json()
    return response_data['access_token']

def upload_document(file_path, token):
    # Upload PDF document to SAP DOX for extraction
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    
    files = {
        'file': open(file_path, 'rb')
    }
    response = requests.post(f"{SAP_DOX_URL}/document/jobs", headers=headers, files=files)
    return response.json()

def process_documents():
    # Process all PDF documents in the folder
    token = get_access_token()
    
    for filename in os.listdir(DOCUMENTS_DIR):
        if filename.endswith(".pdf"):
            file_path = os.path.join(DOCUMENTS_DIR, filename)
            print(f"Processing {file_path}")
            response = upload_document(file_path, token)
            print(f"Response: {response}")

if __name__ == "__main__":
    process_documents()
