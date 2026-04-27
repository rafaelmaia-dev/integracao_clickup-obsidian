def transform(conteudo):
    conteudo = conteudo.replace("#", "##")
    return conteudo
  
with open("doc_clickup.md", "r", encoding = 'utf-8') as f:
        conteudo = f.read
        
        conteudo_transformado = transform(conteudo)
        
with open ("doc_obsidian.md", "w", encoding = 'utf-8') as f:
        f.write(conteudo_transformado)