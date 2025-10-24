%define repo qt6platform-plugins

%def_without clang

Name: deepin-qt6platform-plugins
Version: 6.0.44
Release: alt1

Summary: Qt platform integration plugins for Deepin Desktop Environment

License: LGPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/qt6platform-plugins
VCS: https://github.com/linuxdeepin/qt6platform-plugins

# Source-url: %url/archive/%version/%name-%version.tar.gz
Source: %name-%version.tar
Patch0: %name-%version-%release.patch
Patch1: deepin-qt6platform-plugins-5.6.28-alt-plugin-path.patch

BuildRequires(pre): rpm-build-ninja rpm-macros-dqt6
# Automatically added by buildreq on Wed Apr 30 2025
# optimized out: cmake cmake-modules gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libICE-devel libX11-devel libXau-devel libXext-devel libXfixes-devel libXrender-devel libdouble-conversion3 libdqt6-core libdqt6-dbus libdqt6-gui libdqt6-opengl libdqt6-widgets libdqt6-xcbqpa libglvnd-devel libgpg-error libp11-kit libsasl2-3 libssl-devel libstdc++-devel libxcb-devel libxcb-render-util libxcbutil-cursor libxcbutil-icccm libxcbutil-image libxcbutil-keysyms libxkbcommon-devel libxkbcommon-x11 ninja-build pkg-config python3 python3-base sh5 vulkan-headers xorg-proto-devel
BuildRequires: dqt6-base-devel libSM-devel libXi-devel libcairo-devel libdbus-devel libmtdev-devel libxcb-render-util-devel libxcbutil-cursor-devel libxcbutil-icccm-devel libxcbutil-image-devel libxcbutil-keysyms-devel libxkbcommon-x11-devel libxcbutil-devel libXevie-devel libxprintutil-devel

%if_with clang
BuildRequires: clang-devel lld-devel
%else
BuildRequires: gcc-c++
%endif

Requires: libdqt6-core = %_dqt6_version libdqt6-gui = %_dqt6_version libdqt6-opengl = %_dqt6_version

%description
%repo is the
%summary.

%prep
%setup -n %repo-%version
%patch0 -p1
%patch1 -p1
rm -r xcb/libqt5xcbqpa-dev xcb/libqt6xcbqpa-dev wayland/qtwayland-dev

%build
%if_with clang
%define optflags_lto -flto=thin
export CC=clang
export CXX=clang++
export LDFLAGS="-fuse-ld=lld $LDFLAGS"
%endif

%DQ6build \
  -DCMAKE_INSTALL_LIBDIR=%_lib \
  -DCMAKE_INSTALL_PREFIX=%_prefix \
  -DQT_XCB_PRIVATE_HEADERS=%_dqt6_headerdir/QtXcb \
  -DPLUGIN_INSTALL_DIR=%_dqt6_plugindir \
  -DDTK_VERSION=%version \
#

%install
%DQ6install

%files
%doc CHANGELOG.md README.md
%doc LICENSE
%_dqt6_plugindir/platforms/libdxcb.so

%changelog
* Fri Oct 24 2025 Leontiy Volodin <lvol@altlinux.org> 6.0.44-alt1
- New version 6.0.44.

* Wed Oct 15 2025 Leontiy Volodin <lvol@altlinux.org> 6.0.43-alt1
- New version 6.0.43.

* Tue Aug 19 2025 Leontiy Volodin <lvol@altlinux.org> 6.0.41-alt1
- New version 6.0.41.

* Fri Aug 01 2025 Leontiy Volodin <lvol@altlinux.org> 6.0.40-alt1
- New version 6.0.40.

* Mon Jul 21 2025 Leontiy Volodin <lvol@altlinux.org> 6.0.39-alt1
- New version 6.0.39.

* Fri Jun 20 2025 Leontiy Volodin <lvol@altlinux.org> 6.0.37-alt1
- New version 6.0.37.

* Wed Apr 30 2025 Leontiy Volodin <lvol@altlinux.org> 6.0.34-alt1
- Initial build for ALT Sisyphus.
