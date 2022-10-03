# OvenMediaEngine

<br>

## Links
---

> https://airensoft.gitbook.io/ovenmediaengine/
> 
> https://github.com/AirenSoft/OvenMediaEngine

<br>

## Supported Platforms
---

Platforms listed below. However, we think it can work with other Linux packages as well:

- Docker
- Ubuntu 18+
- CentOS 7+
- Fedora 28+

<br>

## Installation
---

> docker run -d \
> -p 1935:1935 -p 4000:4000/udp -p 3333:3333 -p 3334:3334 -p 3478:3478 -p 9000:9000 -p 9999:9999/udp \
> airensoft/ovenmediaengine:0.14.9

## Configuration
---

To save config to local storage from the container: 

> docker run -d \
> -p 1935:1935 \
> -p 3333:3333 \
> -p 3334:3334 \
> -p 3478:3478 \
> -p 9000:9000 \
> -p 9999:9999/udp \
> -p 4000:4000/udp \
> -v ome-origin-conf:/opt/ovenmediaengine/bin/origin_conf \
> -v ome-edge-conf:/opt/ovenmediaengine/bin/edge_conf \
> --name ovenmediaengine \
> airensoft/ovenmediaengine:latest


Access under /var/lib/docker/volumes/ome-origin-conf/_data :

> Logger.xml  
> Server.id  
> Server.xml

<br>

Configuration can be accessed under -
> `/var/lib/docker/volumes/[volume_name]/_data`

#### Using the above -
> - `/var/lib/docker/volumes/ome-origin-conf/_dat/var/lib/docker/volumes/ome-origin-conf/_data`
> 
> - `/var/lib/docker/volumes/ome-edge-conf/_data`

<br>

#### If you want to put them in a different location, the easiest way is to create a link:
> ln -s /var/lib/docker/volumes/ome-origin-conf/_data/ /my/new/path/to/ome-origin-conf \
> && ln -s /var/lib/docker/volumes/ome-edge-conf/_data/ /my/new/path/to/ome-edge-conf

<br>

#### If you start OvenMediaEngine with systemctl start ovenmediaengine, the config file is loaded from the following path.
> /usr/share/ovenmediaengine/conf/Server.xml

<br>

#### If you run it directly from the command line, it loads the configuration file from:
> /[OvenMediaEngine Binary Path]/conf/Server.xml

<br>

#### If you run it in Docker container, the path to the configuration file is:
> **For Origin mode**
/opt/ovenmediaengine/bin/origin_conf/Server.xml

> **For Edge mode**
/opt/ovenmediaengine/bin/edge_conf/Server.xml

<br>

## Server
---

> The Server is the root element of the configuration file.
> 
> The versionattribute indicates the version of the configuration file.
>
> OvenMediaEngine uses this version information to check if the config file is a compatible version.

```
<?xml version="1.0" encoding="UTF-8"?>
<Server version="8">
    <Name>OvenMediaEngine</Name>
    <IP>*</IP>
    <PrivacyProtection>false</PrivacyProtection>
    <StunServer>stun.l.google.com:19302</StunServer>
    <Bind>...</Bind>
    <VirtualHosts>...</VirtualHosts>
</Server>
```

## Bind
---

```
> The Bind is the configuration for the server port that will be used.
> Bind consists of Providers and Publishers.
> The Providers are the server for stream input, and the Publishers are the server for streaming.
```

> `https://airensoft.gitbook.io/ovenmediaengine/configuration#bind`


## Virtual Hosts
---

> `https://airensoft.gitbook.io/ovenmediaengine/configuration#virtual-host`