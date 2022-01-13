%define sover 0

Name: ayatana-ido
Version: 0.9.0
Release: alt1

Summary: Ayatana Indicator Display Objects
License: LGPLv3 AND LGPLv2.1
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
BuildRequires: gcc-c++
BuildRequires: libgtk+3-gir-devel
BuildRequires: vala-tools

%description
Shared library providing extra GTK menu items for display in
system indicators.

%package -n lib%name%sover
Summary: Ayatana Indicator Display Objects
Group: System/Libraries

%description -n lib%name%sover
Shared library providing extra GTK menu items for display in
system indicators.

%package -n lib%name-devel
Summary: Development files for Ayatana Indicator Display Objects
Group: Development/C++

%description -n lib%name-devel
Shared library providing extra GTK menu items for display in
system indicators.

This package contains the development files for Ido.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files -n lib%name%sover
%_libdir/lib%{name}3-0.4.so.*

%files -n lib%name-devel
%_includedir/lib%{name}3-0.4
%_libdir/girepository-1.0/AyatanaIdo3-0.4.typelib
%_libdir/lib%{name}3-0.4.so
%_pkgconfigdir/lib%{name}3-0.4.pc
%_datadir/gir-1.0/AyatanaIdo3-0.4.gir
%_datadir/vala/vapi/AyatanaIdo3-0.4.vapi

%changelog
* Fri Jan 14 2022 Nazarov Denis <nenderus@altlinux.org> 0.9.0-alt1
- Initial build for ALT Linux
