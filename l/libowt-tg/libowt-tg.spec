# FIXME:
# on aarch64 missed libs during linking:
# ERROR: ./usr/lib64/libtg_owt.so.0.0.0: undefined symbol: _ZN4absl12lts_2021110214ascii_internal13kPropertyBitsE
# ERROR: ./usr/lib64/libtg_owt.so.0.0.0: undefined symbol: _ZN4absl12lts_2021110220StartsWithIgnoreCaseESt17basic_string_viewIcSt11char_traitsIcEES4_
# ERROR: ./usr/lib64/libtg_owt.so.0.0.0: undefined symbol: _ZN4absl12lts_2021110215AsciiStrToLowerEPNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE
# ERROR: ./usr/lib64/libtg_owt.so.0.0.0: undefined symbol: _ZN4absl12lts_2021110216EqualsIgnoreCaseESt17basic_string_viewIcSt11char_traitsIcEES4_
# ERROR: ./usr/lib64/libtg_owt.so.0.0.0: undefined symbol: _ZN4absl12lts_2021110213base_internal18ThrowStdOutOfRangeEPKc
%def_without internal_absl

Name: libowt-tg
Version: 4.3.0.6
Release: alt1

Summary: Open WebRTC Toolkit with Telegram desktop patches

License: Apache-2.0
Group: System/Libraries
Url: https://github.com/desktop-app/tg_owt

# Source-url: https://github.com/desktop-app/tg_owt/archive/master.zip
Source: %name-%version.tar

Patch4: 0001-disable-dcsctp_transport.patch
Patch5: 0001-support-build-with-system-libsrtp.patch
Patch6: 0001-support-build-with-system-libyuv.patch

Patch2000: %name-e2k.patch

# skip aarch64 (see errors in the top of the spec)
ExcludeArch: armh ppc64le aarch64

BuildRequires: libalsa-devel
BuildRequires: libXtst-devel libXcomposite-devel libXdamage-devel libXrender-devel libXrandr-devel
BuildRequires: libavformat-devel libswresample-devel libswscale-devel
BuildRequires: libdb4-devel libjpeg-devel libopus-devel libpulseaudio-devel libssl-devel yasm
BuildRequires: libprotobuf-devel protobuf-compiler
BuildRequires: libgio-devel

# instead of third party
# supported: absl openh264 usrsctp vpx pipewire srtp yuv (used if detected)
%if_without internal_absl
BuildRequires: libabseil-cpp-devel >= 20211102.0
%endif
BuildRequires: libopenh264-devel
BuildRequires: libusrsctp-devel
BuildRequires: libvpx-devel >= 1.10.0
BuildRequires: pipewire-libs-devel
# TODO: upgrade embedded 2.1.0 (build errors with 2.2.0)
# libsrtp: This project uses private APIs.
# https://github.com/desktop-app/tg_owt/pull/55
#BuildRequires: libsrtp2-devel >= 2.2.0
BuildRequires: libyuv-devel >= 0.0.1805

BuildRequires: libgbm-devel libdrm-devel libepoxy-devel

# Just disable noise (cmake TODO https://gitlab.kitware.com/cmake/cmake/-/issues/18158):
# Package 'libpcre', required by 'glib-2.0', not found
# Package libpcre was not found in the pkg-config search path.
BuildRequires: libpcre-devel
# Just to disable noise like Package 'libffi', required by 'gobject-2.0', not found
BuildRequires: libffi-devel

BuildRequires: gcc-c++ cmake ninja-build

#add_optflags -D_FILE_OFFSET_BITS=64
# TODO: enable logging and debugging
#add_optflags -DRTC_DISABLE_LOGGING=1

%add_optflags -fPIC

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
Requires: %name = %EVR
Requires: libjpeg-devel libopus-devel
Requires: libvpx-devel
Requires: libyuv-devel


%description devel
%name-devel contains the libraries and header files needed to
develop programs which make use of %name.

%prep
%setup
%patch4 -p2
%patch5 -p2
%patch6 -p2
%ifarch %e2k
%patch2000 -p2
%endif

# TODO (used in cmake checks):
#rm -rv src/third_party/{openh264,pipewire,usrsctp}
#rm -v cmake/{libopenh264,libusrsctp}.cmake
rm -rfv src/base/android/

# stop using direct path lib libyuv headers (TODO: move to the libyuv patch?)
find -type f -name "*.cc" | xargs subst 's|third_party/libyuv/include/||'

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
          -DTG_OWT_USE_PIPEWIRE:BOOL=ON \
%ifarch %ix86
          -DCMAKE_CXX_FLAGS="-fpic" \
%endif
          ../..
%make_build VERBOSE=1

%install
%makeinstall_std
rm -rv %buildroot%_includedir/tg_owt/sdk/{objc,android}/
rm -rv %buildroot%_includedir/tg_owt/modules/audio_device/android

%if_without internal_absl
rm -rfv %buildroot%_includedir/tg_owt/third_party/abseil-cpp/
%endif

rm -rfv %buildroot%_includedir/tg_owt/third_party/{openh264,usrsctp,libvpx,pipewire,srtp,libyuv}
rm -rfv %buildroot%_includedir/tg_owt/third_party/{yasm,pffft,rnnoise}

%files
%_libdir/libtg_owt.so.*

%files devel
%_includedir/tg_owt/
%_libdir/libtg_owt.so
%_libdir/cmake/tg_owt/

%changelog
* Sun Apr 10 2022 Vitaly Lipatov <lav@altlinux.ru> 4.3.0.6-alt1
- new version (4.3.0.6) with rpmgs script
- build from git 1fe5e68d999e0bf88d0128ad813438726732f6e0
- remove third_party headers from includedir
- stop build for aarch64 (due strange linking issues with abseil-cpp

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
