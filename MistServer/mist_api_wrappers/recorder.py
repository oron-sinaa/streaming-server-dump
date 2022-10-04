from django.http import JsonResponse as JsonResponse
from datetime import datetime, timedelta
from utilities import Utility as util
from pytz import timezone

import json, os


class Recorder():
    """
    [ BASE RECORDER CLASS ] \n
    'Contains helper functions'
    """

    def __init__(self):
        self.MEDIA_PATH = os.environ.get("MEDIA_PATH", "/home/DVR/m3u8_recordings/")
        self.current_time = datetime.now()
        self.current_time_utc = self.current_time(timezone('UTC'))
        self.vod_playback_path = "{MEDIA_PATH}/stream_{stream_name}/{year}-{month}-{day}/{hour}/playlist.m3u8"
        self.VOD_DURATION_THRESHOLD = int(os.getenv('VOD_DURATION_THRESHOLD_HRS', 3))

        self.stream_playback_base = ""


    def get_time_difference(self, alert_created):
        """
            To Fetch time difference
        """
        # IST to UTC
        now = self.current_time.replace(tzinfo=timezone('UTC')) - timedelta(hours=5, minutes=30)
        return now - alert_created


    def add_auto_push_recording(self, stream_name):
        """
        Any matching streams that become active in the future, will upon activation also start a push (recording) as \
        requested here, until the automatic push (recording) is removed again.

        * { "push_auto_add":["STREAMNAME", "URI", scheduletime, completetime] }

        * ?split=1234 - Restarts recording at a keyframe roughly every given amount of seconds (rounding up to nearest keyframe).
                        Re-parses text replacement variables before restarting, allowing for splitting recordings
                        into multiple files with time-based filenames over time in a flexible manner.
        """

        current_datetime = datetime.now()
        next_hour = datetime.now().replace(hour=current_datetime.hour, minute=0, second=0)

        recstartunix, recstopunix = util.get_unix_time(current_datetime), util.get_unix_time(next_hour)

        # Example -> /home/DVR/m3u8_recordings/20220926_15/playlist.m3u8
        start_recording_url = \
            f"{self.MEDIA_PATH}/stream_${stream_name}/$year-$month-$day/$hour/playlist.m3u8?recstartunix={recstartunix}?recstopunix={recstopunix}"
        split_recording_url = \
            f"{self.MEDIA_PATH}/stream_${stream_name}/$year-$month-$day/$hour/playlist.m3u8?recstartunix={recstopunix}?split=3600"

        command_start_rec = \
            {
            "push_auto_add":
                {
                    stream_name:
                        {
                            start_recording_url
                        }
                }
            }

        command_split_rec = \
            {
            "push_auto_add":
                {
                    stream_name:
                        {
                            split_recording_url
                        }
                }
            }

        url_start_rec = util.generate_request_url(command_start_rec)
        url_split_rec = util.generate_request_url(command_split_rec)

        response_start_rec = util.get_request_response(url_start_rec)
        response_split_rec = util.get_request_response(url_split_rec)

        if response_start_rec.status_code == 200 and response_split_rec.status_code == 200:
            return True

        return False


    def remove_auto_push_recording(self, stream_name):
        """
            [ WARNING! ]: This will stop any recording for the specified stream

            This call will stop automatic pushing of matching stream/target combinations.

            { "push_auto_remove":"STREAMNAME" //Removes all entries for the given stream name. }
        """

        command = \
            {
                "push_auto_remove": stream_name
            }

        url = util.generate_request_url(command)
        response = util.get_request_response(url)

        if response:
            self.context = {'flag': True, 'message': "Push auto remove success"}
        else:
            self.context['message'] = "Push auto remove failed"
        return JsonResponse(self.context)


    def get_playback_url(self, stream_name, start_time, end_time):
        """
        RETURNS: Playback URL
        CONDITIONS:
        - if playback_duration < VOD_DURATION_THRESHOLD : from (nDVR) local storage
        - if playack_duration > VOD_DURATION_THRESHOLD : from (DVR) cloud storage
        """

        # Calculate time difference in minutes:
        seconds_in_day = 1440 #24 * 60 * 60
        playack_duration = datetime.self.current_time - start_time
        playack_duration = divmod(playack_duration.days * seconds_in_day + playack_duration.seconds, 60)

        # TODO: get m3u8 from start_time to end_time
        # Get recording URL from (nDVR) local storage
        if playack_duration[0] > self.VOD_DURATION_THRESHOLD:
            vod_playback_path = self.vod_playback_path.format(
                MEDIA_PATH = self.MEDIA_PATH,
                streamname = stream_name,
                year = datetime.now().year,
                month = datetime.now().month,
                day = datetime.now().day,
                hour = datetime.now().hour
            )
            return vod_playback_path

        # TODO: get stream url from MP4 API export to cloud
        # Get recording URL from (DVR) cloud storage
        else:
            stream_playback_url = ""
            pass