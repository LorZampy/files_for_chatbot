# Importa il modulo UnstructuredURLLoader dalla libreria langchain.document_loaders
from langchain.document_loaders import UnstructuredURLLoader

# Definisci una lista di URL da cui scaricare contenuto
urls = [
    "https://www.boxofficemojo.com/weekly/by-year/2019/"
    "https://www.boxofficemojo.com/year/2019/"
    "https://screenrant.com/most-anticipated-movies-2019/"
]

# Crea un oggetto 'loader' di tipo UnstructuredURLLoader, specificando gli URL da caricare
loader = UnstructuredURLLoader(urls=urls)

# Carica il contenuto dalle URL specificate
documents = loader.load()

# Loop attraverso ciascun documento ottenuto dalle URL
for doc in documents:
    # Estrai il contenuto della pagina
    page_content = doc.page_content

    # Ottieni la fonte del documento dalla metadati
    source = doc.metadata["source"]

    # Estrai le prime 100 parole dal contenuto della pagina
    first_words = " ".join(page_content.split()[:100])

    # Stampa le prime 100 parole della pagina insieme alla sua fonte
    print(f"Prime 100 parole della pagina {source}:\n{first_words}")
    print("\n\n")