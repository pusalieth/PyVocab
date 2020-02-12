import requests
import re

class GOOGLE_API:
    def __init__(self):
        self.url = 'https://www.google.com/search?q=define+'

    def define(self, word):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        }

        search_url = self.url + str(word)
        response = requests.get(search_url, headers=headers)
        try:
            first_def = re.search("<span>1</span>", str(response.text)).end()
            end_of_first_span = response.text[first_def:]
            definition_span = re.search("<span>*[a-zA-Z., ]*</span>", end_of_first_span).span()
            definition = end_of_first_span[definition_span[0] + len('<span>'):definition_span[1] -  + len('</span>')]
            return definition
        except:
            return 'No definition returned for %s' % word

if __name__ == "__main__":
    lookup = GOOGLE_API()
    lookup.define('apple')