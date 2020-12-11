import requests
from bs4 import BeautifulSoup

def extract_saramin_pages(url1, url2):
    saramin_res = requests.get(url1+url2)
    # print(saramin_res.text)

    # html parser를 이용해서 html 코드를 Navigate할 것 
    saramin_soup = BeautifulSoup(saramin_res.text, "html.parser")

    # pagination className을 가진 div 태그 추출
    pagination = saramin_soup.find("div", {"class":"pagination"})
    # print(pagination)

    # a 태그를 가진 모든 내용 출력
    links = pagination.find_all('a')

    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))

    if not links:
        max_page = 1
    else:
        max_page = pages[-1]
    return max_page

def extract_job(result):
    company = result.find("div", {"class":"company_nm"}).find("a")["title"]
    title = result.find("div", {"class":"notification_info"}).find("a")["title"]
    location = result.find("div", {"class":"company_info"}).find("p", {"class":"work_place"}).string

    result.select_one(".support_info").select_one(".deadlines").span.decompose()
    deadline = result.find("div", {"class":"support_info"}).find("p", {"class":"deadlines"}).string
    company = str(company)
    title = str(title)
    # 해당 링크에 대한 고유번호. rec-로 시작해서 4부터 시작
    job_id = result["id"][4:]
    # print(job_id)
    return {'title': title, 'company': company, 'location': location, 'deadline': deadline, "link": f"http://www.saramin.co.kr/zf_user/jobs/relay/view?isMypage=no&rec_idx={job_id}&recommend_ids=eJxdkMsZwyAMg6fp3W%2FZ5w7C%2FlvU%2BQgh5fjbQpLRLIUHj6j44KuNbqojSA4cdg2KJalieC0UMh6wmOgJw0YYAy32A6dZJtodK6z3mvaWL7zlFZ7uPYgDV7dOb7s%2BZ7onomhhURtSPmFEIeC9le4mT3OylseKqtZW0L5LOEX%2FznR%2B9YZWDZAeeNek%2FtWs6%2FUPzpxT9w%3D%3D&view_type=list&gz=1&t_ref_content=general&t_ref=jobcategory_recruit#seq=0"}

def extract_saramin_jobs(last_page, url1, url2):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping page {page}")
        saramin_res = requests.get(f"{url1}page={page+1}&{url2}")
        saramin_soup = BeautifulSoup(saramin_res.text, "html.parser")
        results = saramin_soup.find_all("div", {"class":"list_item"})
        # print(results)
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs

# get_jobs는 job(word)을 입력 받아 사용.
def get_jobs(word):
    # word를 받아서 url의 인자로 보낼 수 있게 url을 get_jobs 함수 안에 넣어줌
    url1 = "http://www.saramin.co.kr/zf_user/jobs/list/job-category?"
    url2 = f"cat_key=40430%2C40404%2C40426%2C40427&loc_mcd=101000&loc_cd=102190&searchType=search&searchword={word}&panel_type=&search_optional_item=y&search_done=y&panel_count=y"

    last_page = extract_saramin_pages(url1, url2)
    jobs = extract_saramin_jobs(last_page, url1, url2)
    return jobs