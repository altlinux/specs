%define sover 0

Name: ayatana-ido
Version: 0.9.0
Release: alt2

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

%package -n lib%{name}3-%sover
Summary: Ayatana Indicator Display Objects
Group: System/Libraries
Provides: lib%name%sover = %EVR
Obsoletes: lib%name%sover <= 0.9.0-alt1

%description -n lib%{name}3-%sover
Shared library providing extra GTK menu items for display in
system indicators.

%package -n lib%{name}3-devel
Summary: Development files for Ayatana Indicator Display Objects
Group: Development/C++
Provides: lib%name-devel = %EVR
Obsoletes: lib%name-devel <= 0.9.0-alt1

%description -n lib%{name}3-devel
Shared library providing extra GTK menu items for display in
system indicators.

This package contains the development files for Ido.

%package -n %{name}3-gir
Summary: GObject introspection data for the %{name}3
Group: System/Libraries
Requires: lib%{name}3-%sover = %EVR

%description -n %{name}3-gir
This package provides GObject introspection data for the %{name}3.

%package -n %{name}3-gir-devel
Summary: GObject introspection devel data for the %{name}3
Group: Development/Other
BuildArch: noarch
Requires: %{name}3-gir = %EVR

%description -n %{name}3-gir-devel
This package provides GObject introspection devel data for the %{name}3

%package -n %{name}3-vala
Summary: Vala language bindings for %{name}3
Group: Development/Other
BuildArch: noarch
Requires: lib%{name}3-%sover = %EVR

%description -n %{name}3-vala
This package provides Vala language bindings for %{name}3.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files -n lib%{name}3-%sover
%_libdir/lib%{name}3-0.4.so.*

%files -n lib%{name}3-devel
%_includedir/lib%{name}3-0.4
%_libdir/lib%{name}3-0.4.so
%_pkgconfigdir/lib%{name}3-0.4.pc

%files -n %{name}3-gir
%_typelibdir/AyatanaIdo3-0.4.typelib

%files -n %{name}3-gir-devel
%_girdir/AyatanaIdo3-0.4.gir

%files -n %{name}3-vala
%_vapidir/AyatanaIdo3-0.4.vapi

%changelog
* Sun Feb 13 2022 Nazarov Denis <nenderus@altlinux.org> 0.9.0-alt2
- Rename subpackages
- Separate GObject introspection data and vala language bindings subpackages

* Fri Jan 14 2022 Nazarov Denis <nenderus@altlinux.org> 0.9.0-alt1
- Initial build for ALT Linux
