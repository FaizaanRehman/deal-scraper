from deal import Deal

# Matches keywords agains post data to find & return deals
def find_deals(data, keywords):
    deals = []
    for item in data:
        caption = item.get("caption", "")
        url = item.get("url", "No URL provided")
        matches = [word for word in keywords if word.lower() in caption.lower()]
        # Add this post to deals if there were matches
        if matches:
            deals.append(Deal(len(matches), matches, url))
    # Deals with more keyword matches should appear first
    deals.sort(key=lambda deal: deal.match_count, reverse=True)
    return deals