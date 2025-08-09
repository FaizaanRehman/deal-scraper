from apify_client import ApifyClient
from config import APIFY_KEY

def load_data_from_apify():
    # Initialize ApifyClient
    apify_client = ApifyClient(APIFY_KEY)

    # Get dataset
    dataset = apify_client.dataset('PLVAebVRSH2leQzWe')

    # Get data from dataset
    dataset_items = dataset.list_items()

    return dataset_items.items