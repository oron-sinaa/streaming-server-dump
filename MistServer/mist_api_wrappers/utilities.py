import os
import json
import requests
from datetime import datetime, timedelta
from pytz import timezone
from django.http import JsonResponse
import pandas as pd


class Utility():
    """
    [ BASE UTILITIES CLASS ] \n
    'Contains helper functions'
    """

    def __init__(self):
        self.MISTAPI_DOMAIN = os.environ.get("MISTAPI_DOMAIN", "http://localhost:4242/")


    def generate_request_url(self, command=None):
        """
            RETURNS: API URL including 'command' payload.
        """

        if command:
            command = json.dumps(command, separators=(',', ': '))
            url = f"{self.MISTAPI_DOMAIN}api?command={command}"
        else:
            url = f"{self.MISTAPI_DOMAIN}api"

        return url


    def get_request_response(self, url):
        """
            Hits any URL and fetch the 'response.content' data
            REQUIRED PARAMS: URL is the any API link
            RETURNS: Response data or False
        """

        try:
            res = requests.get(url = url)
            if res.status_code == 200:
                return res.json()
            else:
                print('Request URL API response: {}'.format(res.content))
                return False

        except Exception as e:
            print('Error at request_url', e)
            return False


    def generate_embed_context(self, url, embed_name):
        """
            RETURNS: A context dictionary.
        """

        context = {'flag': True, 'message': f"{embed_name} fetched sucessfully", 'url': url}

        return JsonResponse(context)


    def utc_to_timestamp_conversion(self, date_time):
        """
            RETURNS: timestamp input from date time input.
        """

        date_time = datetime.strptime(date_time, '%d.%m.%Y %H:%M:%S')
        utc_timestamp = date_time.replace(tzinfo=timezone.utc).timestamp()
        return utc_timestamp


    def timestamp_to_utc_conversion(self, timestamp_inp):
        """
            RETURNS: datetime from timestamp input.
        """

        date = datetime.datetime.utcfromtimestamp(timestamp_inp / 1e3)
        return date


    def get_push_id(self, target_url, stream_key):
        """
            RETURNS: PUSH ID from push_list/recording list
        """

        command = \
            {
                "push_list":True,
                "minimal":1
            }
        url = self.generate_request_url(command)
        push_list = self.get_request_response(url).json().get('push_list')

        for push in push_list:
            if push[1] == stream_key and push[2] == target_url:
                push_id = push[0]
                break

        if push_id:
            return push_id

        return False


    def get_auto_push_command(self, stream_key, url):
        """
            RETURNS: command for PUSH AUTO ADD or  to start RECORDING
        """

        command = \
            {
            "push_auto_add":
                [
                 stream_key, url
                ]
            }

        return command


    def get_unix_time(self, current_datetime):
        """
            RETURNS: Unix time by given datetime
        """

        current_unix_time = datetime.datetime.timestamp(current_datetime)
        return current_unix_time