from bs4 import BeautifulSoup
import requests

def extract_jobs(term):
    url = f"https://remoteok.com/remote-{term}-jobs"
    request = requests.get(url, headers={"User-Agent": "Kimchi"})
    if request.status_code == 200:
        soup = BeautifulSoup(request.text, "html.parser")

        jobListAll = []  # 모든 job의 정보
        jobs = soup.find_all('tr', class_="job")
        for job in jobs:
            jobDict = {}  # 한 job의 정보
            # 링크 추가
            jobDict['link'] = "https://remoteok.com" + job.find(
                'a', class_="preventLink")["href"].strip()
            # 제목 추가
            jobDict['title'] = job.find('h2').text.strip()
            # 회사명 추가
            jobDict['company'] = job.find('span',
                                          class_="companyLink").text.strip()
            # 지역 추가
            jobDict['location'] = job.find_all(
                'div', class_="location")[0].text[2:].strip()
            # 봉급 추가
            jobDict['salary'] = job.find_all(
                'div', class_="location")[1].text[2:].strip()
            # 태그 list 추가
            jobDict['tag'] = []
            tags = job.find_all('div', class_="action-add-tag")
            for tag in tags:
                jobDict['tag'].append(tag.text.strip())
            # 시간 추가
            jobDict['time'] = job.find('td',
                                       class_="time").find('time')["datetime"]
            jobListAll.append(jobDict)  # 한 job의 dictionary를 전체 job list에 추가
        print(jobListAll)
    else:
        print("Can't get jobs.")


extract_jobs("rust")
