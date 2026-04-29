from src.clickup.client import ClickUpClient
from src.converts.markdown_converter import MarkdownConverter
from src.obsidian.writer import ObsidianWriter
from src.config import Config
from src.utils.logger import logger

def main():
    
    logger.info("Iniciando a integração do ClickUp com o Obsidian... ")

    clickup = ClickUpClient(Config.CLICKUP_API_KEY)
    logger.info("Conectado ao ClickUp ")

    obsidian = ObsidianWriter(Config.OBSIDIAN_VAULT_PATH)
    logger.info("Conectado ao Obsidian ")

    teams = clickup.get_teams()

    for team in teams:
        logger.info(f"Processando team: {team['name']} ")

        spaces = clickup.get_space(team['id'])

        for space in spaces:
            logger.info(f"Space: {space['name']} ")

            folders = clickup.get_folders(space['id'])

            for folder in folders:
                logger.info(f"Folders: {folder['name']}")

                lists = clickup.get_lists(folder['id'])

                for list_data in lists:
                    tasks = clickup.get_tasks(list_data['id'])

                    for task in tasks:
                        markdown = MarkdownConverter.convert_task_markdown(task)

                        filename = f"{task['id']}--{task['name']}.md"

                        obsidian.write_document(
                            folders=f"{'name'}/{folder['name']}",
                            filename=filename,
                            content=markdown

                        )

                        logger.info(f"{filename} criado! ")
logger.info("Integração feita com sucesso! ")


if __name__ == "__main__":
    main()