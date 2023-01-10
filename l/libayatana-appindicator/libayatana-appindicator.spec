%define sover 1

%ifarch ppc64le riscv64 %mips32
%def_without mono
%else
%def_with mono
%endif

Name: libayatana-appindicator
Version: 0.5.91
Release: alt1.1

Summary: Ayatana application indicators library
License: LGPLv2.1 AND LGPLv3
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
BuildRequires(pre): libffi-devel
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

%if_with mono
BuildRequires: /proc
%endif
BuildRequires: cmake
BuildRequires: libayatana-indicator3-devel
BuildRequires: libdbusmenu-gtk3-devel
BuildRequires: libgtk+3-gir-devel
%if_with mono
BuildRequires: libgtk-sharp3-devel
BuildRequires: libgtk-sharp3-gapi
BuildRequires: mono-devel
%endif
BuildRequires: vala-tools

%description
A library to allow applications to add an icon into the
StatusNotifier-compatible notification area. If none are available,
it also provides an XEmbed-tray fallback.

%package -n %{name}3-%sover
Summary: Ayatana application indicators library
Group: System/Libraries

%description -n %{name}3-%sover
A library to allow applications to add an icon into the
StatusNotifier-compatible notification area. If none are available,
it also provides an XEmbed-tray fallback.

%package -n %{name}3-devel
Summary: Development files for %name
Group: Development/C++

%description -n %{name}3-devel
This package contains the development files for the ayatana
appindicator library..

%package -n %{name}3-gir
Summary: GObject introspection data for the %{name}3
Group: System/Libraries
Requires: %{name}3-%sover = %EVR

%description -n %{name}3-gir
This package provides GObject introspection data for the %{name}3.

%package -n %{name}3-gir-devel
Summary: GObject introspection devel data for the %{name}3
Group: Development/Other
BuildArch: noarch
Requires: %{name}3-gir = %EVR

%description -n %{name}3-gir-devel
This package provides GObject introspection devel data for the %{name}3

%if_with mono
%package -n %{name}3-sharp
Summary: Ayatana application indicators library for C#
Group: System/Libraries

%description -n %{name}3-sharp
This package provides the %{name}3-sharp assembly that
allows CLI (.NET) applications to take menus from applications and
place them in the panel.

%package -n %{name}3-sharp-devel
Summary: Development files for %{name}3-sharp
Group: Development/Other
Requires: %{name}3-sharp = %EVR

%description -n %{name}3-sharp-devel
This package contains the development files for the
%name-sharp library.
%endif

%package -n %{name}3-vala
Summary: Vala language bindings for %{name}3
Group: Development/Other
BuildArch: noarch
Requires: %{name}3-%sover = %EVR

%description -n %{name}3-vala
This package provides Vala language bindings for %{name}3.

%prep
%setup

%build
%cmake \
%if_without mono
	-DENABLE_BINDINGS_MONO:BOOL=FALSE \
%endif
	%nil
%cmake_build

%install
%cmake_install

%files -n %{name}3-%sover
%doc AUTHORS ChangeLog README
%_libdir/%{name}3.so.*

%files -n %{name}3-gir
%_typelibdir/AyatanaAppIndicator3-0.1.typelib

%files -n %{name}3-gir-devel
%_girdir/AyatanaAppIndicator3-0.1.gir

%files -n %{name}3-devel
%_includedir/%{name}3-0.1/
%_libdir/%{name}3.so
%_pkgconfigdir/ayatana-appindicator3-0.1.pc

%if_with mono
%files -n %{name}3-sharp
%_libdir/cli/ayatana-appindicator3-sharp-0.1/

%files -n %{name}3-sharp-devel
%_pkgconfigdir/ayatana-appindicator3-sharp-0.1.pc
%endif

%files -n %{name}3-vala
%_vapidir/ayatana-appindicator3-0.1.vapi
%_vapidir/ayatana-appindicator3-0.1.deps

%changelog
* Tue Jan 10 2023 Ivan A. Melnikov <iv@altlinux.org> 0.5.91-alt1.1
- NMU: Build w/o mono on riscv64 and mipsel

* Tue May 03 2022 Nazarov Denis <nenderus@altlinux.org> 0.5.91-alt1
- Version 0.5.91

* Sun Feb 13 2022 Nazarov Denis <nenderus@altlinux.org> 0.5.90-alt3
- Fix BR
- Rename subpackages
- Separate vala language bindings subpackage
- Build on ppc6le without mono

* Sun Feb 13 2022 Nazarov Denis <nenderus@altlinux.org> 0.5.90-alt2
- Separate GObject introspection data subpackage (ALT #41902)
- Fix BR

* Mon Jan 24 2022 Nazarov Denis <nenderus@altlinux.org> 0.5.90-alt1
- Initial build for ALT Linux
