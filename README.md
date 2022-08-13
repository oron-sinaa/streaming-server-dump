# streaming-server-dump

Here I put all the things I learnt or built about RTSP servers.


## Resources

> https://www.wowza.com/blog/streaming-protocols

> https://www.wowza.com/blog/rtsp-the-real-time-streaming-protocol-explained

> https://gstreamer.freedesktop.org/documentation/gst-rtsp-server/rtsp-server.html?gi-language=c

> http://live555.com/


## TCP vs UDP

> "Because UDP doesn’t support retransmissions, packet ordering, or error-checking, there’s potential for a network glitch to corrupt the data en route"

whereas,

> "TCP requires a three-way handshake when transporting data. The initiator (client) asks the accepter (server) to start a connection, the accepter responds, and the initiator acknowledges the response and maintains a session between either end"

> ![tcp VS UDP](https://user-images.githubusercontent.com/38424838/184505080-66984f98-c0ea-40ee-b6e6-481e92f79475.png)


## Miscellaneous

> ![OSI Model with units](https://user-images.githubusercontent.com/38424838/184504861-4932db92-ebce-40c1-94ab-b37326bb0c59.png)

> ![image](https://user-images.githubusercontent.com/38424838/184505293-99fcf542-4dd5-471b-a699-4c7386af1e9f.png)

>
