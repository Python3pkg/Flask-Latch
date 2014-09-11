# -*- encoding: utf-8 -*-
from __future__ import with_statement

__version_info__ = ('0', '0', '1')
__version__ = '.'.join(__version_info__)
__author__ = 'Jaume Martin'
__license__ = 'MIT'
__copyright__ = '(c) 2014 by Jaume Martin'
__all__ = ['Latch']


import sys
import latch


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
        if app_id is not None and secret_key is not None:
            self.latch = latch.Latch(app_id, secret_key)

    def pair(self, token):
        if token:
            response = self.latch.pair(token)
            if response.get_error() == "":
                return response.data["accountId"]
            else:
                return (response.error.code, response.error.message)

    def status(self, account_id):
        if account_id:
            response = self.latch.status(account_id)
            if response.get_error() == "":
                return response.data["operations"][
                    self.app.config.get("LATCH_APP_ID")]
            else:
                return (response.error.code, response.error.message)

    def unpair(self, account_id):
        if account_id:
            response = self.latch.unpair(account_id)
            if response.get_error() != response.get_data():
                return (response.error.code, response.error.message)

    def is_lock(self, account_id):
        data = self.status(account_id)
        return data["status"] == "off"

    def is_unlock(self, account_id):
        return not self.is_lock(account_id)
