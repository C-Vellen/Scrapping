# enregistrement des résultats dans un json
import json


def export(filename, url, year_count, top_years, url_list):
    '''
    Export des résultats : liste des années avec occurence,
    années les plus fréquentes, liste des urls,
    dans un fichier au format json
    '''
    data = {
        'url': url,
        "year_count":year_count,
        "top_frequent_years":top_years,
        "urls":url_list      
    }
    with open(filename, "w", encoding="utf-8") as f:
	    json.dump(data, f, indent=4, ensure_ascii=False)
    