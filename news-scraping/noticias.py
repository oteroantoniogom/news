import newspaper
import pandas as pd
from fake_useragent import UserAgent

user_agent = UserAgent()

newspapers = ["https://es.cointelegraph.com/", "https://www.elmundo.es/", "https://www.larazon.es/"]

# Definir dataframe vacío
#df = pd.DataFrame(columns=["URL", "CONTENIDO"])

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
            #df = df.append({"URL":article.url, "CONTENIDO":article.text}, ignore_index=True)
            #df = df.append([article.url, article.text], ignore_index=True)
            lista.append(data)
        except Exception as ex:
            # Se produce un error
            print(f"Error al descargar o analizar el artículo {article.url}: {str(ex)}")
    dominio = title.split(".")[1]
    print(dominio)
    print(title)
    df = pd.DataFrame(lista, columns=["URL", "CONTENIDO"])
    df.to_excel(f"{dominio}.xlsx", index=False, encoding="utf-8")

df.to_csv("noticias.csv", index=False, encoding="utf-8")
