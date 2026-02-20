import os, re
from logger import create_logger
from fetcher import fetch
from parser import year_parser, url_parser
from exporter import export






# url
url = "https://fr.wikipedia.org/wiki/Intelligence_artificielle"


# chemin absolu du projet
os.environ["SCRAPATH"] = os.path.dirname(__file__)

# logger
logger_main = create_logger()
logger_main.info(f"Chemin projet: {os.environ.get("SCRAPATH")}")
logger_main.info(f"URL demandée: {url}")

# fetch
response = fetch(url)
if response["ok"]:
    message = f"status: {response["status"]} | size: {response["size"]}"
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
prefix = re.split(r'(?<!/)/(?!/)', url)[0]		# prefix de l'url pour rendre les urls absolues
url_list = url_parser(response["body"], prefix)
logger_main.info("Liste des url utilisées:\n\t\t" + "\n\t\t".join(url_list))


# sauvegarde json:
export_file = os.path.join(os.environ.get("SCRAPATH"), "export.json")
export(export_file, url, year_count, top_years, url_list)
