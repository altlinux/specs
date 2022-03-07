%define sover 7

Name: libayatana-indicator
Version: 0.9.1
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
BuildRequires: libayatana-ido3-devel
BuildRequires: libgtk+2-devel

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

%package -n %{name}3-%sover
Summary: Ayatana Indicator Display Objects
Group: System/Libraries

%description -n %{name}3-%sover
This library contains information to build indicators to go into
the indicator applet.

%package -n %{name}3-devel
Summary: Development files for the Ayatana panel indicator applet library
Group: Development/C++

%description -n %{name}3-devel
This library contains information to build indicators to go into
the indicator applet.

%prep
%setup -a 0
%__mv %name-%version %name-%version-gtk3

%build
# Build with GTK2
%cmake -DFLAVOUR_GTK2:BOOL=TRUE
%cmake_build

# Build with GTK3
pushd %name-%version-gtk3
%cmake -DCMAKE_INSTALL_LIBEXECDIR:PATH=%_libexecdir
%cmake_build
popd

%install
%cmake_install

pushd %name-%version-gtk3
%cmake_install
popd

%files -n %name%sover
%_libdir/%name.so.*

%files devel
%_includedir/%name-0.4
%_libdir/%name.so
%_pkgconfigdir/ayatana-indicator-0.4.pc

%files -n %{name}3-%sover
%_libdir/%{name}3.so.*

%files -n %{name}3-devel
%_includedir/%{name}3-0.4
%_libdir/%{name}3.so
%_pkgconfigdir/ayatana-indicator3-0.4.pc
%_libexecdir/%name
%_datadir/%name

%changelog
* Mon Mar 07 2022 Nazarov Denis <nenderus@altlinux.org> 0.9.1-alt1
- Version 0.9.1

* Sun Feb 13 2022 Nazarov Denis <nenderus@altlinux.org> 0.9.0-alt2
- Rename subpackages
- Fix BR
- Build also with GTK2

* Fri Jan 14 2022 Nazarov Denis <nenderus@altlinux.org> 0.9.0-alt1
- Initial build for ALT Linux
