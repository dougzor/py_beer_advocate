import requests
from bs4 import BeautifulSoup

beer_advocate_search_url = "http://beeradvocate.com/search"
beer_advocate_beer_page_url = "http://beeradvocate.com/beer/profile/%s/%s"
beer_advocate_brewery_page_url = "http://beeradvocate.com/beer/profile/%s"

def get_beer_list(beer_search):
    """Given a beer_search search term, get all beers from BA that potentially match that search term
    """
    payload = {'qt': 'beer', 'q': beer_search}

    r = requests.get(beer_advocate_search_url, params=payload)

    soup = BeautifulSoup(r.text)

    content_element = soup.find(id="baContent")
    try:
        results = content_element.find("ul").find_all("li")

        beer_urls = []
        for result in results:
            link = result.find("a")['href']
            parts = link.split("/")

            beer_id = None
            brewery_id = None

            if len(parts) == 6:
                beer_id = parts[4]
                brewery_id = parts[3]

            name = result.find("b").text
            brewery = result.find_all("a")[1].text

            beer_urls.append([name, brewery, beer_id, brewery_id])

        return beer_urls
    except AttributeError:
        return []


def get_brewery_info(brewery_id):
    brewery_html = requests.get(beer_advocate_brewery_page_url % brewery_id)

    #@todo: do this

    return {}

def get_beer_info(brewery_id, beer_id):
    """Given a beer url from get_beer_list() return the information for that beer
    """
    beer_html = requests.get(beer_advocate_beer_page_url % (brewery_id, beer_id))

    soup = BeautifulSoup(beer_html.text)

    brewery = soup.find("div", {"class": "titleBar"}).find("span").string[3:]

    score = soup.find("span", {"class": "BAscore_big"}).string

    picture = soup.find("img")['src']

    data = {"brewery": brewery,
            "score": score,
            "image": picture}

    return data
