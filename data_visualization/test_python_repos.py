import python_repos
import requests

url = 'http://api.github.com/search/repositories'
url += '?q=language:python+sort:stars+stars:>10000'

headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
# print(f"Status code: {r.status_code}")
def test_python_repos():
    status_code = r.status_code
    assert status_code == 200