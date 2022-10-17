MistServer build
================

<br>

### Clone this forked branch of mistserver -
---
> git clone --branch mbedtls-dev https://github.com/gizahNL/mistserver.git

> cd mistserver

<br>

### Install dependencies and tools -
---
> sudo apt -y install build-essential

> sudo apt -y install libsrtp2-dev

> sudo apt -y install doxygen

> pip3 install meson

> pip3 install ninja

> mkdir build ; cd build

> sudo apt install srt-tools
> sudo apt --fix-broken
> sudo apt install srt-tools

<br>

### Build options -
---
> [ Replace meson_options.txt (from this folder) ]

<br>

### Build and install-
---
> meson ..

> ninja

> sudo ninja install
