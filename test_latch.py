# -*- encoding: utf-8 -*-

from __future__ import with_statement

import unittest
from flask import Flask
from flask_latch import Latch

LATCH_APP_NAME = "Flask-Latch"
LATCH_APP_ID = "xxxxxxxxxxxxxxx"
LATCH_SECRET_KEY = "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"
LATCH_ACCOUNT_ID = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"


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

    def test_connection(self):
        latch = Latch(self.app)
        assert latch.latch.appId == LATCH_APP_ID
        assert latch.latch.secretKey == LATCH_SECRET_KEY

    def test_pair(self):
        latch = Latch(self.app)
        response = latch.pair(raw_input("Pair token: "))
        assert isinstance(response, unicode)
        assert response == LATCH_ACCOUNT_ID

    def test_staus(self):
        latch = Latch(self.app)
        result = latch.status(LATCH_ACCOUNT_ID)
        assert result["status"] == "on"
        assert result["name"] == LATCH_APP_NAME


if __name__ == '__main__':
    unittest.main()
