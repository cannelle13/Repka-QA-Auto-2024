import requests


class GitHub:

    # def get_user_cannelle13(self):
    # r = requests.get('https://api.github.com/users/cannelle13')
    #        body = r.json()

    #        return body

    #    def get_non_exist_user(self):
    #        r = requests.get('https://api.github.com/users/alinarepka')
    #        body = r.json()

    #        return body
    # Оптимізуємо код, щоб передавати параметр username

    def get_user(self, username):
        r = requests.get(f"https://api.github.com/users/{username}")
        body = r.json()

        return body

    def search_repo(self, name):
        r = requests.get(
            "https://api.github.com/search/repositories", params={"q": name}
        )
        body = r.json()

        return body
