Name: libopenrazer
Version: 0.3.0
Release: alt1

Summary: Qt wrapper around the D-Bus API from OpenRazer
License: GPLv3+
Group: System/Configuration/Hardware
Url: https://github.com/z3ntu/libopenrazer

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: gcc-c++
BuildRequires: meson
BuildRequires: qt5-base-devel
BuildRequires: pkgconfig(Qt5UiTools)
BuildRequires: pkgconfig(Qt5Xml)

%description
Qt wrapper around the D-Bus API from OpenRazer.

%package devel
Summary: Development libraries and header files for libopenrazer
Group: Development/C
Requires: %name = %EVR

%description devel
Qt wrapper around the D-Bus API from OpenRazer.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%_datadir/%name
%_libdir/%name.so.*

%files devel
%_includedir/%name.h
%_includedir/%name/*
%_libdir/%name.so
%_libdir/pkgconfig/%name.pc

%changelog
* Mon Jan 13 2025 Sergey Palcheh <minergenon@altlinux.org> 0.3.0-alt1
- Initial build for ALT Sisyphus.

