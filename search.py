from googlesearch import search
import logging
logger = logging.getLogger()

# Google search response

def google_search(query,user_id):
    top_five_links = []
    try:
        for links in search(query, num=5, stop=5, pause=2):
            top_five_links.append(links)
        print(top_five_links)
    except:
        logger.info("Error while fetching data from google")
    return top_five_links
