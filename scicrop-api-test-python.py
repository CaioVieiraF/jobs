import requests
import json


def post_resume():
    with open('resume.json') as f:
        resume = json.load(f)

    # post method test
    # post_url = 'http://httpbin.org/post'
    post_url = 'https://engine.scicrop.com/scicrop-engine-web/api/v1/jobs/post_resume'
    post_request = requests.post(post_url, json=resume)

    print(post_request)
    with open('response.json', 'wb') as f:
        f.write(post_request.content)


if __name__ == '__main__':
    post_resume()
