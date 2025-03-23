# Represents an individual deal record
class Deal:
    def __init__(self, match_count, matches, url):
        self.match_count = match_count
        self.matches = matches
        self.url = url

    def __repr__(self):
        return f"Deal(match_count={self.match_count}, matches={self.matches}, url='{self.url}')"