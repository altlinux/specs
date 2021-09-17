Name: libowt-tg
Version: 4.3.0.5
Release: alt4

Summary: Open WebRTC Toolkit with Telegram desktop patches

License: Apache-2.0
Group: System/Libraries
Url: https://github.com/desktop-app/tg_owt

# Source-url: https://github.com/desktop-app/tg_owt/archive/master.zip
Source: %name-%version.tar

Patch5: ad47b06841f36702ec6ce4d8609ce358c5155cbf.patch
Patch6: c22f796fe1eb6b37f8f891068941bb0e6e19f6cb.patch
Patch2000: %name-e2k.patch

ExcludeArch: armh ppc64le

BuildRequires: libalsa-devel
BuildRequires: libXtst-devel libXcomposite-devel libXdamage-devel libXrender-devel libXrandr-devel
BuildRequires: libavformat-devel libswresample-devel libswscale-devel
BuildRequires: libdb4-devel libjpeg-devel libopus-devel libpulseaudio-devel libssl-devel yasm
BuildRequires: libprotobuf-devel protobuf-compiler
BuildRequires: libgio-devel

# instead of third party
# FIXME:
# on aarch64 missed libs during linking:
# verify-elf: ERROR: ./usr/lib64/libtg_owt.so.0.0.0: undefined symbol: _ZN4absl12lts_2021032414ascii_internal13kPropertyBit
#BuildRequires: libabseil-cpp-devel
BuildRequires: libusrsctp-devel libopenh264-devel
BuildRequires: libvpx-devel >= 1.10.0
BuildRequires: pipewire-libs-devel
BuildRequires: libevent-devel
BuildRequires: libyuv-devel
# TODO: libsrtp2-devel

BuildRequires: gcc-c++ cmake ninja-build

#add_optflags -D_FILE_OFFSET_BITS=64
# TODO: enable logging and debugging
#add_optflags -DRTC_DISABLE_LOGGING=1

%add_optflags -fPIC

%ifarch %ix86
%add_optflags -msse2 -mfpmath=sse
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
Requires: %name = %EVR
Requires: libjpeg-devel libopus-devel
Requires: libvpx-devel
Requires: libyuv-devel


%description devel
%name-devel contains the libraries and header files needed to
develop programs which make use of %name.

%prep
%setup
%patch5 -p1
%patch6 -p1
%ifarch %e2k
%patch2000 -p2
%endif
rm -rfv src/third_party/{libvpx,openh264,pipewire,usrsctp} src/base/third_party/libevent/
rm -fv cmake/{libvpx,libopenh264,libusrsctp,libevent,libyuv}.cmake
rm -rfv src/base/android/

# FIXME: fix direct include paths (used in telegram build too)
mkdir -p src/third_party/libyuv/include
cp %_includedir/libyuv.h src/third_party/libyuv/include/libyuv.h
cp -a %_includedir/libyuv/ src/third_party/libyuv/include


%build
%ifarch %ix86 x86_64 %arm
export CFLAGS="$RPM_OPT_FLAGS -fPIC"
%endif
%cmake_insource \
          -DCMAKE_BUILD_TYPE=RelWithDebInfo \
          -DBUILD_SHARED_LIBS:BOOL=ON \
          -DTG_OWT_PACKAGED_BUILD:BOOL=ON \
          -DCMAKE_POSITION_INDEPENDENT_CODE:BOOL=ON \
          -DTG_OWT_USE_PROTOBUF:BOOL=ON \
%ifarch %ix86
          -DCMAKE_CXX_FLAGS="-fpic" \
%endif
          ../..
%make_build VERBOSE=1

%install
%makeinstall_std
rm -rfv %buildroot%_includedir/tg_owt/sdk/{objc,android}/
rm -rfv %buildroot%_includedir/tg_owt/base/android/
rm -rfv %buildroot%_includedir/tg_owt/modules/audio_device/android
#rm -rfv %buildroot%_includedir/tg_owt/third_party/libyuv

%files
%_libdir/libtg_owt.so.*

%files devel
%_includedir/tg_owt/
%_libdir/libtg_owt.so
%_libdir/cmake/tg_owt/

%changelog
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
