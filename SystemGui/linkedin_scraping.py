from scrape_linkedin import ProfileScraper
from scrape_linkedin.ProfileIdsGoogle import ProfileIdsGoogle
from scrape_linkedin.CreateDoc import CreateDoc
import json
import csv
import pprint


def test(title,loc,li_at):
    try: 
        with ProfileIdsGoogle(cookie=li_at) as idsScrap:
            idsScrap.getIds(jobTitle=title,location=loc)
        users = []
        data = []    
        with open('result.csv','r') as csvFile:
            reader = csv.reader(csvFile,delimiter=',')
            for row in reader:
                for index in row:
                    users.append(index)
        csvFile.close()   
        if users:
            with ProfileScraper(cookie=li_at) as scraper:
                for i in users:
                    profile = scraper.scrape(user=i)
                    if profile is not None:
                        data.append(profile.to_dict())
            CreateDoc().create(data=data)
            return data
    
    except Exception as e:
        print(e)
        return e