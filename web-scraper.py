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
    num_citations = len(citations)

    return f'The number of citations in this URL are: {str(num_citations)}.'


def get_citations_needed_report(URL):
    passages = ''
    response = requests.get(URL)

    content = response.content
    soup = BeautifulSoup(content,'html.parser')    
    main_elements = soup.find(id='mw-content-text')
    all_paragraphs = main_elements.find_all('p')
    
    
    # print(all_paragraphs[0:1])
    paragraph = str(all_paragraphs[0])
    print('***********')
    print (paragraph)
    print('***********')
    # paragraph = all_paragraphs[1]
    # print('***********')
    # print (paragraph)
    # print('***********')
#     txt = "The rain in Spain stays mainly in the plain"
# x = "ain" in txt
# print(x)
    if 'iris' in paragraph:
        print('yeap')
    else:
        print('nop')

    # print(len(all_paragraphs))
    # for parag


    return passages



if __name__ == "__main__":
    URL = 'https://en.wikipedia.org/wiki/History_of_Mexico' 
    # print(get_citations_needed_count(URL))
    print(get_citations_needed_report(URL))
