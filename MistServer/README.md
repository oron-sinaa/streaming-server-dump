## **MistServer**
---


### Links

> [MistServer Calculator](https://news.mistserver.org/news/85/What+hardware+do+I+need+to+run+MistServer%3F)


> Mist server is one of the leading OTT (Internet Streaming) tool-kits with an open source core.
> 
> It allows you to deliver your media content to your users via the Internet.  


---
### -> Installation
---

*Ubuntu (Linux 64 bits) -*

> ` curl -o - https://releases.mistserver.org/is/mistserver_64V3.1.tar.gz 2>/dev/null | sh `

*[Other downloads](https://mistserver.org/download)*

*[Recording URL](https://weworkjarvisndvrci.blob.core.windows.net/ndvr/1664303400_1664307000/live/BLR0410FC002.stream.mp4?se=2022-09-28T07%3A17%3A15Z&sp=r&sv=2019-07-07&ss=b&srt=o&sig=W9craYleGcWPfUUej3%2Bpdue1FKGIzibAY4z66N8CKIs%3D)*

*[Recording Params](
   curl 'https://weworkjarvisndvrci.blob.core.windows.net/ndvr/1664339400_1664343000/live/BLR0410FC002.stream.mp4?se=2022-09-28T07%3A17%3A15Z&sp=r&sv=2019-07-07&ss=b&srt=o&sig=W9craYleGcWPfUUej3%2Bpdue1FKGIzibAY4z66N8CKIs%3D' 
   -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0' 
   -H 'Accept: video/webm,video/ogg,video/*;q=0.9,application/ogg;q=0.7,audio/*;q=0.6,*/*;q=0.5' 
   -H 'Accept-Language: en-US,en;q=0.5' 
   -H 'Range: bytes=653459456-' 
   -H 'Connection: keep-alive' 
   -H 'Referer: https://wework.jarvis.live/' 
   -H 'Sec-Fetch-Dest: video' 
   -H 'Sec-Fetch-Mode: no-cors' 
   -H 'Sec-Fetch-Site: cross-site')

---
### -> Components (7 binaries)
---

1. MistController  (Main)
2. MistIn	   (Read / In)
3. MistInBuffer    (Stream In)
4. MistOut	   (Write / Stream Out)
5. MistProc	   (Frame Processing)
6. MistAnalyzer	   (Probing)
7. MistUtil	   (Other Utilities)

![Mist Server Binaries](assets/Mist_binaries.png)


---
### Default Intallations 
---

1. Binaries
   - /usr/bin/Mist*

2. Settings
   - /etc/mistserver.conf

3. MistServer starts as self starting service on boot


---
### -> Web Panels
---

1. Overview
2. Protocols
3. Streams
4. Push
5. Triggers
6. Logs
7. Statistics
8. Server Stats

![Mist Server UI Panels](assets/Mist_panels.png)


---
### -> Test Cases (demo)
---


---
### -> Performance Statistics
---


---
### -> Highlight features
---

![Mist Server Highlight Features](assets/Mist_highlights.png)


### 1. *The Calculators*
---

   - [Hardware Requirements + Server Capabilities](https://news.mistserver.org/news/85/What+hardware+do+I+need+to+run+MistServer%3F)
  
<br>

### 2. *Embeds*
---

   - Generate and display the HTML code to embed a player onto a website.
   - Embedded player automatically detects stream settings & browser/device capabilities and for optimal playback.
   - Use a different host - Change the host in the embeddable url/codes in case the host used to connect to the web interface can not be used on the target website
   - URLs - (Stream info json/script)
   - Embed code
   - Embed code options (optional)
   - Protocol stream urls (generated based on available codecs in the stream and enabled protocols)
  
<br>

### 3. *Supported Protocols*
---

   - RTSP
   - HLS
   - WebRTC
   - RTMP
   - CMAF (fMP4) over HTTP (DASH, HLS7, HSS)
   - (using) HTTP
     - AAC
     - WebM/MKV
     - FLV
     - H264
     - HDS
     - TS
     - JSON
     - MP4
     - MP3
     - OGG
     - SubRip/WebVTT
     - WAV
   - DTSC
   - TS over TCP
   - TS over SRT
   - Utility: Static HTTPS File Server

  
<br>

### 4. *Logging*
---

![Logging Levels](assets/Logging_levels.png)
![API for logging](assets/Log_api.png)

   - (Under MistAnalyzer)
   - 10 Verosity Levels.
   - Full reboot is required after changing verbosity levels.
   - Can be set under "Overview" panel, or using "log" api while requesting.

<br>

### 5. *Wildcard Push Inputs*
---

   - Mist has extensive support for wildcards, Push input being a highlighted use case.
   - dtsc://host[:port][/streamname[+wildcard]]
   - rtsp://myaccount:mypassword@1.2.3.4:5678/videoMain


<br>

### 6. *Integrations*
---

   - Eg - http://localhost:4242/api?commands={"addstream":{"test1":{"source":"rtsp://android:stackqueue@35.207.248.73:1935/live/BerkowitsAsrao11.stream","always_on":true}}}
   - API (42)
     - Authentication
     - AddStream
     - DeleteStream
     - Config
     - Active_Streams
     - Stats_Streams
     - Push_Start
     - Push_List
     - Push_Stop
     - ...
   - HTTP output info handler
   - Prometheus Intrumentation
  
<br>

### 7. *Triggers*
---

![Triggers](assets/Triggers.png)

   - "If a trigger is _triggered_, do some action"
   - May be handled by a URL or an executable.
   - As URL:
     - POST request is sent to the URL with an extra X-Trigger header containing trigger name and payload as body.
   - As Executable:
     - Executable is started with the trigger name as its onlyargument, and the payload is piped into the executable over standard input.
   
   - "Handler" : The handler URL or executable.
   - "Nonblocking" : Variable is a boolean true (blocking) or false (non-blocking). 
      - (Note that non-blocking executable triggers will not have anything connected to standard output, 
         which in the case of bash scripts will mean that they abort as soon as you try to echo anything.)


8. *HTTP output info handler*

   - The various outputs can retrieve this information from the inputs.
      A. JSON format stream information
         (http://localhost:4242/json_STREAMNAME.js)

<br>
<br>

---
---
<br>

> https://github.com/DDVTECH/mistserver/
>
> [DTSH](https://news.mistserver.org/news/76/DTSC%3A+MistServer%27s+internal+media+format)
> 
> [What Does a Push/Streaming API Look Like?](https://www.programmableweb.com/news/what-does-pushstreaming-api-look/research/2018/05/24#:~:text=Push%2FStreaming%20APIs%20are%20event,that's%20waiting%20for%20such%20updates.)

<br>

---
---
## Push input for live streams

---

If you plan to push a stream towards the server through RTMP (or RTSP), you’ll want to configure the source as:

> ` push://[host][@passphrase] `

Both the source host and the passphrase are optional. An incoming push will have to match at least one of the two to be allowed push access to the server, as well as the stream name.

The [host] may include a subnet mask, in CIDR notation (e.g. 192.168.0.0/16 will allow the complete 192.168.X.Y range to push). This even works with hostnames, but be aware the same CIDR mask will apply both to IPv4 and IPv6 if your hostname has records both address types!

Some examples:

* push:// will allow anyone to push to the given stream name, without any host or password
checking.
* push://127.0.0.1 will allow only localhost to push to the given stream name.
* push://@123abc will allow only users passing on the passphrase “123abc” to push to the
given stream name.
* push://127.0.0.1@123abc will allow localhost without a passphrase, and all other hosts with the passphrase to push to the given stream name.
* Once set up, you can push over the RTMP protocol using the following RTMP URL:
rtmp://hostname:port/passphrase/streamname
* The passphrase may be filled with any value (including leaving it empty) if not used. The section “rtmp://hostname:port/passphrase” is often referred to in RTMP broadcasting software as the “application URL” while the streamname is usually referred to as either the stream name or the stream key in RTMP broadcasting software. If port 1935 is used it may be left out.

Pushing over RTSP is also possible, using the URL:

> `rtsp://hostname:port/streamname?pass=passphrase`

The same guidelines and behaviour as for RTMP pushing apply.

If port 554 is used it may be left out.


<br>
<br>

### Basics
---
> 1. **ADD STREAM**
> ---

>> Source = push://(ip)(@passphrase)
Both ip and passphrase optional

>>> Method A = Using panel

>>> Method B = Using API calls 


<br>

---
> 2. **PUSH TO OTHER STREAM**
> ---

>> Add process = target = "the push url"


<br>

---
> 3. **LOGS**

>> Method A = Using panel

>> Method B = Using API calls 

>> Method C = /etc/mistserver.log


<br>

---
> 4. **CONFIG**

>> Method A = Using panel

>> Method B = Using API calls 

>> Method C = /var/mistserver.log

<br>
<br>


### Push to an empty push RTSP URL -
---
> After creating a new stream...
>
> ...
>
>> `ffmpeg -y -noautorotate -re -stream_loop -1 -i rtsp://android:stackqueue@35.207.248.73:1935/live/BerkowitsAsrao11.stream -codec copy -f rtsp -rtsp_transport tcp rtsp://localhost:5554/test_ffmp`
>
> ...
>
>> `ffmpeg -re -i /home/aanisnoor/Videos/sample.mp4 -f rtsp -c:v libx264 -c:a aac rtsp://localhost:5554/test_ffmp`
>
> ...
>
>> `ffmpeg -re -stream_loop -1 -i ndvr/DVR\ Recordings\ \ JARVIS\ \(39\).mp4 -codec copy -f rtsp -rtsp_transport tcp rtsp://10.160.0.18:1935/live/MGD.stream`
> 
> ...
> 
>> lib/processors/process_offline_stream.py


---

<br>

### Existing model - panel_videorecording -
---

![panel_viewrecording](assets/panel_viewrecording.png)
       


"dvr_status" is fetched using "fetch_required_timeline()" which uses nimble api to return such data.

<br>

### How nimble stores recordings -
---

![nimble_storage_structure](assets/nimble_storage.png)

<br>