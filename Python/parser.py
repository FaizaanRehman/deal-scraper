from deal import Deal
from constants import KEYWORDS, DATE_PATTERNS
import re
import dateparser

# Matches keywords agains post data to find & return deals
def find_deals(data):
    deals = []
    for item in data:
        caption = item.get("caption", "")
        url = item.get("url", "No URL provided")
        matches = [word for word in KEYWORDS if word.lower() in caption.lower()]
        # Add this post to deals if there were matches
        if matches:
            date_range = extract_dates(caption)
            deals.append(Deal(len(matches), matches, url, date_range))
    # Deals with more keyword matches should appear first
    deals.sort(key=lambda deal: deal.match_count, reverse=True)
    return deals

def extract_dates(text):
    for pattern in DATE_PATTERNS:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            groups = match.groups() # returns all captured groups from the match
            dates = [dateparser.parse(group.strip()) for group in groups if group.strip()] # strip whitespace, convert to datetime object 
            dates = [date for date in dates if date]    # remove any failed conversions, i.e. null
            if len(dates) == 1:
                # safer to assume its the end date
                return {"start":None, "end": dates[0]}
            elif len(dates) >= 2:
                # possible the start date is mentioned twice, should try to filter this case
                return {"start": dates[0], "end": dates[1]}
            
    return None