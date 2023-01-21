from bs4 import BeautifulSoup
import requests


def extract_remoteok_jobs(term):
  url = f"https://remoteok.com/remote-{term}-jobs"
  request = requests.get(url, headers={"User-Agent": "Kimchi"})
  if request.status_code == 200:
    soup = BeautifulSoup(request.text, "html.parser")

    jobListAll = []  #모든 job의 정보
    jobs = soup.find_all('tr', class_="job")
    for job in jobs:
      jobDict = {}  #한 job의 정보
      #링크 추가
      jobDict['link'] = "https://remoteok.com" + job.find(
        'a', class_="preventLink")["href"].strip()
      # 회사 페이지 링크 추가
      jobDict['companyLink'] = "https://remoteok.com" + job.find(
        'span', class_="companyLink")["href"].strip()
      #제목 추가
      jobDict['title'] = job.find('h2', itemprop="title").text.strip()
      #회사 추가
      jobDict['company'] = job.find('h3', itemprop="name").text.strip()

      #지역/봉급 추가
      #location이 하나도 없을 때
      if len(job.find_all('div', class_="location")) == 0:
        jobDict['location'] = []
        jobDict['salary'] = ""
      #location이 하나 있는데, 하나 있으면 무조건 salary(봉급)
      elif len(job.find_all('div', class_="location")) == 1:
        jobDict['location'] = []
        jobDict['salary'] = job.find('div', class_="location").text[2:]
      #location이 하나 초과로 있는 job
      else:
        locationList = []
        for location in job.find_all('div', class_="location"):
          locationList.append(location.text)
        jobDict['salary'] = locationList[-1][2:]
        locationList.pop(-1)
        jobDict['location'] = locationList

      #tag 추가
      jobDict['tag'] = []
      tags = job.find_all('div', class_="action-add-tag")
      for tag in tags:
        jobDict['tag'].append(tag.text.strip())

      #time 추가
      jobDict['time'] = job.find('td', class_="time").find('time')["datetime"]
      jobListAll.append(jobDict)  #한 job의 dictionary를 전체 job list에 추가
    return jobListAll
  else:
    return [{'error', request.status_code}]
