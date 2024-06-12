import string


class URLShortener:
    def __init__(self):

        self.map = {}
        self.count = 1

        self.chars = string.ascii_letters + string.digits
        self.base = len(self.chars)

    def encode(self, num):
        encoded = []
        while num > 0:
            num, rem = divmod(num, self.base)
            encoded.append(self.chars[rem])
        return "".join(reversed(encoded))

    def shorten(self, long_url):
        short_code = self.encode(self.count)
        self.map[short_code] = long_url
        self.count += 1
        return short_code

    def retrieve(self, short_code):
        return self.map.get(short_code)


if __name__ == "__main__":
    shortener = URLShortener()

    long_url = "https://www.example.com/some/long/url"
    short_code = shortener.shorten(long_url)
    print(f"Original URL: {long_url}")
    print(f"Short Code: {short_code}")

    original_url = shortener.retrieve(short_code)
    print(f"Retrieved URL: {original_url}")
