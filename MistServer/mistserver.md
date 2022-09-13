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


1. *The Calculators*

   - [Hardware Requirements + Server Capabilities](https://news.mistserver.org/news/85/What+hardware+do+I+need+to+run+MistServer%3F)
  

2. *Embeds*

   - Generate and display the HTML code to embed a player onto a website.
   - Embedded player automatically detects stream settings & browser/device capabilities and for optimal playback.
   - Use a different host - Change the host in the embeddable url/codes in case the host used to connect to the web interface can not be used on the target website
   - URLs - (Stream info json/script)
   - Embed code
   - Embed code options (optional)
   - Protocol stream urls (generated based on available codecs in the stream and enabled protocols)


3. *Supported Protocols*

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


4. *Logging*

![Logging Levels](assets/Logging_levels.png)
![API for logging](assets/Log_api.png)

   - (Under MistAnalyzer)
   - 10 Verosity Levels.
   - Full reboot is required after changing verbosity levels.
   - Can be set under "Overview" panel, or using "log" api while requesting.



5. *Wildcard Push Inputs*

   - Mist has extensive support for wildcards, Push input being a highlighted use case.
   - dtsc://host[:port][/streamname[+wildcard]]
   - rtsp://myaccount:mypassword@1.2.3.4:5678/videoMain


6. *Integrations*

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


7. *Triggers*

[Triggers](assets/Triggers.png)

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
      C. 


9.  *The Meta Players*





> https://github.com/DDVTECH/mistserver/
>
> [DTSH](https://news.mistserver.org/news/76/DTSC%3A+MistServer%27s+internal+media+format)
> 
> [What Does a Push/Streaming API Look Like?](https://www.programmableweb.com/news/what-does-pushstreaming-api-look/research/2018/05/24#:~:text=Push%2FStreaming%20APIs%20are%20event,that's%20waiting%20for%20such%20updates.)
