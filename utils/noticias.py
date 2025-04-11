import requests

def obtener_estudios_nutricion():
    url = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
    params = {
        "query": "nutrition AND open_access:y",
        "format": "json",
        "pageSize": 10
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()
        articulos = data.get("resultList", {}).get("result", [])

        estudios = []
        for art in articulos:
            full_text_links = art.get("fullTextUrlList", {}).get("fullTextUrl", [])
            url = ""
            for link in full_text_links:
                if link.get("availability") == "Open access":
                    url = link.get("url", "")
                    break
            if not url:
                url = f"https://europepmc.org/article/MED/{art.get('pmid', '')}"

            estudios.append({
                "titulo": art.get("title", "Sin título"),
                "resumen": art.get("abstractText", "Sin resumen disponible."),
                "autores": art.get("authorString", "Autores desconocidos"),
                "fecha": art.get("firstPublicationDate", "Sin fecha"),
                "url": url
            })
        return estudios

    except Exception as e:
        print(f"Error al obtener estudios: {e}")
        return []