import pytest
# from modules.api.clients.github import GitHub


@pytest.mark.api
def test_user_exists(github_api):
    # api = GitHub()
    user = github_api.get_user('cannelle13')
    assert user['login'] == 'cannelle13'


@pytest.mark.api
def test_user_not_exists(github_api):
    # api = GitHub()
    r = github_api.get_user('alinarepka')
    # print(r) - щоб побачити, що виводиться в тілі відповіді
    assert r['status'] == '404'


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('Repka-QA-Auto-2024')
    print(r)
    assert r['total_count'] == 1
    # assert 'repka-qa-auto' in r['items'][0]['name']


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('sergiibutenko_repo_non_exist')
    assert r['total_count'] == 0


@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0
