from bs4 import BeautifulSoup
import requests
url_address = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation='

html_text = requests.get(url_address).text
# print(html_text)

soup = BeautifulSoup(html_text, 'lxml')

# jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
job = soup.find('li', class_='clearfix job-bx wht-shd-bx')

# print(jobs)
company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')

skill_rec = job.find('span', class_='srp-skills').text.replace(' ','')
published_date = job.find('span', class_='sim-posted').text

# print(skill_rec)
# print(company_name.replace(' ', ''))
# print(job.h3.text.replace(' ', ''))

print(f''''

Company Name: {company_name}
Required Skills: {skill_rec}
Published Date: {published_date}
''')