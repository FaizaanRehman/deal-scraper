from parser import find_deals
from scraper import load_data_from_apify
from constants import KEYWORDS

def main():
    data = load_data_from_apify()
    deals = find_deals(data, KEYWORDS)
    for deal in deals:
        print(f"{deal.match_count} matches in {deal.url} with {deal.matches}")


if __name__ == "__main__":
    main()

    