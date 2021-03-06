import requests
from bs4 import BeautifulSoup

URL1 = "http://www.saramin.co.kr/zf_user/jobs/list/job-category?"
URL2 = "cat_key=40430%2C40404%2C40426%2C40427&loc_mcd=101000&loc_cd=102190&searchType=search&searchword=python&panel_type=&search_optional_item=y&search_done=y&panel_count=y"

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

def extract_job(result):
    company = result.find("div", {"class":"company_nm"}).find("a")["title"]
    title = result.find("div", {"class":"notification_info"}).find("a")["title"]
    location = result.find("div", {"class":"company_info"}).find("p", {"class":"work_place"}).string
    company = str(company)
    title = str(title)
    job_id = result["id"][4:]
    # print(job_id)
    return {'title': title, 'company': company, 'location': location, "link": f"http://www.saramin.co.kr/zf_user/jobs/relay/view?isMypage=no&rec_idx={job_id}&recommend_ids=eJxdkMsZwyAMg6fp3W%2FZ5w7C%2FlvU%2BQgh5fjbQpLRLIUHj6j44KuNbqojSA4cdg2KJalieC0UMh6wmOgJw0YYAy32A6dZJtodK6z3mvaWL7zlFZ7uPYgDV7dOb7s%2BZ7onomhhURtSPmFEIeC9le4mT3OylseKqtZW0L5LOEX%2FznR%2B9YZWDZAeeNek%2FtWs6%2FUPzpxT9w%3D%3D&view_type=list&gz=1&t_ref_content=general&t_ref=jobcategory_recruit#seq=0"}

def extract_saramin_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping page {page}")
        saramin_res = requests.get(f"{URL1}page={page+1}&{URL2}")
        saramin_soup = BeautifulSoup(saramin_res.text, "html.parser")
        results = saramin_soup.find_all("div", {"class":"list_item"})
        # print(results)
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs