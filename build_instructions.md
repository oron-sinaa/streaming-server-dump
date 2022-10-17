MistServer build
================

> git clone --branch mbedtls-dev https://github.com/gizahNL/mistserver.git

> cd mistserver

> sudo apt -y install libsrtp2-dev

> sudo apt -y install doxygen

> mkdir build ; cd build

> meson ..

> ninja

> sudo ninja install
