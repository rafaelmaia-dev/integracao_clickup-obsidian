from dotenv import load_dotenv
from pathlib import Path
import os

result = Path(__file__).parent.parent / ".env"
load_dotenv(result)

class Config:
    CLICKUP_API_URL = "https://api.clickup.com/api/v2"
    CLICKUP_API_TOKEN = os.getenv("CLICKUP_API_TOKEN")
    OBSIDIAN_VAULT_PATH = os.getenv("OBSIDIAN_VAULT_PATH")
   
def validate_config():
    if not Config.CLICKUP_API_TOKEN or not Config.OBSIDIAN_VAULT_PATH:
        raise ValueError("CLICKUP_TOKEN e OBSIDIAN_VAULT_PATH não encontrado")
       
    else:
        print("CLICKUP_TOKEN e OBSIDIAN_VAULT_PATH encontrado.")


