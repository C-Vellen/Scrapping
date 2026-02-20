from fetcher import fetch
from parser import year_parser, url_parser
from exporter import export
import logging




# preparation logs
logging.basicConfig(
	level=logging.DEBUG, # Niveau minimum affiché (défaut : info)
	format="%(asctime)s - %(levelname)s - %(message)s",  # Format des messages
	filename="app.log", # Sortie dans un fichier (défaut : sur la console)
	filemode="w" # Écriture (remplace le fichier existant) ou "a" pour ajouter
)
logger_main = logging.getLogger("main")
logger_main.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
logger_main.addHandler(console_handler)

# url
url = "https://fr.wikipedia.org/wiki/Intelligence_artificielle"
prefix = "https://fr.wikipedia.org"

# fetch
response = fetch(url)
if response["ok"]:
    message = f"status: {response["status"]} | size: {response["size"]} | body: {response["body"][:15]}"
    logger_main.info(message)
else:
    logger_main.warning(f"site non trouvé --> error {response["status"]}")
    

# parse years    
n = 5 # pour le calcul du top n des années les plus fréquentes
year_count, top_years = year_parser(response["body"], n) 

year_display = [f"\t\tannée {y}: {c:>3} occurence{'s'*(c>1)}" for y,c in year_count.items()]
logger_main.info("Occurences de chaque année:\n" + "\n".join(year_display))

# top_years = top_frequent_years(year_count, n)
top_year_display = [f"\t\tannée {y}: {c:>3} occurence{'s'*(c>1)}" for y,c in top_years]
logger_main.info(f"{n} années les plus fréquentes:\n" + "\n".join(top_year_display))


# parse urls

url_list = url_parser(response["body"], prefix)
logger_main.info("Liste des url utilisées:\n\t\t" + "\n\t\t".join(url_list))


# sauvegarde json:
export("scrap.json", year_count, top_years, url_list)
