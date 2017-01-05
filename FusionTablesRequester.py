#!python3
#encoding:utf-8

import os.path
import requests
import urllib.parse
import json
from datetime import datetime
import AccessTokenRequester
import GoogleKeysGetter

class FusionTablesRequester:
    def __init__(self):
        self.google_keys_getter = None
        self.token_requester = None
        self.api_key = None
        self.client_id = None
        self.client_secret = None
        self.refresh_key = None
        self.access_key = None

    def initialize(self, db_path, project_id=None):
        self.google_keys_getter = GoogleKeysGetter.GoogleKeysGetter()
        self.google_keys_getter.initialize(db_path)
        if (None is project_id):
            project_id = self.google_keys_getter.get_first_project_id()
        self.api_key = self.google_keys_getter.get_api_key(project_id)
        self.client_id = self.google_keys_getter.get_client_id(project_id)
        self.client_secret = self.google_keys_getter.get_client_secret(project_id)
        self.refresh_token = self.google_keys_getter.get_refresh_token(self.client_id)
        self.token_requester = AccessTokenRequester.AccessTokenRequester()
        self.access_token = self.token_requester.get_access_token(self.client_id, self.client_secret, self.refresh_token)

    def query(self, sql, is_write_response=False):
        r = self._query_request(sql)
        print(r.text)
        
        if not(r.status_code == 200):
            print("Error: {0}\n".format(r.status_code))
            print(r.text)
            if (self._is_old_asscess_token(r)):
                self.access_token = self.token_requester.get_access_token(self.client_id, self.client_secret, self.refresh_token)
                r = self._query_request(sql)
                print(r.text)

        if (is_write_response):
            filePath = "Google.FusionTables.query.{0:%Y%m%d%H%M%S}.json".format(datetime.now())
            file = open(filePath, 'w', encoding='utf-8')
            file.write(r.text)
            file.close()

    def _query_request(self, sql):
        headers={'Content-Type':'application/json'}
        data = {
            "sql": sql
        }
        url = ('https://www.googleapis.com/fusiontables/v2/query?' +
                'key=' + urllib.parse.quote(self.api_key) + '&' + 
                'access_token=' + urllib.parse.quote(self.access_token) + '&' + 
                'sql=' + urllib.parse.quote(sql))
        return requests.post(url, data=data, headers=headers)

    def _is_old_asscess_token(self, response):
        if (response.status_code == 401):
            j = json.loads(response.text)
            errors = j["error"]["errors"][0]
            if (errors["reason"] == "authError" and 
                errors["message"] == "Invalid Credentials" and
                errors["location"] == "Authorization"
            ):
                return True
            else:
                return False
