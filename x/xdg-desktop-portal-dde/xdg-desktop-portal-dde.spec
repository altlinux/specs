%def_without clang

%define _libexecdir %_prefix/libexec

Name: xdg-desktop-portal-dde
Version: 1.1.6
Release: alt1

Summary: A backend implement for xdg-desktop-portal on Deepin

License: LGPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/xdg-desktop-portal-dde
VCS: https://github.com/linuxdeepin/xdg-desktop-portal-dde

Packager: Leontiy Volodin <lvol@altlinux.org>

# Source-url: %url/archive/%version/%name-%version.tar.gz
Source: %name-%version.tar
Patch0: %name-%version-%release.patch
Patch1: %name-1.0.15-alt-fix-undefined-symbols.patch

BuildRequires(pre): rpm-build-ninja rpm-macros-dqt6
# Automatically added by buildreq on Wed Apr 30 2025
# optimized out: bash5 bashrc cmake cmake-modules dqt6-base-common dqt6-base-devel gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libX11-devel libdouble-conversion3 libdqt6-concurrent libdqt6-core libdqt6-dbus libdqt6-gui libdqt6-network libdqt6-printsupport libdqt6-waylandclient libdqt6-widgets libdqt6-xml libdtk6core-devel libdtk6gui-devel libdtk6log-devel libglvnd-devel libgpg-error libp11-kit libsasl2-3 libssl-devel libstartup-notification libstdc++-devel libwayland-client libwayland-client-devel libwayland-cursor libwayland-cursor-devel libxkbcommon-devel ninja-build pkg-config python3 python3-base sh5 vulkan-headers wayland-devel xorg-proto-devel
BuildRequires: dqt6-tools dqt6-tools-devel dqt6-wayland-devel dqt6-declarative-devel dtk6-common-devel libdtk6widget-devel libdtk6declarative-devel libwayland-egl-devel libwayland-server-devel treeland-protocols wlr-protocols libcups-devel wayland-protocols libdrm-devel libgbm-devel pipewire-libs-devel libdqt6-qmlcompiler
BuildRequires: libdqt6-concurrent
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
%patch0 -p1
%patch1 -p2

%build
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
%doc LICENSE README.md debian/changelog
%_libexecdir/xdg-desktop-portal-dde
%_userunitdir/xdg-desktop-portal-dde.service
%_datadir/dbus-1/services/org.freedesktop.impl.portal.desktop.dde.service
%dir %_datadir/dsg/
%dir %_datadir/dsg/icons/
%_datadir/dsg/icons/portal-screencast.dci
%dir %_datadir/xdg-desktop-portal/
%dir %_datadir/xdg-desktop-portal/portals/
%_datadir/xdg-desktop-portal/portals/dde.portal
%_datadir/xdg-desktop-portal/dde-portals.conf
%dir %_datadir/%name/
%dir %_datadir/%name/translations/

%files -n lib%{name}-wayland
%_libdir/libxdg-desktop-portal-dde-wayland.so

%changelog
* Mon Jun 22 2026 Leontiy Volodin <lvol@altlinux.org> 1.1.6-alt1
- New version 1.1.6.
- Fixed build on treeland-protocols 0.5.9.

* Fri Feb 27 2026 Leontiy Volodin <lvol@altlinux.org> 1.1.3-alt1
- New version 1.1.3.

* Tue Nov 18 2025 Leontiy Volodin <lvol@altlinux.org> 1.1.1-alt1
- New version 1.1.1.

* Fri Oct 31 2025 Leontiy Volodin <lvol@altlinux.org> 1.1.0-alt1
- New version 1.1.0.

* Wed Oct 15 2025 Leontiy Volodin <lvol@altlinux.org> 1.0.15-alt1
- New version 1.0.15.

* Thu Jul 31 2025 Leontiy Volodin <lvol@altlinux.org> 1.0.13-alt1
- New version 1.0.13.

* Wed Apr 30 2025 Leontiy Volodin <lvol@altlinux.org> 1.0.8-alt1.1
- Cleanup buildrequires.

* Fri Jan 17 2025 Leontiy Volodin <lvol@altlinux.org> 1.0.8-alt1
- New version 1.0.8.
- Added vcs tag.
- Switched to separate qt6 (ALT #48138).

* Wed May 29 2024 Leontiy Volodin <lvol@altlinux.org> 1.0.5.0.9.g8633f76-alt1
- New version 1.0.5-9-g8633f76.
- Switched to qt6 by upstream.

* Fri Dec 08 2023 Leontiy Volodin <lvol@altlinux.org> 1.0.5-alt1.git1c65849
- Initial build for ALT Sisyphus.
