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


    def _build_path(self, space_name: str, folder_name: str, task_name: str) -> Path
        # if folder_name.exists()
            pasta.mkdir(parents=True, exist_ok=True)
        # else:

       
if __name__ == "__main__":
     writer = ObsidianWriter(Config.OBSIDIAN_VAULT_PATH)

