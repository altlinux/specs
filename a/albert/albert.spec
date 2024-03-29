Name:    albert
Version: 0.23.0
Release: alt1

Summary: A fast and flexible keyboard launcher
License: BSD-3-Clause
Group:   Graphical desktop/Other
Url:     https://github.com/albertlauncher/albert

Packager: Sergey Gvozdetskiy <serjigva@altlinux.org>

Source: %name-%version.tar
Source1: submodules.tar

BuildRequires(pre): cmake rpm-macros-cmake
BuildRequires: gcc-c++

BuildRequires: pkgconfig(Qt6Svg)
BuildRequires: pkgconfig(Qt6UiTools)
BuildRequires: pkgconfig(libqalculate)
BuildRequires: pkgconfig(libarchive)
BuildRequires: pkgconfig(libxml++-2.6)
BuildRequires: pkgconfig(pybind11)
BuildRequires: pkgconfig(Qt6Scxml)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(liblzma)
BuildRequires: pkgconfig(python3)

Requires: libqt6-statemachineqml
Requires: libqt6-svg
Requires: qt6-5compat
Requires: libarchive13

%description
Albert is a plugin based, desktop agnostic C++/Qt keyboard launcher that helps
you to accomplish your workflows in a breeze.

%prep
%setup
tar xf %SOURCE1

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc *.md
%_bindir/%name
%dir %_libdir/%name/
%_libdir/%name/*.so*
%_libdir/lib%name.so*
%_datadir/%name/
%_desktopdir/%name.desktop
%dir %_iconsdir/hicolor/scalable/
%dir %_iconsdir/hicolor/scalable/apps/
%_iconsdir/hicolor/scalable/apps/%name.svg

%changelog
* Fri Mar 29 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.23.0-alt1
- Initial build for Sisyphus (Closes: #47237)
