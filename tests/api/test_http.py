import pytest
import requests


@pytest.mark.http
def test_first_request():
    r = requests.get('https://api.github.com/zen')
    print(r.text)


@pytest.mark.http
def test_second_request():
    r = requests.get('https://api.github.com/users/cannelle')
    body = r.json()
    headers = r.headers

    assert body['login'] == 'cannelle'
    # print(f'Response Body is {r.json()}')
    # print(f'Response Status code is {r.status_code}')
    assert r.status_code == 200
    # print(f'Response Headers are {r.headers}')
    assert headers['Server'] == 'GitHub.com'


@pytest.mark.http
def test_status_code_request():
    r = requests.get('https://api.github.com/users/alina_repka')

    assert r.status_code == 404
