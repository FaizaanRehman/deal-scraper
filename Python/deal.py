# Represents an individual deal record
class Deal:
    def __init__(self, match_count, matches, url, date_range=None):
        self.match_count = match_count
        self.matches = matches
        self.url = url
        self.date_range = date_range

    def __repr__(self):
        return (f"Deal(match_count={self.match_count}, "
                f"matches={self.matches}, "
                f"url='{self.url}', "
                f"dates={self.date_range})")
    
    def get_date_string(self):
        if not self.date_range:
            return None
        start = self.date_range.get("start")
        end = self.date_range.get("end")
        if start:
            start = start.strftime("%b %d")
        if end:
            end = end.strftime("%b %d")
        
        if start and end:
            return f"{start} - {end}"
        elif end:
            return end
        else:
            return None