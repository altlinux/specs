%def_without clang

%define _libexecdir %_prefix/libexec

Name: xdg-desktop-portal-dde
Version: 1.0.8
Release: alt1

Summary: A backend implement for xdg-desktop-portal on Deepin

License: LGPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/xdg-desktop-portal-dde
Vcs: git://github.com/linuxdeepin/xdg-desktop-portal-dde.git

Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz

BuildRequires(pre): rpm-build-ninja rpm-macros-dqt6
BuildRequires: dwayland-devel extra-cmake-modules libwayland-cursor-devel libwayland-egl-devel dqt6-tools dqt6-wayland-devel dtk6-common-devel libdtk6core-devel libdtk6widget-devel treeland-protocols wlr-protocols
%if_with clang
BuildRequires: clang-devel
%else
BuildRequires: gcc-c++
%endif

%description
%summary.

%package -n lib%{name}-wayland
Summary: Library for %name
Group: System/Libraries
Requires: libdqt6-gui = %_dqt6_version
Requires: libdqt6-waylandclient = %_dqt6_version

%description -n lib%{name}-wayland
The package provides lib%{name}-wayland for %name.

%prep
%setup

%build
export LC_ALL=C.UTF-8
%if_with clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
export NM="llvm-nm"
export READELF="llvm-readelf"
%endif
%DQ6build

%install
%DQ6install
%find_lang --with-qt %name

%files -f %name.lang
%doc LICENSE README.md
%_libexecdir/xdg-desktop-portal-dde
%_userunitdir/xdg-desktop-portal-dde.service
%_datadir/dbus-1/services/org.freedesktop.impl.portal.desktop.dde.service
%dir %_datadir/xdg-desktop-portal/
%dir %_datadir/xdg-desktop-portal/portals/
%_datadir/xdg-desktop-portal/portals/dde.portal
%_datadir/xdg-desktop-portal/dde-portals.conf
%dir %_datadir/%name/
%dir %_datadir/%name/translations/

%files -n lib%{name}-wayland
%_libdir/libxdg-desktop-portal-dde-wayland.so

%changelog
* Fri Jan 17 2025 Leontiy Volodin <lvol@altlinux.org> 1.0.8-alt1
- New version 1.0.8.
- Added vcs tag.
- Switched to separate qt6 (ALT #48138).

* Wed May 29 2024 Leontiy Volodin <lvol@altlinux.org> 1.0.5.0.9.g8633f76-alt1
- New version 1.0.5-9-g8633f76.
- Switched to qt6 by upstream.

* Fri Dec 08 2023 Leontiy Volodin <lvol@altlinux.org> 1.0.5-alt1.git1c65849
- Initial build for ALT Sisyphus.
