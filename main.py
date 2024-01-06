from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    #print(soup.prettify())
    tags = soup.find('h5') #chooses the first element only
    tags = soup.find_all('h5') #chooses all element
    print(tags)