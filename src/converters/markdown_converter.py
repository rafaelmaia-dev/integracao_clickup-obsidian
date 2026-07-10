import datetime 
import html2text
from src.utils.logger import logger

class MarkdownConverter:

    def __init__(self):
        self.converter = html2text.HTML2Text()
        self.converter.ignore_links = False
        self.converter.body_width = 0


    def _build_frontmatter(self, task: dict) -> str:
        task_id = task.get("id", "")
        status = task.get("status", {}).get("status", "")
        priority = task.get("priority", {}).get("priority", "sem prioridade")
        url = task.get("url", "")
        ts = int(task.get("date_created", 0))
        dt_cr = datetime.datetime.fromtimestamp(ts / 1000).strftime("%Y-%m-%d")

        return f"""---
task_id: {task_id}
status: {status}
priority: {priority}
url: {url}
dt_cr: {dt_cr}
---"""

    def _build_body(self, task: dict) -> str:

        name = task.get("name")

        descricao_html = task.get("description") or ""

        if descricao_html:
            descricao_md = self.converter.handle(descricao_html)
        else:
            descricao_md = ""
        return f"# {name}\n\n{descricao_md}"



    def convert(self, task: dict) -> str:
        try:
            resultado1 = self._build_frontmatter(task)
            resultado2 = self._build_body(task)
            logger.info(f"Task: '{task.get('name')}' convertida com sucesso. ")
            return f"{resultado1}\n\n{resultado2}"
        except Exception as e:
            logger.error(f"Erro ao converter task '{task.get('name')}': {e}")
            raise


        

       


