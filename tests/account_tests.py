import random

from api.account_api import Account
from config import Currency

curr = Currency()


class TestAccount(Account):
    cur_ru = Currency.CURRENCY_RU

    def test_post_sign_up_valid_user(self):
        email = "poleshuk.alex134@gmail.com"
        password = "aaaAAA1"
        lang = "ru"
        country = "RU"
        currency = self.cur_ru[random.randint(0, 7)]
        status_code, body = self.post_sign_up(email, password, lang, country, currency)
        assert status_code == 200, "Статус код не соответсвует ожидаемому"
        assert body["status"] == "success", "Статус в теле ответа не соответсвует"
        assert body["data"]["email"] == email, "Почта в теле ответа не соответсвует"
