import requests
from bs4 import BeautifulSoup

saramin_res = requests.get("http://www.saramin.co.kr/zf_user/jobs/list/job-category?cat_key=40430%2C40404%2C40426%2C40427&loc_mcd=101000&loc_cd=102190&panel_type=&search_optional_item=n&search_done=y&panel_count=y")
# print(saramin_res.text)

# html parser를 이용해서 html 코드를 Navigate할 것 
saramin_soup = BeautifulSoup(saramin_res.text, "html.parser")

# pagination className을 가진 div 태그 추출
pagination = saramin_soup.find("div", {"class":"pagination"})
# print(pagination)

# a 태그를 가진 모든 내용 출력
pages = pagination.find_all('a')
# print(pages)

spans = []
for page in pages:
  spans.append(page.find("span"))

# print(spans[:-1])
# spans를 모두 가져오되 마지막 것은 제외

spans = spans[:-1]
print(spans)