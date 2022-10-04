from recorder import Recorder as recorder
from utilities import Utility as util
from django.http import JsonResponse
from asyncio import subprocess
from time import time

import datetime
import os


class LiveStream():
    """
        [ BASE STREAMER CLASS ]
        - Contains all stream related features
    """

    def __init__(self, wowza_feed):
        super().__init__(wowza_feed)
        self.context = {
            'flag': False,
            'message': ''
        }
        self.RTMP_PUSH_DOMAIN = os.environ.get("RTMP_PUSH_DOMAIN", "rtmp://localhost/live/")
        self.RTSP_PUSH_DOMAIN = os.environ.get("RTSP_PUSH_DOMAIN", "rtsp://localhost:5554/")
        self.PUSH_TARGET_BASE = os.environ.get("PUSH_TARGET_BASE", "rtsp://localhost:5554/")
        self.MEDIA_PATH = os.environ.get("MEDIA_PATH", "/home/staqu/mist_server/media/")


    def push_rtsp_ffmpeg(self, stream_name, stream_source):
        """
            Pushes a stream from "stream_source" using ffmpeg subprocess to defined blank push -
            * [rtsp://(host):(port)/(stream_name)]
        """

        stream_target = str(self.PUSH_TARGET_BASE + stream_name).strip()

        ffmpeg_push_command = ["ffmpeg", "-re", "-i", stream_source, "-f", "rtsp", "-c:v", "copy", "-c:a", "copy", stream_target]

        ffmpeg_push_process = subprocess.Popen(ffmpeg_push_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = ffmpeg_push_process.communicate()

        time.sleep(2.5)

        if err:
            print(f"{datetime.now()} - [CRITICAL] - {err}")
            return False

        return True


    def add_push_stream(self, request, stream_name, stream_source):
        """
            To add a PUSH to

            - push://(domain)/live/(stream_name)

            - REQUIRED PARAMS: stream_name -> string
            - CONSTRAINTS: 'stream_name' contains only lower case & underscores
        """

        stream_name = request.data.get("stream_name") # -> String

        command = \
            {
            "addstream":
                {
                    stream_name:
                    {
                        "source": "push://"
                    }
                }
            }

        url = util.generate_request_url(command)
        response = util.get_request_response(url)

        if response.status_code == 200:
            push_rtsp_ffmpeg = self.push_rtsp_ffmpeg(stream_name, stream_source)

            if not push_rtsp_ffmpeg:
                self.context = {'message': "Stream failed to push"}

            else:
                push_urls = \
                    {
                    'rtmp_full_url': self.RTMP_PUSH_DOMAIN + stream_name,
                    'rtsp_full_url': self.RTSP_PUSH_DOMAIN + stream_name,
                    'rtmp_base_url': self.RTMP_PUSH_DOMAIN,
                    'stream_name': stream_name
                    }
                self.context = {'flag': True, 'message': "Stream added sucessfully", 'push_urls': push_urls}
        else:
            self.context['message'] = "Stream failed to push!"

        return JsonResponse(self.context)


    # TODO: Insert into database after every successful stream addition
    def update_add_stream(self, request):
        """
            To ADD/UPDATE a stream's name and/or source.

            REQUEST BODY:
            {
                "stream_name" : stream_name,
                "source" : source,
                "always_on" : True/False
            }

            REQUIRED PARAMS: stream_name -> string
                             source -> string
            OPTIONAL PARAMS: always_on -> bool
        """

        stream_name = request.data.get("stream_name")
        always_on = next(request.data.get("always_on"), True)
        source = request.data.get("source")

        command = \
            {
            "addstream":
                {
                    f"{stream_name}":
                    {
                        "source": f"{source}",
                        "always_on": always_on
                    }
                }
            }

        url = util.generate_request_url(command)
        response = util.get_request_response(url)

        if response.status_code == 404 :
            self.context['message'] = "Stream failed to add"

        elif response.status_code == 200 :
            # TODO: recorder.add_auto_push_recording(stream_name) should return boolean whether stream was added or not
            recording_started = True if recorder.add_auto_push_recording(stream_name) else False
            self.context = {
                'flag': True, 'message': "Stream added sucessfully",
                'stream_name': stream_name,
                'recording_started': recording_started
                }

        return JsonResponse(self.context)


    def get_all_streams(self):
        """
            To get all added (configured) streams.

            Default API request always returns 'streams' object.
        """
        url = util.generate_request_url()
        response = util.get_request_response(url)
        streams = response.get('streams')

        if not response:
            self.context['message'] = "Unable to fetch streams"
        else:
            self.context = {'flag': True, 'message': "All streams fetched sucessfully", 'streams': streams}

        return JsonResponse(self.context)


    def get_active_streams(self):
        """
            To get all active streams.

            REQUEST BODY:
            {
                "active_streams" : True,
                "source" : source,
                "always_on" : True
            }
            REQUIRED PARAMS: active_streams -> bool
        """

        command = \
            {
                "active_streams": True
            }

        url = util.generate_request_url(command)
        response = util.get_request_response(url)
        active_streams = response.get('active_streams')

        if not response:
            self.context['message'] = "Unable to fetch active streams"
        else:
            self.context = {'flag': True, 'message': "Active streams fetched sucessfully", 'active_streams': active_streams}

        return JsonResponse(self.context)


    def delete_stream(self, request):
        """
            Deletes single stream at a time.

            {
                "deletestream" : "streamname_here"
            }
        """

        stream_name = request.data.get("stream_name")
        command = \
            {
                "deletestream": stream_name
            }
        url = util.generate_request_url(command)
        response = util.get_request_response(url)
        if not response:
            self.context['message'] = "Unable to delete stream"
        else:
            self.context['message'] = "Streams deleted sucessfully"

        return JsonResponse(self.context)