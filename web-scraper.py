import requests
from bs4 import BeautifulSoup


def get_citations_needed_count(URL):
    num_citations = 0
    response = requests.get(URL)

    # Extract the content
    content = response.content
    # convert ro BS object
    soup = BeautifulSoup(content,'html.parser')    
    # Find the main element
    main_elements = soup.find(id='mw-content-text')
    # find all the citation
    citations = main_elements.find_all('sup', class_='noprint Inline-Template Template-Fact')
    # Obtainn the number of citations
    num_citations = len(citations)-1

    return f'The number of citations in this URL are: {str(num_citations)}.'


def get_citations_needed_report(URL):
    return_passages = ''
    response = requests.get(URL)

    content = response.content
    soup = BeautifulSoup(content,'html.parser')    
    main_elements = soup.find(id='mw-content-text')
    all_paragraphs = main_elements.find_all('p')

    ind = 0
    for paragraph in all_paragraphs:
        if 'citation needed' in str(paragraph.text):
            return_passages += str(paragraph.text) + "\n\n"
            ind = ind + 1
     
     
    return return_passages



if __name__ == "__main__":
    URL = 'https://en.wikipedia.org/wiki/History_of_Mexico' 
    print(get_citations_needed_count(URL))
    print(get_citations_needed_report(URL))
