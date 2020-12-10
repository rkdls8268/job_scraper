import csv

def save_to_file(jobs, word):
    file = open(f"{word}_jobs.csv", mode="w", encoding='utf-8')
    # 인코딩
    # file = open("jobs.csv", mode="w", encoding='utf-8')
    # csv 파일 작성하기
    writer = csv.writer(file) # 방금 우리가 연 파일(file)에 csv를 작성
    writer.writerow(["title", "company", "location", "link"])
    for job in jobs:
        writer.writerow(list(job.values()))
    return