import requests
from config import Base


class Account:
    url = Base.BASE_URL
    ver = Base.VERSION
    acc = "account/"
    v = "2.0"

    """Библиотека api для работы с аккаунтом"""

    def post_sign_up(self, email, password, lang, country, currency):
        """ Метод отправляет запрос на регистрацию пользователя """

        data = {
            "email": email,
            "password": password,
            "lang": lang,
            "country": country,
            "currency": currency,
            "cookie_policy_accept": False,
            "v": self.v
        }

        r = requests.post(self.url + self.ver + self.acc + "sign_up.json", json=data)
        status_code = r.status_code
        body = r.json()
        return status_code, body
