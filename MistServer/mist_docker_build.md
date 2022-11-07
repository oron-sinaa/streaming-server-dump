## Clone Catalyst branch Mistserver =

> git clone -b catalyst https://github.com/DDVTECH/mistserver.git


### (Make any required edits in the source files)


## Building for raspberry pi =

> Edit dockerfile (under catalyst)
> 
> FROM balenalib/raspberry-pi


## Building with docker =

> docker login -u $DOCKERHUB_USERNAME -p $DOCKERHUB_PASSWORD

> `docker buildx build --progress=plain --target=mist --build-arg BUILD_TARGET=static --build-arg STRIP_BINARIES=true --build-arg BUILD_VERSION=e064f8951738fc89605844891605e1150dd636b6 --tag livepeerci/mistserver:static-catalyst-amd64 --tag livepeerci/mistserver:static-e064f8951738fc89605844891605e1150dd636b6-amd64 --tag livepeerci/mistserver:static-e064f895-amd64 --tag livepeerci/mistserver:static-e064f8951738fc89605844891605e1150dd636b6-amd64 --tag livepeerci/mistserver:static-latest-amd64 --push .`



## Run with docker =

> sudo docker run docker.io/livepeerci/mistserver:static-catalyst-amd64
