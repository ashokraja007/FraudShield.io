import logging
from datetime import datetime
import whois

logger = logging.getLogger(__name__)

def search(domain):
    domain_name = domain['name'] + '.' + domain['tld']
    creation_date = None
    try:
        w = whois.whois(domain_name)
        if w.creation_date:
            creation_date = w.creation_date
            if isinstance(creation_date, list):
                creation_date = creation_date[-1]  # Use the last creation date if there are multiple
            if isinstance(creation_date, datetime):
                return creation_date.replace(tzinfo=None)
    except Exception as e:
        logger.error("Exception occurred while fetching domain information")
        logger.error(str(e))
    return creation_date
