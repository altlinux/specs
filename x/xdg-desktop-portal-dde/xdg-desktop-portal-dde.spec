%def_without clang

%define _libexecdir %_prefix/libexec

Name: xdg-desktop-portal-dde
Version: 1.0.5
Release: alt1.git1c65849

Summary: A backend implement for xdg-desktop-portal on Deepin

License: LGPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/xdg-desktop-portal-dde

Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz

BuildRequires(pre): rpm-build-ninja
BuildRequires: dwayland-devel extra-cmake-modules kf5-kdeclarative-devel kf5-ki18n-devel kf5-knotifications-devel kf5-kpackage-devel libwayland-cursor-devel libwayland-egl-devel qt5-wayland-devel
%if_with clang
BuildRequires: clang-devel
%else
BuildRequires: gcc-c++
%endif

%description
%summary.

%prep
%setup

%build
%if_with clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
export NM="llvm-nm"
export READELF="llvm-readelf"
%endif
export PATH=%_qt5_bindir:$PATH
%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
#
cmake --build "%_cmake__builddir" -j%__nprocs	

%install
%cmake_install

%files
%doc LICENSE README.md
%_libexecdir/xdg-desktop-portal-dde
%_userunitdir/xdg-desktop-portal-dde.service
%_datadir/dbus-1/services/org.freedesktop.impl.portal.desktop.dde.service
%dir %_datadir/xdg-desktop-portal/
%dir %_datadir/xdg-desktop-portal/portals/
%_datadir/xdg-desktop-portal/portals/dde.portal
%_datadir/xdg-desktop-portal/dde-portals.conf

%changelog
* Fri Dec 08 2023 Leontiy Volodin <lvol@altlinux.org> 1.0.5-alt1.git1c65849
- Initial build for ALT Sisyphus.
