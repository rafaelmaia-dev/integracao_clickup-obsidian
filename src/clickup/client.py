from src.config import Config
from src.utils.logger import logger
import requests

class ClickUpClient:

    def __init__(self, token: str):
        if not token:
            raise ValueError("Token não pode ser vazio. ")
        
        self.token = token
        self.base_url = Config.CLICKUP_API_URL

        self.headers = {
            "Authorization": self.token,
            "Content-Type": "application/json"
        }

        logger.info("ClickUpClient inicializado com sucesso. ")

    def get_teams(self):
        url =  f"{self.base_url}/team"

        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            logger.info("Teams buscados com sucesso. ")
            return response.json()
        
        except requests.RequestExceptions as e:
            logger.error(f"Erro ao buscar o teams: {e} ")
            raise


    def get_spaces(self, team_id: str):

        if not team_id:
            raise ValueError("team_id não pode ser vazio. ")
        
        url = f"{self.base_url}/team/{team_id}/space"

        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            logger.info(f"Spaces do team {team_id} buscados com sucesso. ")
            return response.json()
        
        except requests.exceptions.RequestException as e:
            logger.error(f"Erro ao buscar o spaces: {e}")
            raise

        

        
            

 


