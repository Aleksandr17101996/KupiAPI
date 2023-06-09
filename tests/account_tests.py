import random

from api.account_api import Account
from config import Locale


class TestAccount(Account):
    currency = Locale.CURRENCY
    lang = Locale.LANG
    country = Locale.COUNTRY

    def test_post_sign_up_valid_user(self):
        email = "poleshuk.alex@gmail.com"
        password = "aaaAAA1"
        lang = self.lang[random.randint(0, 7)]
        country = self.country[random.randint(0, 1)]
        currency = self.currency[random.randint(0, 14)]
        status_code, body = self.post_sign_up(email, password, lang, country, currency)
        assert status_code == 200, "Статус код не соответсвует ожидаемому"
        assert body["status"] == "success", "Статус в теле ответа не соответсвует"
        assert body["data"]["email"] == email, "Почта в теле ответа не соответсвует"
