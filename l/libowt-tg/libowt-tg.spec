%def_enable internal_absl

# Dynamic build is not supported by upstream
%def_enable static

%def_disable pipewire

Name: libowt-tg
Version: 4.3.0.10
Release: alt6

Summary: Open WebRTC Toolkit with Telegram desktop patches

License: Apache-2.0
Group: System/Libraries
Url: https://github.com/desktop-app/tg_owt

# Source-url: https://github.com/desktop-app/tg_owt/archive/master.zip
Source: %name-%version.tar

# Source1-url: https://github.com/cisco/libsrtp/archive/refs/tags/v2.5.0.tar.gz
Source1: %name-libsrtp-%version.tar

# Source2-url: https://github.com/abseil/abseil-cpp/archive/refs/tags/20230125.3.tar.gz
Source2: %name-abseil-cpp-%version.tar

Patch1: 0011-cmake-external.cmake-add-link_libyuv-function.patch
Patch2: 0012-cmake-libwebrtcbuild.cmake-add-tg_owt-libyuv-only-if.patch
Patch3: 0013-CMakeLists.txt-use-external-libyuv.patch
Patch4: 0014-CMakeLists.txt-don-t-include-cmake-rules-for-externa.patch

Patch2000: %name-e2k.patch

BuildRequires(pre): rpm-macros-cmake

BuildRequires: libalsa-devel
BuildRequires: libXtst-devel libXcomposite-devel libXdamage-devel libXrender-devel libXrandr-devel
BuildRequires: libavformat-devel libswresample-devel libswscale-devel
BuildRequires: libdb4-devel libjpeg-devel libopus-devel libpulseaudio-devel libssl-devel yasm
BuildRequires: libprotobuf-devel protobuf-compiler
BuildRequires: libgio-devel

%if_disabled internal_absl
BuildRequires: libabseil-cpp-devel >= 20211102.0
%endif
BuildRequires: libopenh264-devel
#BuildRequires: libusrsctp-devel
BuildRequires: libvpx-devel >= 1.10.0
%if_enabled pipewire
BuildRequires: pipewire-libs-devel
%endif
#BuildRequires: libsrtp2-devel >= 2.5.0
BuildRequires: libyuv-devel >= 0.0.1874
BuildRequires: libcrc32c-devel

# TODO remove epoxy
BuildRequires: libgbm-devel libdrm-devel libepoxy-devel

# Just disable noise (cmake TODO https://gitlab.kitware.com/cmake/cmake/-/issues/18158):
# Package 'libpcre', required by 'glib-2.0', not found
# Package libpcre was not found in the pkg-config search path.
BuildRequires: libpcre-devel
# Just to disable noise like Package 'libffi', required by 'gobject-2.0', not found
BuildRequires: libffi-devel

BuildRequires: gcc-c++ cmake ninja-build

# TODO: enable logging and debugging
#add_optflags -DRTC_DISABLE_LOGGING=1

%if_disabled static
%add_optflags -fPIC
%endif

#if_enabled static
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
#endif
%global optflags_lto -ffat-lto-objects
%add_optflags -ffat-lto-objects

# https://github.com/desktop-app/tg_owt/issues/106
# NDEBUG or DCHECK_ALWAYS_ON enable RTC_DCHECK_ON
%add_optflags -DNDEBUG

%ifarch %ix86
%add_optflags -msse2 -mfpmath=sse
# verify-elf: ERROR: ./usr/lib/libtg_owt.so.0.0.0: TEXTREL entry found: 0x0000000
%set_verify_elf_method textrel=relaxed
%endif

%description
Open WebRTC Toolkit with Telegram desktop patches.

WebRTC is an open source project that enables web browsers with Real-Time
Communications (RTC) capabilities via simple Javascript APIs. The WebRTC
components have been optimized to best serve this purpose.
WebRTC implements the W3C's proposal for video conferencing on the web.

%package devel
Summary: Open WebRTC Toolkit library and header files
Group: Development/C++
%if_disabled static
Requires: %name = %EVR
%endif
Requires: libjpeg-devel libopus-devel
Requires: libvpx-devel
Requires: libyuv-devel
#Requires: libsrtp2-devel


%description devel
%name-devel contains the libraries and header files needed to
develop programs which make use of %name.

%prep
%setup -a1 -a2
%patch1 -p2
%patch2 -p2
%patch3 -p2
%patch4 -p2
%ifarch %e2k
%patch2000 -p2
%endif

# TODO (used in cmake checks):
rm -rv src/third_party/openh264
rm -rv src/third_party/libyuv
rm -rv src/third_party/crc32c
rm -v cmake/libopenh264.cmake
rm -v cmake/libyuv.cmake
rm -v cmake/libcrc32c.cmake
rm -rfv src/base/android/

# stop using direct path lib libyuv headers (TODO: move to the libyuv patch?)
find -type f -name "*.cc" | xargs subst 's|third_party/libyuv/include/||'
# stop using embedded srtp2
#find -type f -name "*.h" | xargs subst 's|third_party/libsrtp/crypto/include/|srtp2/|'
#find -type f -name "*.h" | xargs subst 's|third_party/libsrtp/include/|srtp2/|'
#find -type f -name "*.cc" | xargs subst 's|third_party/libsrtp/include/|srtp2/|'

# not used, pulls in excessive deps
sed -i '/absl\/strings\/cord.cc/d' cmake/libabsl.cmake

%build
%cmake_insource \
          -DCMAKE_BUILD_TYPE=RelWithDebInfo \
          -DBUILD_SHARED_LIBS:BOOL=OFF \
          -DTG_OWT_PACKAGED_BUILD:BOOL=ON \
          -DCMAKE_POSITION_INDEPENDENT_CODE:BOOL=ON \
          -DTG_OWT_USE_PROTOBUF:BOOL=ON \
%if_enabled pipewire
          -DTG_OWT_USE_PIPEWIRE:BOOL=ON \
%else
          -DTG_OWT_USE_PIPEWIRE:BOOL=OFF \
%endif
          %nil
%make_build VERBOSE=1

%install
%makeinstall_std
rm -rv %buildroot%_includedir/tg_owt/sdk/{objc,android}/
rm -rv %buildroot%_includedir/tg_owt/modules/audio_device/android

%if_disabled internal_absl
rm -rv %buildroot%_includedir/tg_owt/third_party/abseil-cpp/
%endif

rm -rv %buildroot%_includedir/tg_owt/third_party/libvpx
rm -rv %buildroot%_includedir/tg_owt/third_party/{yasm,pffft,rnnoise}

%if_disabled static
%files
%_libdir/libtg_owt.so.*
%endif

%files devel
%_includedir/tg_owt/
%if_disabled static
%_libdir/libtg_owt.so
%else
%_libdir/libtg_owt.a
%endif
%_libdir/cmake/tg_owt/

%changelog
* Wed Aug 02 2023 Vitaly Lipatov <lav@altlinux.ru> 4.3.0.10-alt6
- remove Obsoletes: %name from devel subpackage (ALT bug 47099)

* Wed Aug 02 2023 Vitaly Lipatov <lav@altlinux.ru> 4.3.0.10-alt5
- new version (4.3.0.10) with rpmgs script
- build from git a45d8b8f0a99bd0e5118dda1dc4a8b7b3ad5dcfd
- build without pipewire support (possible crash source)
- build static only lib
- drop out embedded crc32c
- pack third party libsrtp2, abseil-cpp 
- build with embedded abseil-cpp
- build with -DNDEBUG

* Thu Apr 27 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.3.0.7-alt2
- rebuilt on all arches

* Wed Jun 15 2022 Vitaly Lipatov <lav@altlinux.ru> 4.3.0.7-alt1
- new version (4.3.0.7) with rpmgs script
- build from git 10d5f4bf77333ef6b43516f90d2ce13273255f41
- removed BR: usrsctp
- pack third party crc32c

* Sun Apr 10 2022 Vitaly Lipatov <lav@altlinux.ru> 4.3.0.6-alt1
- new version (4.3.0.6) with rpmgs script
- build from git 1fe5e68d999e0bf88d0128ad813438726732f6e0
- remove third_party headers from includedir
- stop build for aarch64 (due strange linking issues with abseil-cpp)

* Fri Sep 17 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 4.3.0.5-alt4
- added patch for Elbrus

* Thu Jul 08 2021 Vitaly Lipatov <lav@altlinux.ru> 4.3.0.5-alt3
- don't pack symlink

* Sun Jul 04 2021 Vitaly Lipatov <lav@altlinux.ru> 4.3.0.5-alt2
- build with external libyuv, libvpx, libusrsctp, libopenh264

* Sun Jun 27 2021 Vitaly Lipatov <lav@altlinux.ru> 4.3.0.5-alt1
- new version (4.3.0.5) with rpmgs script
- build from git f03ef05abf665437649a4f71886db1343590e862

* Mon Feb 01 2021 Vitaly Lipatov <lav@altlinux.ru> 4.3.0.4-alt1
- new version (4.3.0.4) with rpmgs script
- build from git be23804afce3bb2e80a1d57a7c1318c71b82b7de
- build with bundled libyuv ad890067f661dc747a975bc55ba3767fe30d4452
- build with bundled libvpx 5b63f0f821e94f8072eb483014cfc33b05978bb9

* Sat Dec 05 2020 Vitaly Lipatov <lav@altlinux.ru> 4.3.0.3-alt3
- build from git 75ac66937341d8a9207375aaee79b4bdc500146c
- build shared lib

* Sun Nov 01 2020 Vitaly Lipatov <lav@altlinux.ru> 4.3.0.3-alt2
- fix build

* Fri Oct 30 2020 Vitaly Lipatov <lav@altlinux.ru> 4.3.0.3-alt1
- build from git 1d4f7d74ff1a627db6e45682efd0e3b85738e426
- pack as usual static lib with cmake module

* Thu Sep 10 2020 Vitaly Lipatov <lav@altlinux.ru> 4.3.0.2-alt1
- build from git ceef372ff87c1b6b9ab925cb30ccd00388f8fe73
- build with bundled libvpx

* Sat Sep 05 2020 Vitaly Lipatov <lav@altlinux.ru> 4.3.0.1-alt1
- build from git a4d3a58afda96b4e92426fb464f644205e07acae
- temp. exclude armh arch

* Sat Aug 22 2020 Vitaly Lipatov <lav@altlinux.ru> 4.3-alt1
- build OWT patched for Telegram Desktop
