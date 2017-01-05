#!python3
#encoding:utf-8

import sqlite3
import traceback

class GoogleKeysGetter:
    def __init__(self):
        pass

    def initialize(self, path):
        self.connector = sqlite3.connect(path)
        self.cursor = self.connector.cursor()

    def get_api_key(self, google_project_id):
        pid = self._get_meta_project_id(google_project_id)
        sql = "select ApiKey from ApiKeys where ProjectId = '{0}';".format(pid)
        self.cursor.execute(sql)
        try:
            items = self.cursor.fetchall()
            return items[0][0]
        except:
            traceback.print_exc()
            return None

    def get_meta_client_id(self, google_project_id):
        pid = self._get_meta_project_id(google_project_id)
        sql = "select Id from ClientIds where ProjectId = '{0}';".format(pid)
        self.cursor.execute(sql)
        try:
            items = self.cursor.fetchall()
            return items[0][0]
        except:
            traceback.print_exc()
            return None

    def get_client_id(self, google_project_id):
        pid = self._get_meta_project_id(google_project_id)
        sql = "select ClientId from ClientIds where ProjectId = '{0}';".format(pid)
        self.cursor.execute(sql)
        try:
            items = self.cursor.fetchall()
            return items[0][0]
        except:
            traceback.print_exc()
            return None

    def get_client_secret(self, google_project_id):
        pid = self._get_meta_project_id(google_project_id)
        sql = "select ClientSecret from ClientIds where ProjectId = '{0}';".format(pid)
        self.cursor.execute(sql)
        try:
            items = self.cursor.fetchall()
            return items[0][0]
        except:
            traceback.print_exc()
            return None

    def get_refresh_token(self, client_id):
        cid = None
        sql = "select Id from ClientIds where ClientId = '{0}';".format(client_id)
        self.cursor.execute(sql)
        try:
            items = self.cursor.fetchall()
            cid = items[0][0]
        except:
            traceback.print_exc()
            return None

        sql = "select RefreshToken from RefreshTokens where ClientId = '{0}';".format(cid)
        self.cursor.execute(sql)
        try:
            items = self.cursor.fetchall()
            return items[0][0]
        except:
            traceback.print_exc()
            return None

    def _get_meta_project_id(self, google_project_id):
        sql = "select Id from Projects where GoogleProjectId = '{0}';".format(google_project_id)
        self.cursor.execute(sql)
        try:
            items = self.cursor.fetchall()
            return items[0][0]
        except:
            traceback.print_exc()
            return None

    def get_first_project_id(self):
        sql = "select GoogleProjectId from Projects;"
        self.cursor.execute(sql)
        try:
            items = self.cursor.fetchall()
            return items[0][0]
        except:
            traceback.print_exc()
            return None
