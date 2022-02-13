%define sover 1

Name: libayatana-appindicator
Version: 0.5.90
Release: alt2

Summary: Ayatana application indicators library
License: LGPLv2.1 AND LGPLv3
Group: System/Libraries

Url: https://github.com/AyatanaIndicators/%name
Packager: Nazarov Denis <nenderus@altlinux.org>

ExcludeArch: ppc64le

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
BuildRequires: libayatana-indicator-devel
BuildRequires: libdbusmenu-gtk3-devel
BuildRequires: libgtk-sharp3-devel
BuildRequires: libgtk-sharp3-gapi-devel
BuildRequires: mono-devel
BuildRequires: vala-tools

%description
A library to allow applications to add an icon into the
StatusNotifier-compatible notification area. If none are available,
it also provides an XEmbed-tray fallback.

%package -n %name%sover
Summary: Ayatana application indicators library
Group: System/Libraries

%description -n %name%sover
A library to allow applications to add an icon into the
StatusNotifier-compatible notification area. If none are available,
it also provides an XEmbed-tray fallback.

%package devel
Summary: Development files for %name
Group: Development/C++

%description devel
This package contains the development files for the ayatana
appindicator library..

%package gir
Summary: GObject introspection data for the %name
Group: System/Libraries
Requires: %name%sover = %EVR

%description gir
This package provides GObject introspection data for the %name.

%package gir-devel
Summary: GObject introspection devel data for the %name
Group: Development/Other
Requires: %name-gir = %EVR

%description gir-devel
This package provides GObject introspection devel data for the %name

%package sharp
Summary: Ayatana application indicators library for C#
Group: System/Libraries

%description sharp
This package provides the %name-sharp assembly that
allows CLI (.NET) applications to take menus from applications and
place them in the panel.

%package sharp-devel
Summary: Development files for %name-sharp
Group: Development/Other
Requires: %name-sharp = %EVR

%description sharp-devel
This package contains the development files for the
%name-sharp library.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files -n %name%sover
%doc AUTHORS ChangeLog README
%_libdir/%{name}3.so.*

%files gir
%_typelibdir/AyatanaAppIndicator3-0.1.typelib

%files gir-devel
%_girdir/AyatanaAppIndicator3-0.1.gir

%files devel
%_includedir/%{name}3-0.1/
%_libdir/%{name}3.so
%_pkgconfigdir/ayatana-appindicator3-0.1.pc
%_datadir/vala/vapi/ayatana-appindicator3-0.1.vapi
%_datadir/vala/vapi/ayatana-appindicator3-0.1.deps

%files sharp
%_libdir/cli/ayatana-appindicator3-sharp-0.1/

%files sharp-devel
%_pkgconfigdir/ayatana-appindicator3-sharp-0.1.pc

%changelog
* Sun Feb 13 2022 Nazarov Denis <nenderus@altlinux.org> 0.5.90-alt2
- Separate GObject introspection data subpackage (ALT #41902)
- Fix BR

* Mon Jan 24 2022 Nazarov Denis <nenderus@altlinux.org> 0.5.90-alt1
- Initial build for ALT Linux
