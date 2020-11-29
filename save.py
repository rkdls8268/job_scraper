import csv

def save_to_file(jobs):
    file = open("jobs.csv", mode="w")
    # csv 파일 작성하기
    writer = csv.writer(file) # 방금 우리가 연 파일(file)에 csv를 작성
    writer.writerow(["title", "company", "location", "link"])
    for job in jobs:
        writer.writerow(list(job.values()))
    return