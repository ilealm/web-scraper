import requests
from bs4 import BeautifulSoup

# send a request to the URL
# URL = 'https://en.wikipedia.org/wiki/History_of_Mexico'
# response = requests.get(URL)

# print(response)
# Extract the content
# content = response.content

# # convert ro BS object
# soup = BeautifulSoup(content,'html.parser')
# print(soup)

# Find the main element
# results = soup.find(id='mw-content-text')

# find all the citation
# citations = results.find_all('sup', class_='noprint Inline-Template Template-Fact')

# <sup class="noprint Inline-Template Template-Fact" style="white-space:nowrap;">[<i><a href="/wiki/Wikipedia:Citation_needed" title="Wikipedia:Citation needed"><span title="This claim needs references to reliable sources. (August 2010)">citation needed</span></a></i>]</sup>
# # Obtainn the number of citations
# num_citations = len(citations)
# print(num_citations)

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



if __name__ == "__main__":
    URL = 'https://en.wikipedia.org/wiki/History_of_Mexico' 
    print(get_citations_needed_count(URL))
