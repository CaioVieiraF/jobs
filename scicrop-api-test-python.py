import requests
import json
import time
from datetime import date, datetime


def post_resume():
    with open('resume.json') as f:
        resume = json.load(f)

    start_date = datetime.today()
    begin_date = date(2019, 3, 7)
    end_date = date(2022, 11, 29)
    resume['degrees'][0]['begin_date'] = int(time.mktime(begin_date.timetuple()))
    resume['degrees'][0]['end_date'] = int(time.mktime(end_date.timetuple()))
    resume['start_date'] = int(time.mktime(start_date.timetuple()))

    # post method test:
    # post_url = 'http://httpbin.org/post'
    post_url = 'https://engine.scicrop.com/scicrop-engine-web/api/v1/jobs/post_resume'
    post_request = requests.post(post_url, json=resume)

    print(post_request)
    with open('response.json', 'wb') as f:
        f.write(post_request.content)


if __name__ == '__main__':
    post_resume()
