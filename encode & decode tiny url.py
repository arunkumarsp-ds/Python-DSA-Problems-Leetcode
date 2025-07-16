logic:
"""
1) We want to encode the longUrl to a shortUrl, and when we decode this shortUrl, we should get back the original longUrl.
   So in short, we need to map the shortUrl to longUrl and our longUrl to shortUrl.
   
2) By this, we know we can use a dictionary to do that. But what shortUrl can we create for the respective longUrl?
   It can be any consistent pattern — for simplicity, I am going to use the length of the dictionary.
   
3) Which means:
   If we are getting the 1st longUrl, we will assign the short URL as 1 When we get the 2nd one, we assign 2 as the short URL And so on...
   
4) To make it more realistic, we convert this number into a string and concatenate it with any realistic domain.
   Example: shorturl = "https://urlshortner.com/" + str(len(encodedict) + 1)
   
5) We will be using two dictionaries — one for encoding and one for decoding.
   When we encode the longUrl, at the same time we can prepare the decoding map also.
"""
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

"""
Time:
     O(1) for searching in dictionary (both encode and decode)

Space:
     1) encodedict[longUrl] = shortUrl

        * Stores the full longUrl as the key → O(n) space per key
        * Stores the short URL as value → say it's O(1) or a small constant (like "http://urlshortner.com/123")

     2) decodedict[shortUrl] = longUrl

        * Stores the short URL (key) → O(1)
        * Stores the full longUrl (value) → O(n)

So, Space = O(n) Where n is the number of unique URLs we are encoding.
