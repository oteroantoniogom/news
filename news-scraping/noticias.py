import newspaper
import pandas as pd
from fake_useragent import UserAgent

user_agent = UserAgent()

newspapers = ["https://es.cointelegraph.com/", "https://www.elmundo.es/", "https://www.larazon.es/"]

# Recorrer cada periódico en la lista de periódicos
for title in newspapers:
    lista = []
    paper = newspaper.build(title, memoize_articles=False, request_kwargs={'headers': {'User-Agent': user_agent.random}})
    # Recorrer cada artículo en el periódico
    for article in paper.articles:
        try:
            # Descargar y analizar el artículo
            article.download()
            article.parse()
            # Agregar la URL y el contenido del artículo al dataframeim
            data = [article.url, article.text]
            lista.append(data)
        except Exception as ex:
            # Se produce un error al descargar o analizar el artículo
            print(f"Error al descargar o analizar el artículo {article.url}: {str(ex)}")
    dominio = title.split(".")[1]
    print(dominio)
    print(title)
    df = pd.DataFrame(lista, columns=["URL", "CONTENIDO"])
    df.to_excel(f"{dominio}.xlsx", index=False, encoding="utf-8")