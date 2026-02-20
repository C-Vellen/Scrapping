import os, logging


def create_logger():
    '''
    Créé un logger pour enregistrer les messages et les sorties dans le journal.log
    '''
    
    logging.basicConfig(
    	level=logging.DEBUG, # Niveau minimum affiché (défaut : info)
    	format="%(asctime)s - %(levelname)s - %(message)s",  # Format des messages
    	filename=os.path.join(os.environ.get("SCRAPATH"), "journal.log"), # Sortie dans un fichier (défaut : sur la console)
    	filemode="w" 
    )
    logger = logging.getLogger("main")
    logger.setLevel(logging.INFO)
    console_handler = logging.StreamHandler()
    logger.addHandler(console_handler)
    
    return logger

    