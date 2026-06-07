import html2text
from src.utils.logger import logger

class MarkdownConverter:

    def __init__(self):
        self.converter = html2text.HTML2Text()
        self.converter.ignore_links = False
        self.converter.body_width = 0


    def _build_frontmatter(self, task: dict) -> str:
        id = task.get("id", "")
        status = task.get("status", {}).get("status", "")
        priority = task.get("priority", {}).get("priority", "sem prioridade")
        url = task.get("url", "")
        dt_cr = task.get("date_created", "")

        return f"""---
id: {id}
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
        resultado1 = self._build_frontmatter(task)
        resultado2 = self._build_body(task)
        logger.info(f"Task: '{task.get('name')}' convertida com sucesso. ")
        return f"{resultado1}\n\n{resultado2}"
        


        

       


