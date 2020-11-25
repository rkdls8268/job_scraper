import requests
from bs4 import BeautifulSoup

URL1 = "http://www.saramin.co.kr/zf_user/jobs/list/job-category?"
URL2 = "cat_key=40430%2C40404%2C40426%2C40427&loc_mcd=101000&loc_cd=102190&panel_type=&search_optional_item=n&search_done=y&panel_count=y"

def extract_saramin_pages():
    saramin_res = requests.get(URL1+URL2)
    # print(saramin_res.text)

    # html parser를 이용해서 html 코드를 Navigate할 것 
    saramin_soup = BeautifulSoup(saramin_res.text, "html.parser")

    # pagination className을 가진 div 태그 추출
    pagination = saramin_soup.find("div", {"class":"pagination"})
    # print(pagination)

    # a 태그를 가진 모든 내용 출력
    links = pagination.find_all('a')
    # print(pages)

    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))

    max_page = pages[-1]
    return max_page

def extract_saramin_jobs(last_page):
    for page in range(last_page):
        result = requests.get(f"{URL1}page={page+1}&{URL2}")
        print(result.status_code)
