# Keywords to search for that could imply a special/deal
KEYWORDS = [
    "deal", "%", "discount", "special", "offer", "promotion", "sale",
    "limited time", "exclusive", "coupon", "voucher", "save", "BOGO",
    "free", "half price", "50%", "anniversary", "grand opening"
]

# Regex patterns that could match a date range
# ordered by precedence
DATE_PATTERNS = [
    r'from (.*?) to (.*?)',
    r'between (.*?) and (.*?)',
    r'(\w+ \d{1,2})(?:st|nd|rd|th)? to (\w+ \d{1,2})',
    r'until (.*?)',
    r'till (.*?)',
    r'through (.*?)',
    r'on (\w+ \d{1,2})',
    r'(\w+ \d{1,2})(?:st|nd|rd|th)?',
    r'(\w+day)',
]