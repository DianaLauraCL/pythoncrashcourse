import python_repos
import requests

def test_python_repos():
    url = 'http://api.github.com/search/repositories'
    url += '?q=language:python+sort:stars+stars:>10000'
    r = requests.get(url)

    status_code = r.status_code
    assert status_code == 200