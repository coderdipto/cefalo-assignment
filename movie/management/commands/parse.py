import json
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from movie.models import Movie

start_url = "https://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films"


def soup_sanitizing(soup):
    """
    Text formatting and sanitizing
    """
    for sup in soup.findAll('sup'):
        sup.decompose()

    return soup


def get_soup(url):
    """
    Parses URL and fetches movie wiki link
    url(string): URL to parse
    return BeautifulSoup soup
    """

    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        r = requests.get(url, headers=headers, timeout=5)

        if r.status_code != 200:
            raise Exception('Unreachable URL')

        return BeautifulSoup(r.content, 'html.parser')
    except Exception:
        return None


def get_movie_detail(url):
    """
    Parses URL and fetches movie info
    url(string): URL to parse
    return Dict

    """
    soup = get_soup(url)
    data = {}

    if not soup:
        return data

    infobox = soup.find('table', class_='infobox')

    if not infobox:
        return data

    for tr in soup.find('table', class_='infobox').findAll('tr'):
        th = tr.find('th')
        td = tr.find('td')

        if th and td:
            td = soup_sanitizing(td)
            info = td.text.strip()
            info = info.strip('\n')
            data[th.text] = info

    return data


# Get start_url html content as soup
soup = get_soup(start_url)
movie_data = {}

if soup:
    # For each movie info row, fetch data
    for tr in soup.find('table', class_='wikitable').find_all('tr'):
        try:
            link = urljoin(start_url, tr.find_all('td')[0].find('a').get('href'))
            title = tr.find_all('td')[0].text.strip()
            year = tr.find_all('td')[1].text.strip()
            awards = soup_sanitizing(tr.find_all('td')[2]).text.strip()
            nominations = soup_sanitizing(tr.find_all('td')[3]).text.strip()

            # Fetch movie detail data from respective movie link
            detail = get_movie_detail(link)

            movie = Movie.objects.create(
                title=title,
                year=year,
                awards=awards,
                nominations=nominations,
                info=json.dumps(detail)
            )

            print("Stored data for Movie: %s" % movie)
        except Exception:
            pass

