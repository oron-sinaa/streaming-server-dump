MistServer build
================

> git clone --branch mbedtls-dev https://github.com/gizahNL/mistserver.git

> cd mistserver

> sudo apt -y install libsrtp2-dev

> sudo apt -y install doxygen

> mkdir build ; cd build

> sudo apt install srt-tools

> sudo apt --fix-broken

> sudo apt install srt-tools

> [ Replace meson_options.txt (from this folder) ]

> meson ..

> ninja

> sudo ninja install
