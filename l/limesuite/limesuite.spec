%define _unpackaged_files_terminate_build 1
%define _udevrulesdir /lib/udev/rules.d

Name: limesuite
Version: 23.11.0
Release: alt3

Summary: Driver and GUI for LMS7002M-based SDR platforms
License: Apache-2.0
Group: Engineering
Url: https://github.com/myriadrf/LimeSuite

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libwxBase3.2-devel
BuildRequires: libwiringpi-devel-static
BuildRequires: pkgconfig(opengl)
BuildRequires: pkgconfig(glu)
BuildRequires: pkgconfig(glew)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(xft)
BuildRequires: pkgconfig(xfixes)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(SoapySDR)
BuildRequires: /usr/bin/octave-config
BuildRequires: octave-devel
BuildRequires: pkgconfig(libusb-1.0)
BuildRequires: /usr/bin/fltk-config
BuildRequires: /usr/bin/doxygen

%description
Lime Suite is a collection of software supporting Lime Microsystems LMS7
RF transceiver based hardware such as the LimeSDR, LMS7002M UNITE board,
or the Novena with LMS7 RF board.

%prep
%setup
%patch -p1
sed -i 's|MODE="660"|MODE="666"|g' udev-rules/64-limesuite.rules
sed -i 's|^Categories=.*|Categories=Development;Debugger;|' Desktop/lime-suite.desktop

%build
%add_optflags -std=gnu17
%cmake \
       -Wno-dev \
       -DCMAKE_BUILD_TYPE=Release \
       -DENABLE_UTILITIES=True \
       -DENABLE_LIME_UTIL=True \
       -DCMAKE_SKIP_RPATH=True \
       -DENABLE_DESKTOP=True \
       -DENABLE_SOAPY_LMS7=True \
       -DENABLE_PCIE_XILLYBUS=True \
       -DENABLE_QUICKTEST=True \
       -DENABLE_MCU_TESTBENCH=True \
       -DENABLE_FTDI=True \
       -DENABLE_FX3=True \
       -DENABLE_STREAM_UNITE=True \
       -DENABLE_EXAMPLES=True \
       -DENABLE_HEADERS=True \
       -DENABLE_GUI=True \
       -DENABLE_OCTAVE=False \
       -DENABLE_API_DOXYGEN=True \
       -DENABLE_EVB7COM=True \
       -DENABLE_SPI=True \
       -DBUILD_SHARED_LIBS=ON \
       -DUDEV_RULES_PATH=%_udevrulesdir \
       -DENABLE_SIMD_FLAGS=none \
       -DOVERRIDE_LIME_SUITE_VERSION="%version"

%cmake_build

%install
%cmake_install

%files
%doc Changelog.txt COPYING README.md
%_bindir/LimeQuickTest
%_bindir/LimeSuiteGUI
%_bindir/LimeUtil
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/*/*.png
%_udevrulesdir/*.rules
%_libdir/SoapySDR/modules0.8/libLMS7Support.so
%_libdir/libLimeSuite.so*

%dir %_includedir/lime
%_includedir/lime/*
%dir %_libdir/cmake/LimeSuite
%_libdir/cmake/LimeSuite/*
%_pkgconfigdir/*.pc

%changelog
* Thu Apr 23 2026 Nikolay Strelkov <snk@altlinux.org> 23.11.0-alt3
- Fixed FTBFS caused by gcc15.

* Fri Jun 27 2025 Nikolay Strelkov <snk@altlinux.org> 23.11.0-alt2
- Applied repocop fix for sisyphus_check, freedesktop-categories

* Sun Jun 08 2025 Nikolay Strelkov <snk@altlinux.org> 23.11.0-alt1
- Initial build for Sisyphus
