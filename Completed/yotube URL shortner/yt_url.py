import re
import sys


def main():
    print(parse(input("HTML: ")))

def parse(s):
    if re.search(r'<iframe(.)*><\/iframe>',s): # search from the iframe
        if url := re.search(r'(http(s)*:\/\/(www\.)*(?P<site>youtube)\.com\/embed\/)(?P<site_id>[\w]+)',s):
            site = [letter for letter in url.group('site')]
            site.insert(-2,'.')
            site = ''.join(site)
            return f"https://{site}/{url.group('site_id')}"

if __name__ == "__main__":
    main()
