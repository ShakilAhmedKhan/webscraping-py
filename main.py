from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    #print(soup.prettify())
    tags = soup.find('h5') #chooses the first element only
    # courses_html_tags = soup.find_all('h5') #chooses all element
    # for course in courses_html_tags:
    #     print(course.text)

    course_cards = soup.find_all('div', class_='card')
    for course in course_cards:
     print(course.h5.text)
     print(course.a.text)
