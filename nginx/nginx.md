# NGINX

<br>

> - [nginx vod module](https://github.com/kaltura/nginx-vod-module)
> - https://packages.debian.org/sid/libnginx-mod-rtmp
> - https://www.guyrking.com/2019/10/20/configure-run-and-test-nginx-on-localhost.html
> - https://www.digitalocean.com/community/tutorials/how-to-set-up-a-video-streaming-server-using-nginx-rtmp-on-ubuntu-20-04

<br>

## Package: libnginx-mod-rtmp (1.22.0-3) 
---

<br>

RTMP support for Nginx

The nginx RTMP module is a fully-featured streaming solution implemented in nginx.

It provides the following features:

 - Live streaming with RTMP, HLS and MPEG-DASH;
 - RTMP Video on Demand from local or HTTP sources;
 - Stream relay support via a push or pull model;
 - Integrated stream recording;
 - and more.



<br>

## Run docker image
---

> `sudo docker run --interactive --tty --publish 8000:80 nginx bash`