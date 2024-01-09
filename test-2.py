from bs4 import BeautifulSoup
import requests
url_address = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation='

html_text = requests.get(url_address).text
# print(html_text)

soup = BeautifulSoup(html_text, 'lxml')

jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
# job = soup.find('li', class_='clearfix job-bx wht-shd-bx')

# print(jobs)
for job in jobs:
    published_date = job.find('span', class_='sim-posted').text
    if 'few' in published_date:

        company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')

        skill_rec = job.find('span', class_='srp-skills').text.replace(' ','')
        more_info = job.header.h2.a['href']

        # print(skill_rec)
        # print(company_name.replace(' ', ''))
        # print(job.h3.text.replace(' ', ''))

        print(f'Company Name: {company_name.strip()}')
        print(f'Required Skills: {skill_rec.strip()}')
        # print(f'Date: {published_date}')
        print(f'More info: {more_info}')

        print(" ")