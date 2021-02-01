# https://bugzilla.altlinux.org/show_bug.cgi?id=38832
%def_without packaged_openh264
%def_without packaged_vpx

Name: libowt-tg
Version: 4.3.0.4
Release: alt1

Summary: Open WebRTC Toolkit with Telegram desktop patches

License: Apache-2.0
Group: System/Libraries
Url: https://github.com/desktop-app/tg_owt

# Source-url: https://github.com/desktop-app/tg_owt/archive/master.zip
Source: %name-%version.tar

# TODO: build with packaged libyuv
# Source2-url: https://chromium.googlesource.com/libyuv/libyuv/+archive/ad890067f661dc747a975bc55ba3767fe30d4452.tar.gz
Source2: %name-libyuv-%version.tar

# TODO: build with packaged libvpx
# Source3-url: https://chromium.googlesource.com/webm/libvpx/+archive/5b63f0f821e94f8072eb483014cfc33b05978bb9.tar.gz
Source3: %name-libvpx-%version.tar

Patch4: 0001-add-support-for-packaged-libvpx-enabled-via-TG_OWT_V.patch
Patch5: 1958098091b858767e801456625bc324d4e1d0fb.patch

ExcludeArch: armh ppc64le

BuildRequires: libalsa-devel libXtst-devel
BuildRequires: libavformat-devel libswresample-devel libswscale-devel
BuildRequires: libdb4-devel libjpeg-devel libopus-devel libpulseaudio-devel libssl-devel yasm
BuildRequires: libprotobuf-devel protobuf-compiler

BuildRequires: gcc-c++ cmake ninja-build

%if_with packaged_vpx
BuildRequires: libvpx-devel
%endif

%if_with packaged_openh264
BuildRequires: libopenh264-devel
%endif

# TODO: obsoleted in the distro
#BuildRequires: libyuv-devel

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
Group: Development/C
#Requires: %name = %EVR
Requires: libjpeg-devel libopus-devel
%if_with packaged_vpx
Requires: libvpx-devel
%endif

%description devel
%name-devel contains the libraries and header files needed to
develop programs which make use of %name.

%prep
%setup -a2 -a3
%if_with packaged_vpx
%patch4 -p1
%endif
%patch5 -p1

#subst "1iset(CMAKE_CXX_STANDARD 17)" CMakeLists.txt

%if_with packaged_vpx
rm -rfv src/third_party/libvpx/
%endif

%if_with packaged_openh264
rm -rfv src/third_party/openh264/
mkdir -p src/third_party/openh264/src/codec/api/
ln -s %_includedir/wels src/third_party/openh264/src/codec/api/svc
%__subst "s|.*openh264.*||" CMakeLists.txt
%endif

# TODO
#rm -rfv src/third_party/libyuv/
#mkdir -p src/third_party/libyuv/
#ln -s %_includedir src/third_party/libyuv/include

%build
%ifarch %ix86 x86_64 %arm
export CFLAGS="$RPM_OPT_FLAGS -fPIC"
%endif
%cmake_insource \
          -DCMAKE_BUILD_TYPE=RelWithDebInfo \
          -DBUILD_SHARED_LIBS:BOOL=ON \
          -DCMAKE_POSITION_INDEPENDENT_CODE:BOOL=ON \
          -DTG_OWT_USE_PROTOBUF:BOOL=ON \
%ifarch %ix86
          -DCMAKE_CXX_FLAGS="-fpic" \
%endif
%if_with packaged_vpx
          -DTG_OWT_VPX_PACKAGED_BUILD=TRUE \
%endif
          ../..
%make_build

%install
%makeinstall_std

%files
%_libdir/libtg_owt.so.*

%files devel
%_includedir/tg_owt/
%_libdir/libtg_owt.so
%_libdir/cmake/tg_owt/

%changelog
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
