MistServer build (--branch catalyst)
====================================

(https://drone.livepeer.fish/DDVTECH/mistserver/341/13/1)


<br>

DEPENDENCIES
---

> git init

> git remote add origin https://github.com/DDVTECH/mistserver.git

> git fetch  origin +refs/heads/catalyst:

> git checkout e064f8951738fc89605844891605e1150dd636b6 -b catalyst

> set -e

> export CI_PATH="$(realpath ..)"

> git clone https://github.com/cisco/libsrtp.git $CI_PATH/libsrtp

> git clone -b dtls_srtp_support --depth=1 https://github.com/livepeer/mbedtls.git $CI_PATH/mbedtls

> git clone https://github.com/Haivision/srt.git $CI_PATH/srt

> mkdir -p $CI_PATH/libsrtp/build $CI_PATH/mbedtls/build $CI_PATH/srt/build $CI_PATH/compiled

> cd $CI_PATH/libsrtp/build/ && cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=$CI_PATH/compiled .. && make -j $(nproc) install

> export PKG_CONFIG_PATH="$CI_PATH/compiled/lib/pkgconfig" && export LD_LIBRARY_PATH="$CI_PATH/compiled/lib" && export C_INCLUDE_PATH="$CI_PATH/compiled/include"

> cd $CI_PATH/mbedtls/build/ && cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=$CI_PATH/compiled .. && make -j $(nproc) install VERBOSE=1

> cd $CI_PATH/srt/build/ && cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=$CI_PATH/compiled -DCMAKE_PREFIX_PATH=$CI_PATH/compiled -DUSE_ENCLIB=mbedtls -DENABLE_SHARED=false .. && make -j $(nproc) install

> exit

<br>

BINARIES
---

> cd mistserver [ROOT/mistserver]

> export CI_PATH="$(realpath ..)"

> export PKG_CONFIG_PATH="$CI_PATH/compiled/lib/pkgconfig" && export LD_LIBRARY_PATH="$CI_PATH/compiled/lib" && export C_INCLUDE_PATH="$CI_PATH/compiled/include"

> mkdir -p build/ && echo e064f8951738fc89605844891605e1150dd636b6 | tee build/BUILD_VERSION

> cd build && cmake -DDEBUG=3 -DPERPETUAL=1 -DLOAD_BALANCE=1 -DNOLLHLS=1 -DCMAKE_INSTALL_PREFIX="$CI_PATH" -DCMAKE_PREFIX_PATH="$CI_PATH/compiled" -DCMAKE_BUILD_TYPE=RelWithDebInfo -DNORIST=yes -DNOLLHLS=1 ..


<br>

COMPRESS
---

> cd mistserver [ROOT/mistserver]

> export CI_PATH="$(realpath ..)"

> cd $CI_PATH/bin/

> tar -czvf livepeer-mistserver-linux-amd64.tar.gz ./*

<br>

UPLOAD
---

> scripts/upload_build.sh -d "$(realpath ..)/bin" "livepeer-mistserver-linux-amd64.tar.gz"
