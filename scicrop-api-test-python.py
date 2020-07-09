import json
import requests


def post_resume():
    with open('resume.json') as f:
        resume = json.load(f)

    resume = json.dumps(resume, indent=2)

    post_url = 'https://engine.scicrop.com/scicrop-engine-web/api/v1/jobs/post_resume'
    post_request = requests.post(post_url, json=resume)

    print(post_request)


if __name__ == '__main__':
    post_resume()
