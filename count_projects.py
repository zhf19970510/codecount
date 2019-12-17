import requests
from bs4 import BeautifulSoup
from lxml import etree


def count_project():
    session = requests.session()
    login_url = 'https://git.jczh56.com/users/sign_in'

    login_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/78.0.3904.108 Safari/537.36'
    }
    data1 = session.get(login_url, headers=login_headers)
    html1 = etree.HTML(data1.text)
    authenticity_token = html1.xpath('//div/form/input[2]/@value')
    login_data = {
        'user[login]': '18516239479@163.com',
        'user[password]': 'zc123456',
        'authenticity_token': authenticity_token
    }
    now_data = session.post(login_url, data=login_data, headers=login_headers)
    soup = BeautifulSoup(now_data.text, 'lxml')
    page_href = soup.select('a.page-link')
    page_set = set()
    for i in range(len(page_href)):
        if str(page_href[i]['href']) != '#':
            page_set.add(str(page_href[i]['href']))
    for page_url in page_set:
        now_url = 'https://git.jczh56.com/' + page_url
        page_data = session.get(now_url).text
        page_soup = BeautifulSoup(page_data, 'lxml')
        one_href = page_soup.select('a.text-plain')
        url_set = set()
        for i in range(len(one_href)):
            url_set.add(str(one_href[i]['href']))
        for one_url in url_set:
            my_url = 'https://git.jczh56.com/' + one_url
            my_data = session.get(my_url).text
            my_soup = BeautifulSoup(my_data, 'lxml')
            result_project_name = str(my_soup.select_one('div.sidebar-context-title').text).strip('\n')
            result_url = my_soup.find('input', id='project_clone')["value"]
            print({result_project_name: result_url})


count_project()
