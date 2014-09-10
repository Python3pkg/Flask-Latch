# -*- encoding: utf-8 -*-

from __future__ import with_statement

import sys
import unittest
from flask import Flask
from flask_latch import Latch

try:
    from flask import _app_ctx_stack as stack
except ImportError:
    sys.stderr.write("Flask >= 0.9 is required.")


class TestLatchConfig(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)

    def test_app_configuration(self):
        self.app.config.setdefault("LATCH_APP_ID", "snA9FKQ7XydnmreYywCm")
        self.app.config.setdefault("LATCH_SECRET_KEY",
                                   "Zz8v33rr9yP3ZNtQjJMBC4BmBeFpyEi7GbmPqPTP")
        assert self.app.config.get("LATCH_APP_ID"), "LATCH_APP_ID is not set"
        assert self.app.config.get("LATCH_SECRET_KEY"), \
            "LATCH_SECRET_KEY is not set"


class TestLatch(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config.setdefault("LATCH_APP_ID", "snA9FKQ7XydnmreYywCm")
        self.app.config.setdefault("LATCH_SECRET_KEY",
                                   "Zz8v33rr9yP3ZNtQjJMBC4BmBeFpyEi7GbmPqPTP")

    def test_latch_connection(self):
        with self.app.test_request_context():
            self.latch = Latch(self.app)
            ctx = stack.top
            assert ctx.latch

    def test_latch_connection_response(self):
        with self.app.test_request_context():
            self.latch = Latch(self.app)
            ctx = stack.top
            assert ctx.latch
            self.latch.status()


if __name__ == '__main__':
    unittest.main()
