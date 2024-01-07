from bs4 import BeautifulSoup
import requests
url_address = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation='

html_text = requests.get(url_address).text
# print(html_text)

soup = BeautifulSoup(html_text, 'lxml')

# jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
job = soup.find('li', class_='clearfix job-bx wht-shd-bx')

# print(jobs)
print(job)