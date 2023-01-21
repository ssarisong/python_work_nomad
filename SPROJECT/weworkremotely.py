from bs4 import BeautifulSoup
import requests


def extract_weworkremotely_jobs(term):
  url = f"https://weworkremotely.com/remote-jobs/search?term={term}"
  request = requests.get(url, headers={"User-Agent": "Kimchi"})
  if request.status_code == 200:
    soup = BeautifulSoup(request.text, "html.parser")
    jobList = []
    for jobs in soup.find_all('section', class_="jobs"):
      for job in jobs.find_all('li'):
        if job["class"] != ['view-all']:
          jobDict = {}
          jobDict['link'] = "https://weworkremotely.com" + job.find_all('a')[1]["href"].strip()
          jobDict['companyLink'] = "https://weworkremotely.com" + job.find('div', class_='tooltip').find('a')["href"]
          jobDict['title'] = job.find('span', class_="title").text.strip()
          jobDict['company'] = job.find('span', class_="company").text.strip()
          jobDict['workingHour'] = job.find_all('span', class_="company")[1].text.strip()
          if job.find('span', class_="region") == None:
            jobDict['location'] = []
          else:
            jobDict['location'] = job.find('span', class_="region").text.split('/')
          jobList.append(jobDict)
          
    return jobList
  else:
    return [{'error', request.status_code}]