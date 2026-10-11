Name: libmegasdk
Version: 10.19.0
Release: alt1

Summary: MEGA SDK - Client Access Engine

License: BSD-2-Clause
Group: System/Libraries
Url: https://github.com/meganz/sdk

# Source-url: https://github.com/meganz/sdk/archive/v%version.tar.gz
Source: v%version.tar.gz

# The SDK has no stable ABI: the soname changes with every minor release
%define abiversion %(echo %version | cut -d. -f1-2)

# Upstream builds only a static in-tree library: build it shared and install it
Patch1: libmegasdk-10.19.0-shared-library.patch
Patch2: libmegasdk-10.19.0-install.patch
Patch3: libmegasdk-10.19.0-qt-bindings-install.patch
Patch4: libmegasdk-10.19.0-no-stdc++fs.patch
Patch5: libmegasdk-10.19.0-direct-deps.patch

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildRequires(pre): rpm-build-cmake
BuildRequires: gcc-c++ qt5-base-devel
BuildRequires: libcryptopp-devel libsodium-devel libsqlite3-devel libcurl-devel libssl-devel libicu-devel
BuildRequires: libuv-devel libfreeimage-devel libmediainfo-devel libzen-devel libreadline-devel
# libmediainfo.pc refers to glib-2.0 includes
BuildRequires: glib2-devel
BuildRequires: zlib-devel
BuildRequires: libavformat-devel libavcodec-devel libavutil-devel libswscale-devel libswresample-devel

%description
MEGA SDK - Client Access Engine.

MEGA --- The Privacy Company --- is a Secure Cloud Storage provider
that protects your data thanks to end-to-end encryption.
We call it User Controlled Encryption, or UCE, and all our clients automatically manage it.

All files stored on MEGA are encrypted. All data transfers from and to MEGA are encrypted.
And while most cloud storage providers can and do claim the same,
MEGA is different - unlike the industry norm where the cloud storage provider holds the decryption key,
with MEGA, you control the encryption, you hold the keys, and you decide who you grant or deny access to your files.

%package -n libmega%abiversion
Summary: MEGA SDK shared library
Group: System/Libraries

%description -n libmega%abiversion
MEGA SDK - Client Access Engine shared library.

%package -n libmega-qt%abiversion
Summary: Qt5 bindings for MEGA SDK shared library
Group: System/Libraries

%description -n libmega-qt%abiversion
Qt5 bindings for MEGA SDK - Client Access Engine shared library.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: libmega%abiversion = %EVR
Requires: libmega-qt%abiversion = %EVR
# the exported CMake targets include MEGA::gfxworker
Requires: %name-gfxworker = %EVR
Provides: %name-devel-qt5 = %EVR
Obsoletes: %name-devel-qt5 < %EVR

%description devel
This package contains the headers, pkg-config and CMake files necessary
for developing with %name (including the Qt5 bindings).

%package gfxworker
Summary: MEGA SDK isolated graphics processing helper
Group: Graphics

%description gfxworker
Helper process used by MEGA SDK based applications to create thumbnails
and previews in a separate process.

%package tools
Summary: Tools from MEGA SDK
Group: File tools

Conflicts: megafuse

%description tools
Example tools from MEGA SDK - Client Access Engine
* megacli (a powerful command line tool that allows to use all SDK features)

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DBUILD_SHARED_LIBS=ON \
    -DSDKLIB_INSTALL=ON \
    -DCMAKE_INSTALL_LIBEXECDIR=%_libexecdir \
    -DSDKLIB_OUTPUT_NAME=mega \
    -DSDKQTBINDINGS_OUTPUT_NAME=mega-qt \
    -DENABLE_SDKLIB_WERROR=OFF \
    -DENABLE_SDKLIB_TESTS=OFF \
    -DENABLE_SDKLIB_EXAMPLES=ON \
    -DENABLE_QT_BINDINGS=ON \
    -DENABLE_ISOLATED_GFX=ON \
    -DENABLE_LOG_PERFORMANCE=ON \
    -DENABLE_MEDIA_FILE_METADATA=ON \
    -DUSE_LIBUV=ON \
    -DUSE_FREEIMAGE=ON \
    -DUSE_FFMPEG=ON \
    -DUSE_PDFIUM=OFF \
    -DUSE_READLINE=ON \
    %nil
%cmake_build

%install
%cmake_install

%files -n libmega%abiversion
%_libdir/libmega.so.%abiversion
%_libdir/libmega.so.%version

%files -n libmega-qt%abiversion
%_libdir/libmega-qt.so.%abiversion
%_libdir/libmega-qt.so.%version

%files devel
%_includedir/megasdk/
%_libdir/libmega.so
%_libdir/libmega-qt.so
%_libdir/pkgconfig/sdklib.pc
%_libdir/cmake/sdklib/

%files gfxworker
%dir %_libexecdir/megasdk/
%_libexecdir/megasdk/gfxworker

%files tools
%_bindir/megacli

%changelog
* Sun Oct 11 2026 Vitaly Lipatov <lav@altlinux.ru> 10.19.0-alt1
- new version 10.19.0 (CMake build)
- build SDKlib as shared libmega.so.10.19 (the ABI changes every minor release)
- pack libmega10.19 and libmega-qt10.19 (Qt5 bindings) per Shared Libs Policy
- install headers (into /usr/include/megasdk), pkg-config and CMake package files
- pack gfxworker helper into libmegasdk-gfxworker subpackage
- drop libmegasdk-devel-qt5 (the Qt5 bindings are in libmegasdk-devel now)
- megasimplesync is dropped by upstream

* Tue Nov 07 2023 Vitaly Lipatov <lav@altlinux.ru> 4.28.3-alt1
- new version 4.28.3 (with rpmrb script)

* Tue Sep 15 2020 Vitaly Lipatov <lav@altlinux.ru> 3.7.3b-alt1
- new version 3.7.3b (with rpmrb script)

* Sun Mar 08 2020 Vitaly Lipatov <lav@altlinux.ru> 3.6.8-alt1
- new version 3.6.8

* Wed Apr 10 2019 Fr. Br. George <george@altlinux.ru> 3.4.9-alt1
- Autobuild version bump to 3.4.9

* Sun Nov 25 2018 Vitaly Lipatov <lav@altlinux.ru> 3.4.3-alt1
- new version 3.4.3 (with rpmrb script)

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 3.4.0-alt1.1
- NMU: Rebuild with new openssl 1.1.0.

* Wed Aug 15 2018 Fr. Br. George <george@altlinux.ru> 3.4.0-alt1
- Autobuild version bump to 3.4.0

* Sat Jun 09 2018 Vitaly Lipatov <lav@altlinux.ru> 3.3.8-alt1
- new version 3.3.8 (with rpmrb script)
- rebuild with libcryptopp-6.1.0

* Mon Feb 12 2018 Vitaly Lipatov <lav@altlinux.ru> 3.2.8-alt3.1
- NMU: autorebuild with libsodium-1.0.16

* Sat Dec 23 2017 Vitaly Lipatov <lav@altlinux.ru> 3.2.8-alt3
- pack m4 subdir
- pack missed mega_glob.h, mega_http_parser.h

* Sat Dec 23 2017 Vitaly Lipatov <lav@altlinux.ru> 3.2.8-alt2
- build devel-qt5 subpackage with qt binding
- build with all possible libs

* Fri Dec 22 2017 Vitaly Lipatov <lav@altlinux.ru> 3.2.8-alt1
- rename source package, cleanup spec
- new version (3.2.8), change packager

* Sat Dec 09 2017 Vitaly Lipatov <lav@altlinux.ru> 2.5.0-alt1.3
- NMU: autorebuild with libcryptopp-5.6.5

* Wed Jul 05 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.5.0-alt1.2
- Updated build dependencies

* Tue Aug 18 2015 Danil Mikhailov <danil@altlinux.org> 2.5.0-alt3
- added two new packages libmegasdk and libmegasdk-devel

* Thu Aug 13 2015 Danil Mikhailov <danil@altlinux.org> 2.5.0-alt2
- fix bugs with /bin/sh in mss-serv, added $ to CONFIG var
- remove megafuse, use megafuse package

* Sat Jul 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.0-alt1.1
- Rebuilt with gcc5

* Mon May 25 2015 Danil Mikhailov <danil@altlinux.org> 2.5.0-alt1
- initial build for ALT Linux Sisyphus
