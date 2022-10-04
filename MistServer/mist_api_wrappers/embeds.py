import os
from utilities import Utility as util
from django.http import JsonResponse


class Embeds():
    """
    [ GENERATES EMBED CODES & URLs ]
    """


    def __init__(self, requests):
        self.MISTPANEL_DOMAIN =  os.environ.get("MISTPANEL_DOMAIN", "http://localhost:8080/")
        self.STREAM_NAME = self.request.query_params.get("stream_name", None)
        self.RESPONSE = requests.get(url = f"{self.MISTPANEL_DOMAIN}json_{self.STREAM_NAME}.js").json()
        self.EMBED = requests.get(url = f"{self.MISTPANEL_DOMAIN}{self.STREAM_NAME}.html")
        self.SOURCE_LIST = self.RESPONSE.get('source')
        self.RTSP_DOMAIN = "rtsp://localhost:5554/"
        self.RTMP_PLAY_DOMAIN = os.environ.get("RTMP_PLAY_DOMAIN", "rtmp://localhost/play/")
        self.MP4_WEBSOCKET_DOMAIN= os.environ.get("MP4_WEBSOCKET_DOMAIN", "ws://localhost:8080/")


    def get_live_embed_code(self):
        """
            To get embed code of stream.
        """
        embed_code = self.EMBED.text
        response = util.generate_embed_context(embed_code, self.get_live_embed_code.func_name)

        return response


    def get_live_hls(self):
        """
            To get live HSL URL of stream.
        """
        # hls_url = list(filter(lambda source: source.get('hrn') == "HLS (TS)", self.SOURCE_LIST))[0].get('url')
        hls_url = f"{self.MISTPANEL_DOMAIN}hls/{self.STREAM_NAME}/index.m3u8"
        response = util.generate_embed_context(hls_url, self.get_live_hls.func_name)

        return response


    def get_live_mp4(self):
        """
            To get live mp4 URL of stream.
        """
        # mp4_url = list(filter(lambda source: source.get('hrn') == "MP4 WebSocket", self.SOURCE_LIST))[0].get('url')
        mp4_url = f"{self.MP4_WEBSOCKET_DOMAIN}{self.STREAM_NAME}.mp4"
        response = util.generate_embed_context(mp4_url, self.get_live_mp4.func_name)

        return response


    def get_live_dash(self):
        """
            To get live DASH URL of stream.
        """
        # dash_url = list(filter(lambda source: source.get('hrn') == "DASH", self.SOURCE_LIST))[0].get('url')
        dash_url = f"{self.MISTPANEL_DOMAIN}cmaf/{self.STREAM_NAME}/index.mpd"
        response = util.generate_embed_context(dash_url, self.get_live_dash.func_name)

        return response


    def get_live_rtmp(self):
        """
            To get live RTMP URL of stream.
        """
        # rtmp_url = list(filter(lambda source: source.get('hrn') == "RTMP", self.SOURCE_LIST))[0].get('url')
        rtmp_url = f"{self.RTMP_PLAY_DOMAIN}{self.STREAM_NAME}"
        response = util.generate_embed_context(rtmp_url, self.get_live_rtmp.func_name)

        return response


    def get_live_rtsp(self):
        """
            To get live RTSP URL of stream.
        """
        # rtsp_url = list(filter(lambda source: source.get('hrn') == "RTSP", self.SOURCE_LIST))[0].get('url')
        rtsp_url = f"{self.RTSP_DOMAIN}{self.STREAM_NAME}"
        response = util.generate_embed_context(rtsp_url, self.get_live_rtsp.func_name)

        return response


    def get_live_h264(self):
        """
            To get live h264 URL of stream.
        """
        # h264_url = list(filter(lambda source: source.get('hrn') == "Raw progressive", self.SOURCE_LIST))[0].get('url')
        h264_url = f"{self.MISTPANEL_DOMAIN}{self.STREAM_NAME}.h264"
        response = util.generate_embed_context(h264_url, self.get_live_h264.func_name)

        return response



