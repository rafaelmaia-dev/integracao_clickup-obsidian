from pathlib import Path
from src.config import Config
from src.utils.logger import logger
import re

class ObsidianWriter:

    def __init__(self, vault_path: str):
        self.vault_path = Path(vault_path)

        if not self.vault_path.exists():
            raise ValueError(f"Vault não encontrado: {self.vault_path}")

        logger.info(f"ObsidianWriter inicializado. Vault: {self.vault_path}")


    def _build_path(self, space_name: str, folder_name: str, task_name: str) -> Path:
         space_name = re.sub(r'[<>:"/\\|?*]', '', space_name)
         folder_name = re.sub(r'[<>:"/\\|?*]', '', folder_name)
         task_name = re.sub(r'[<>:"/\\|?*]', '', task_name)

         pasta = self.vault_path / "ClickUp" / space_name / folder_name
         pasta.mkdir(parents=True, exist_ok=True) 
         return pasta / f"{task_name}.md"


    def write(self, space_name: str, folder_name: str, task_name: str, content: str) -> Path:

        file_path = self._build_path(space_name, folder_name, task_name)
        file_path.write_text(content, encoding="utf-8")

        logger.info(f"{file_path} Salvo com sucesso! ")

        return file_path
        
      
if __name__ == "__main__":
     writer = ObsidianWriter(Config.OBSIDIAN_VAULT_PATH)

