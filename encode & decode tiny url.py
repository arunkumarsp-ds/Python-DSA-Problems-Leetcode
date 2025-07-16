class Codec:
    def __init__(self):
        self.encodedict = {}
        self.decodedict = {}
        self.baseurl = "https://shorturl.com/" # this is optional just to mimic the real practices

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl not in self.encodedict:
            shorturl = self.baseurl + str(len(self.encodedict) +1)
            self.encodedict[longUrl] = shorturl
            self.decodedict[shorturl] = longUrl
        return self.encodedict[longUrl]
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.decodedict[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))