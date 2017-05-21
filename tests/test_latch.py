# -*- encoding: utf-8 -*-



import unittest
from flask import Flask
from flask_latch import Latch

LATCH_APP_NAME = "Flask-Latch"
LATCH_APP_ID = "XXXXXXXXXXXXXXX"
LATCH_SECRET_KEY = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY"
LATCH_ACCOUNT_ID = "ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ"


class TestLatchConfig(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)

    def test_app_configuration(self):
        self.app.config.setdefault("LATCH_APP_ID", LATCH_APP_ID)
        self.app.config.setdefault("LATCH_SECRET_KEY", LATCH_SECRET_KEY)
        assert self.app.config.get("LATCH_APP_ID"), "LATCH_APP_ID is not set"
        assert self.app.config.get("LATCH_SECRET_KEY"), \
            "LATCH_SECRET_KEY is not set"


class TestLatch(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config.setdefault("LATCH_APP_ID", LATCH_APP_ID)
        self.app.config.setdefault("LATCH_SECRET_KEY", LATCH_SECRET_KEY)

    def tearDown(self):
        pass

    def test_connection(self):
        latch = Latch(self.app)
        assert latch.latch
        assert latch.latch.appId == LATCH_APP_ID
        assert latch.latch.secretKey == LATCH_SECRET_KEY

    def test_pair_success(self):
        latch = Latch(self.app)
        response = latch.pair(input("Pair token: "))
        assert isinstance(response, str)
        assert response == LATCH_ACCOUNT_ID

    def test_pair_failure(self):
        latch = Latch(self.app)
        response = latch.pair("INVALID TOKEN")
        assert isinstance(response, tuple)

    def test_staus_success(self):
        latch = Latch(self.app)
        result = latch.status(LATCH_ACCOUNT_ID)
        assert result["status"] == "on"
        assert result["name"] == LATCH_APP_NAME

    def test_staus_failure(self):
        latch = Latch(self.app)
        result = latch.status("INVALID ACCOUNT ID")
        assert isinstance(result, tuple)

    def test_unpair_success(self):
        latch = Latch(self.app)
        response = latch.unpair(LATCH_ACCOUNT_ID)
        assert response is None

    def test_unpair_failure(self):
        latch = Latch(self.app)
        response = latch.unpair("INVALUD ACCOUNT ID")
        assert isinstance(response, tuple)


if __name__ == '__main__':
    unittest.main()
