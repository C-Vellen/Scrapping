# récupération d'une page internet

import requests


def fetch(url: str):
    """ récuple body de l apage web """

    headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36",
        }
    response = requests.get(url, headers= headers)
    return {"ok": response.ok, "status": response.status_code, "size": len(response.text), "body":response.text}


    
    
    
    