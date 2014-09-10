# -*- encoding: utf-8 -*-
from __future__ import with_statement

__version_info__ = ('0', '0', '1')
__version__ = '.'.join(__version_info__)
__author__ = 'Jaume Martin'
__license__ = 'MIT'
__copyright__ = '(c) 2014 by Jaume Martin'
__all__ = ['Latch']


import sys
from functools import wraps
import latch
from flask import current_app

try:
    from flask import _app_ctx_stack as stack
except ImportError:
    sys.stderr.write("Flask >= 0.9 is required.")


class Latch(object):

    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app_id = app.config.get("LATCH_APP_ID", None)
        secret_key = app.config.get("LATCH_SECRET_KEY", None)
        if app_id is None:
            sys.stderr.write("LATCH_APP_ID configuration values is required")
        if secret_key is None:
            sys.stderr.write(
                "LATCH_SECRET_KEY configuration values is required")
        ctx = stack.top
        ctx.latch = latch.Latch(app_id, secret_key)

    def pair(self, token):
        pass

    def status(self, account_id):
        ctx = stack.top
        self.data = ctx.latch.data
        print(self.data)

    def unpair(self, account_id):
        pass

    def account_is_lock(self, account_id):
        pass

    def account_is_unlock(self, account_id):
        pass
