import newspaper
import pandas as pd
from fake_useragent import UserAgent

user_agent = UserAgent()

# Incluir aquí los portales de noticias a analizar. Tener en cuenta que siempre debe haber al menos un "." antes de la web. [www.elmundo.es] --> correcto | [as.com] --> incorrecto
newspapers = ["https://es.cointelegraph.com/", "https://www.elmundo.es/", "https://www.larazon.es/"]

# Recorrer cada periódico en la lista de periódicos
for title in newspapers:
    lista = []
    # Construir un objeto de periódico utilizando el título y especificando no memorizar los artículos, además de especificar el agente de usuario
    paper = newspaper.build(title, memoize_articles=False, request_kwargs={'headers': {'User-Agent': user_agent.random}})
    # Recorrer cada artículo en el periódico
    for article in paper.articles:
        try:
            # Descargar y analizar el artículo
            article.download()
            article.parse()
            # Agregar la URL y el contenido del artículo a una lista
            data = [article.url, article.text]
            lista.append(data)
        except Exception as ex:
            # Se produce un error al descargar o analizar el artículo
            print(f"Error al descargar o analizar el artículo {article.url}: {str(ex)}")
    # Extraer el dominio del título del periódico
    dominio = title.split(".")[1]
    print(dominio)
    print(title)
    # Crear un dataframe de pandas utilizando la lista de datos y especificando el nombre de las columnas
    df = pd.DataFrame(lista, columns=["URL", "CONTENIDO"])
    # Guardar el dataframe como un archivo de Excel en la raíz del proyecto con el nombre del dominio del periódico
    df.to_excel(f"{dominio}.xlsx", index=False, encoding="utf-8")
    print(f"{article.url} analizado.")
