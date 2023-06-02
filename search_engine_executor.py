import requests
import bs4


class SearchEngineExecutor:
    def __init__(self):
        self.__wiki_search_url = None
        self.__search_results = {}

    def document_search(self, search_index):
        print("===================")
        print(search_index)
        self.__wiki_search_url = f'https://en.wikipedia.org/wiki/{search_index}'
        request_result = requests.get(self.__wiki_search_url)

        soup = bs4.BeautifulSoup(request_result.text,
                                 "html.parser")

        doc_title = self.__get_document_title(soup)
        self.__search_results["title"] = doc_title

        doc_paragraph = self.__get_two_paragraph(soup)
        self.__search_results["paragraph1"] = doc_paragraph[0]
        self.__search_results["paragraph2"] = doc_paragraph[1]

        return self.__search_results

    def __get_document_title(self, soup):
        return soup.find('h1').text

    def __get_two_paragraph(self, soup):
        if len(soup.findAll('p')) < 2:
            return ['', 'Error: Nothing found!']

        return soup.findAll('p')[0].text, soup.findAll('p')[1].text
