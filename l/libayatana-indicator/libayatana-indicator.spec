%define sover 7

Name: libayatana-indicator
Version: 0.9.0
Release: alt1

Summary: Ayatana Indicator Display Objects
License: GPLv3
Group: System/Libraries

Url: https://github.com/AyatanaIndicators/%name
Packager: Nazarov Denis <nenderus@altlinux.org>

# https://github.com/AyatanaIndicators/%name/archive/%version/%name-%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): at-spi2-atk-devel
BuildRequires(pre): bzlib-devel
BuildRequires(pre): libXdmcp-devel
BuildRequires(pre): libXcomposite-devel
BuildRequires(pre): libXcursor-devel
BuildRequires(pre): libXdamage-devel
BuildRequires(pre): libXi-devel
BuildRequires(pre): libXinerama-devel
BuildRequires(pre): libXrandr-devel
BuildRequires(pre): libXtst-devel
BuildRequires(pre): libat-spi2-core-devel
BuildRequires(pre): libblkid-devel
BuildRequires(pre): libbrotli-devel
BuildRequires(pre): libdatrie-devel
BuildRequires(pre): libdbus-devel
BuildRequires(pre): libepoxy-devel
BuildRequires(pre): libexpat-devel
BuildRequires(pre): libfribidi-devel
BuildRequires(pre): libpcre-devel
BuildRequires(pre): libpixman-devel
BuildRequires(pre): libmount-devel
BuildRequires(pre): libselinux-devel
BuildRequires(pre): libthai-devel
BuildRequires(pre): libtiff-devel
BuildRequires(pre): libuuid-devel
BuildRequires(pre): libxkbcommon-devel
BuildRequires(pre): libwayland-cursor-devel
BuildRequires(pre): libwayland-egl-devel

BuildRequires: cmake
BuildRequires: libayatana-ido-devel

%description
This library contains information to build indicators to go into
the indicator applet.

%package -n %name%sover
Summary: Ayatana Indicator Display Objects
Group: System/Libraries

%description -n %name%sover
This library contains information to build indicators to go into
the indicator applet.

%package devel
Summary: Development files for the Ayatana panel indicator applet library
Group: Development/C++

%description devel
This library contains information to build indicators to go into
the indicator applet.

%prep
%setup

%build
%cmake -DCMAKE_INSTALL_LIBEXECDIR:PATH=%_libexecdir
%cmake_build

%install
%cmake_install

%files -n %name%sover
%_libdir/%{name}3.so.*

%files devel
%_includedir/%{name}3-0.4
%_libdir/%{name}3.so
%_pkgconfigdir/ayatana-indicator3-0.4.pc
%_libexecdir/%name
%_datadir/%name

%changelog
* Fri Jan 14 2022 Nazarov Denis <nenderus@altlinux.org> 0.9.0-alt1
- Initial build for ALT Linux
