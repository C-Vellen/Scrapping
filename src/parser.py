# analyse le contenu du site
import re
from collections import Counter
from functools import cmp_to_key

def year_parser(content:str, n:int):
    '''Extrait du contenu les années et leurs ocuurences sous forme {2025:3, ...}'''
    
    # recherche des années :
    year_list = re.findall(r"[1-2]\d\d\d", content)
    
    # transformation des années en entier:
    year_list = list(map(lambda x: int(x), year_list))
    
    # filtre entre 1950 et 2050 :
    year_list = list(filter(lambda x: (x>=1950 and x<=2050), year_list))
    
    # tri
    year_list.sort()
    
    # comptage des occurences des années
    year_count = Counter(year_list)
    top_years = year_count.most_common(n)
   
    return dict(year_count), top_years
    
  

def url_parser(content:str, prefix:str):
    
    # recherche des urls dans href="..."
    rough_url_list = re.findall( r"href=['\"]([^'\"]+)['\"]" , content)       # récupère que l'url dans (...)
    # url_list = re.findall( r"href=['\"][^'\"]+['\"]" , content)           # récupère tout y compris href="..."
      
    # unicité des liens
    url_list = dict(Counter(rough_url_list)).keys()
    
    
    # conversion lien relatifs en liens absolus
    def absolute_line(url):
        nonlocal prefix
        if url.find("https://") == 0:
            return url
        elif url.find("//") == 0:
            return "https:" + url
        else:
            return prefix + url
    url_list = list(filter(lambda x: x[0] != '#', url_list)) # on retire les ancres
    url_list = list(map(absolute_line, url_list))
     
    return url_list