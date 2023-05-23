import requests
import bs4

text = "Web scraping"

google_search_url = f'https://en.wikipedia.org/wiki/{text}'


def hyperlinks_search(search_index):
    request_result = requests.get(google_search_url)

    soup = bs4.BeautifulSoup(request_result.text,
                             "html.parser")

    find_all_hyperlinks = soup.find('h1')
    print(find_all_hyperlinks.text)
    """
    hyperlinks = []
    for links in find_all_hyperlinks:
        hyperlinks.append(links.get('href'))
        print(hyperlinks)

    return hyperlinks
"""

def optimzed_hyperlinks_search(search_index):
    request_result = requests.get(google_search_url)

    soup = bs4.BeautifulSoup(request_result.text,
                             "html.parser")

    find_all_hyperlinks = soup.find_all('a')

    hyperlinks = []
    for link in find_all_hyperlinks:
        hyperlinks.append(link)
        print(hyperlinks)

    return hyperlinks


hyperlinks_search(text)

