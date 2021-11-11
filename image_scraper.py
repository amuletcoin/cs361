import requests
import json
from bs4 import BeautifulSoup


def getdata(url):
    r = requests.get(url)
    return r.text


def find_images(url):
    htmldata = getdata(url)
    soup = BeautifulSoup(htmldata, 'html.parser')
    images = {}
    index = 0

    for image in soup.find_all('img'):
        if image.has_attr('src'):
            if image['src'].startswith("http"):
                key = "image" + str(index)
                images[key] = image['src']
                index += 1

    return json.dumps(images)


def main():
    print(find_images("https://bowwowinsurance.com.au/dogs/dogs-breeds/"))


if __name__ == "__main__":
    main()

