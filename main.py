from src.utils.logger import logger
from src.config import validate_config, Config
from src.obsidian.writer import ObsidianWriter
from src.clickup.client import ClickUpClient
from src.converters.markdown_converter import MarkdownConverter

def sync():
    logger.info("=== Sync iniciada ===")
   
    client = ClickUpClient(Config.CLICKUP_API_TOKEN)
    convert = MarkdownConverter()
    writer = ObsidianWriter(Config.OBSIDIAN_VAULT_PATH)

    teams = client.get_teams()["teams"]
       
    for team in teams:
        spaces = client.get_spaces(team["id"])["spaces"]
        for space in spaces:
            folders = client.get_folders(space["id"])["folders"]
            for folder in folders:
                lists = client.get_lists(folder["id"])["lists"]
                for list_int in lists:
                    tasks = client.get_tasks(list_int["id"])["tasks"]
                    for task in tasks:
                        try:
                            content = convert.convert(task)
                            writer.write(space_name=space["name"], folder_name=folder["name"], task_name=task["name"], content=content)
                        except Exception as e:
                            logger.error(f"Falha ao processar task '{task.get('name')}': {e}")
                            continue

    logger.info("=== Sync concluída ===")
  
if __name__ == "__main__":
    validate_config()
    try:
        sync()
    except Exception as e:
        logger.error(f"Sync falhou: {e}")









    