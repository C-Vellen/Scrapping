# enregistrement des résultats dans un json
import json

def export(filename, year_count, top_years, url_list):
    data = {
        "year_count":year_count,
        "top_frequent_years":top_years,
        "urls":url_list      
    }
    
    
    with open(filename, "w", encoding="utf-8") as f:
	    json.dump(data, f, indent=4, ensure_ascii=False)
    