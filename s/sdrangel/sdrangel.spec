%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: sdrangel
Version: 7.26.1
Release: alt1

Summary: Qt-based SDR front-end for various devices
License: GPL-3.0-or-later
Group: Engineering
Url: https://github.com/f4exb/sdrangel

Source: %name-%version.tar

# sync with Debian unstable 7.26.1+dfsg-2, apply local fixes
Patch: %name-%version-%release.patch

ExcludeArch: %not_qt6_qtwebengine_arches

BuildRequires(pre): cmake
BuildRequires(pre): rpm-macros-qt6-webengine

BuildRequires: gcc-c++
BuildRequires: git
BuildRequires: patchelf

## Qt libraries
BuildRequires: qt6-base-devel
BuildRequires: qt6-tools-devel
BuildRequires: pkgconfig(Qt6WebSockets)
BuildRequires: pkgconfig(Qt6Quick)
BuildRequires: pkgconfig(Qt6Svg)
BuildRequires: pkgconfig(Qt6Multimedia)
BuildRequires: pkgconfig(Qt6Positioning)
BuildRequires: pkgconfig(Qt6Charts)
BuildRequires: pkgconfig(Qt6SerialPort)
BuildRequires: pkgconfig(Qt6StateMachine)
BuildRequires: pkgconfig(Qt6WebEngineQuick)
BuildRequires: pkgconfig(Qt6TextToSpeech)
BuildRequires: pkgconfig(cups)
BuildRequires: pkgconfig(Qt6Location)

## Misc libraries
%ifarch x86_64 aarch64
BuildRequires: pkgconfig(libunwind)
%endif

BuildRequires: boost-devel-headers
BuildRequires: pkgconfig(fftw3f)
BuildRequires: pkgconfig(flac)
BuildRequires: pkgconfig(libusb-1.0)
BuildRequires: libopencv-devel
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(faad2)
BuildRequires: pkgconfig(codec2)
BuildRequires: libhidapi-devel
BuildRequires: pkgconfig(libavdevice)
BuildRequires: pkgconfig(libavfilter)
BuildRequires: pkgconfig(hamlib)

## Hardware libraries
BuildRequires: pkgconfig(libairspy)
BuildRequires: pkgconfig(libbladeRF)
BuildRequires: pkgconfig(libhackrf)
BuildRequires: limesuite
BuildRequires: pkgconfig(libiio)
BuildRequires: pkgconfig(libmirisdr)
BuildRequires: pkgconfig(librtlsdr)
BuildRequires: pkgconfig(uhd)
BuildRequires: pkgconfig(SoapySDR)

## Documentation
BuildRequires: doxygen
BuildRequires: graphviz

## not enabled components
#   # disabled via cmake flag ENABLE_CHANNELRX_SIGMFFILESINK=OFF
#   # BuildRequires: pkgconfig(libsigmf) # TODO
#
#   # disabled via cmake flags ENABLE_CHANNELTX_REMOTESOURCE=OFF and ENABLE_CHANNELRX_REMOTESINK=OFF
#   # BuildRequires: pkgconfig(libcm256cc) # TODO
#
#   # disabled via cmake flag ENABLE_CHANNELRX_DEMODDSD=OFF
#   # BuildRequires: pkgconfig(libdsdcc) # TODO
#
#   # disabled via cmake flag ENABLE_FEATURE_SATELLITETRACKER=OFF
#   # BuildRequires: pkgconfig(sgp4) # TODO
#
#   # ???
#   # CSPICE # TODO?
#
#   # disabled via cmake flag ENABLE_CHANNELRX_DEMODAPT=OFF
#   # BuildRequires: pkgconfig(apt) # TODO
#
#   # disabled via cmake flag ENABLE_CHANNELRX_DEMODAPT=OFF
#   # BuildRequires: pkgconfig(libdab) # TODO
#
#   # libpostproc-dev, - upstream doesn't support it anymore
#   # BuildRequires: pkgconfig(libpostproc)
#
#   # disabled via cmake flag ENABLE_FEATURE_MORSEDECODER=OFF
#   # BuildRequires: pkgconfig(libggmorse) # TODO
#
#   # disabled via cmake flag ENABLE_FEATURE_DENOISER=OFF
#   #BuildRequires: pkgconfig(librnnoise) # TODO
#
#   # disabled via cmake flag ENABLE_CHANNELRX_DEMODINMARSAT=OFF
#   # inmarsatc_decoder.h and so on
#
# # Hardware libraries
#
#   # BuildRequires: pkgconfig(libairspyhf) # TODO
#   # BuildRequires: pkgconfig(libxtrx) # TODO
#
#   # disabled via cmake flag ENABLE_PERSEUS=OFF
#   # BuildRequires: pkgconfig(libperseus-sdr) # TODO
#
#   # disabled via cmake flag ENABLE_SDRPLAY=OFF
#   # sdrplay_api.h and so on

Requires: libqt6-core5compat
Requires: libqt6-labsanimation
Requires: libqt6-location
Requires: libqt6-positioning
Requires: libqt6-qml
Requires: libqt6-quick
Requires: libqt6-quickcontrols2
Requires: libqt6-quickcontrols2basic
Requires: libqt6-quickcontrols2fusion
Requires: libqt6-quickeffects

%description
SDR front-end supporting many hardware and software receivers/transmitter,
including: RTL-SDR, BladeRF, HackRF and others.

It uses Qt framework and OpenGL for graphical rendering,
works on many operating systems.

Supported modes:

* Analog:
  AM, APT, Broadcast FM, DSB, FM, ILS, NTSC, PAL, SSB, VOR
* Digital:
  AIS, ADS-B, APRS, DAB, DVB-S, DVB-S2, FreeDV, Navtex, Packet (AX.25)
  and numerous additional.

%prep
%setup
%patch -p1
sed -i 's|#!/usr/bin/env python|#!/usr/bin/python3|g' swagger/sdrangel/examples/*.py

%ifarch loongarch64
sed -i 's|FATAL_ERROR "Not supported|WARNING "Not supported|' cmake/Modules/DetectArchitecture.cmake
%endif

%build
%cmake \
       -Wno-dev \
       -DENABLE_QT6=ON \
       -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DRX_SAMPLE_24BIT=ON \
%ifarch x86_64 aarch64
       -DENABLE_LIBUNWIND=ON \
%else
       -DENABLE_LIBUNWIND=OFF \
%endif
%ifarch i586 x86_64
       -DFORCE_SSE41=ON \
%endif
       -DENABLE_PERSEUS=OFF \
       -DENABLE_SDRPLAY=OFF \
       -DENABLE_CHANNELRX_DEMODINMARSAT=OFF \
       -DENABLE_CHANNELRX_DEMODDAB=OFF \
       -DENABLE_CHANNELRX_DEMODAPT=OFF \
       -DENABLE_CHANNELRX_DEMODDSD=OFF \
       -DENABLE_CHANNELRX_REMOTESINK=OFF \
       -DENABLE_CHANNELRX_SIGMFFILESINK=OFF \
       -DENABLE_CHANNELTX_REMOTESOURCE=OFF \
       -DENABLE_FEATURE_SATELLITETRACKER=OFF \
       -DENABLE_FEATURE_MORSEDECODER=OFF \
       -DENABLE_FEATURE_DENOISER=OFF
%cmake_build

%install
%cmake_install

rm -vf %buildroot%_datadir/sdrangel/Readme.md

patchelf %buildroot%_bindir/sdrangel --add-rpath %_libdir/sdrangel
patchelf %buildroot%_bindir/sdrangelbench --add-rpath %_libdir/sdrangel
patchelf %buildroot%_bindir/sdrangelsrv --add-rpath %_libdir/sdrangel

patchelf %buildroot%_libdir/sdrangel/*.so --add-rpath %_libdir/sdrangel
patchelf %buildroot%_libdir/sdrangel/plugins/*.so --add-rpath %_libdir/sdrangel
patchelf %buildroot%_libdir/sdrangel/pluginssrv/*.so --add-rpath %_libdir/sdrangel

%files
%doc Readme.md
%doc swagger/sdrangel/examples/
%_bindir/sdrangel
%_bindir/sdrangelbench
%_bindir/sdrangelsrv
%dir %_libdir/sdrangel
%_libdir/sdrangel/*.so
%dir %_libdir/sdrangel/plugins
%_libdir/sdrangel/plugins/*.so
%dir %_libdir/sdrangel/pluginssrv
%_libdir/sdrangel/pluginssrv/*.so
%_desktopdir/sdrangel.desktop
%_iconsdir/hicolor/scalable/apps/sdrangel_icon.svg
%_datadir/metainfo/org.sdrangel.SDRangel.metainfo.xml

%changelog
* Thu Jun 18 2026 Nikolay Strelkov <snk@altlinux.org> 7.26.1-alt1
- Initial build for Sisyphus
