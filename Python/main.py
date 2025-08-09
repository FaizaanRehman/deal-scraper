from parser import find_deals
from scraper import load_data
import os

def main():
    # Get the instagram post data in JSON format, obtained through Apify
    file_path = os.path.join("..", "Datasets", "InstagramPosts.json")

    data = load_data(file_path)
    deals = find_deals(data)
    for deal in deals:
        print(f"{deal.match_count} matches in {deal.url} with {deal.matches}")
        if deal.date_range:
            print(f"Dates: {deal.get_date_string()}")


if __name__ == "__main__":
    main()

    