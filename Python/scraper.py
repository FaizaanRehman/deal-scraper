import json
import os

# Represents an individual deal record
class Deal:
    def __init__(self, match_count, matches, url):
        self.match_count = match_count
        self.matches = matches
        self.url = url

    def __repr__(self):
        return f"Deal(match_count={self.match_count}, matches={self.matches}, url='{self.url}')"

# Obtaining data in JSON format
def load_data(filepath):
    try:
        with open(filepath, encoding="utf8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading JSON data: {e}")
        exit(1)

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
    deals.sort(key=lambda deal: deal.match_count, reverse=True)
    return deals

# Get the instagram post data in JSON format, obtained through Apify
file_path = os.path.join("..", "Datasets", "InstagramPosts.json")

# Keywords to search for that could imply a special/deal
keywords = [
    "deal", "%", "discount", "special", "offer", "promotion", "sale",
    "limited time", "exclusive", "coupon", "voucher", "save", "BOGO",
    "free", "half price", "50%", "anniversary", "grand opening"
]

data = load_data(file_path)
deals = find_deals(data, keywords)
for deal in deals:
    print(f"{deal.match_count} matches in {deal.url} with {deal.matches}")
