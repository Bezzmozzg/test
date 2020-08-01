import requests


class GetMeets:
    BASE_URL = "https://xsolla-test-analytics.herokuapp.com"

    def __init__(self, token, headers):
        self._token = token
        self._headers = headers

    def get_days(self):
        url = "{}/dates".format(self.BASE_URL)
        payload = {'token': self._token}
        response = requests.get(url, params=payload, headers=self._headers)
        dates = response.json()
        return dates["dates"]

    def get_meets(self, day):
        url = "{}/daily".format(self.BASE_URL)
        payload = {'day': day, 'token': self._token}
        page = requests.get(url, params=payload, headers=self._headers)
        return page.json()['meetings']
