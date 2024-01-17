%define repo qt5platform-plugins
%define qtver 5.15.11

%def_without clang

Name: deepin-qt5platform-plugins
Version: 5.6.20
Release: alt1

Summary: Qt platform integration plugins for Deepin Desktop Environment

License: LGPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/qt5platform-plugins

Source: %url/archive/%version/%name-%version.tar.gz
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-ninja
# qt5-base-devel-static for libQt5EdidSupport.a
# Automatically added by buildreq on Sat Oct 28 2023
# optimized out: cmake cmake-modules fontconfig-devel gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libICE-devel libSM-devel libX11-devel libXext-devel libXfixes-devel libXi-devel libcairo-devel libdouble-conversion3 libfreetype-devel libglvnd-devel libgmock-devel libgpg-error libp11-kit libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-test libqt5-waylandclient libqt5-widgets libqt5-x11extras libqt5-xcbqpa libsasl2-3 libssl-devel libstdc++-devel libwayland-client-devel libwayland-server-devel libxcb-devel libxcb-render-util libxcbutil-icccm libxcbutil-image libxcbutil-keysyms libxcbutil-keysyms-devel libxkbcommon-devel libxkbcommon-x11 pkg-config python3 python3-base python3-dev python3-module-setuptools qt5-base-devel sh5 wayland-devel xorg-proto-devel zlib-devel
BuildRequires: dwayland-devel extra-cmake-modules libdbus-devel libgtest-devel libmtdev-devel libwayland-cursor-devel libxcb-render-util-devel libxcbutil-icccm-devel libxcbutil-image-devel libxkbcommon-x11-devel qt5-base-devel-static = %qtver qt5-wayland-devel = %qtver qt5-x11extras-devel = %qtver
BuildRequires: kf5-kwayland-devel

%if_with clang
BuildRequires: clang-devel lld-devel
%else
BuildRequires: gcc-c++
%endif

%description
%repo is the
%summary.

%prep
%setup -n %repo-%version
%patch -p1
rm -r xcb/libqt5xcbqpa-dev xcb/libqt6xcbqpa-dev wayland/qtwayland-dev

%build
export PATH=%_qt5_bindir:$PATH

%if_with clang
%define optflags_lto -flto=thin
export CC=clang
export CXX=clang++
export LDFLAGS="-fuse-ld=lld $LDFLAGS"
%endif

%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCMAKE_INSTALL_LIBDIR=%_lib \
  -DCMAKE_INSTALL_PREFIX=%_prefix \
  -DQT_XCB_PRIVATE_HEADERS=%_qt5_headerdir/QtXcb
#
cmake --build %_cmake__builddir -j%__nprocs

%install
%cmake_install

%files
%doc CHANGELOG.md README.md
%doc LICENSE
%_qt5_plugindir/platforms/libdxcb.so
%_qt5_plugindir/platforms/libdwayland.so
%_qt5_plugindir/wayland-shell-integration/libkwayland-shell.so

%changelog
* Tue Jan 16 2024 Leontiy Volodin <lvol@altlinux.org> 5.6.20-alt1
- New version 5.6.20.

* Tue Nov 28 2023 Leontiy Volodin <lvol@altlinux.org> 5.6.16-alt1
- New version 5.6.16.
- Built via cmake instead qmake (by upstream).
- Enabled wayland support.

* Fri Jun 02 2023 Leontiy Volodin <lvol@altlinux.org> 5.6.12-alt1
- New version.

* Tue Apr 18 2023 Leontiy Volodin <lvol@altlinux.org> 5.6.9-alt1
- New version.

* Thu Mar 02 2023 Leontiy Volodin <lvol@altlinux.org> 5.6.5-alt1
- New version.
- Applied fixes from master branch.

* Wed Feb 15 2023 Leontiy Volodin <lvol@altlinux.org> 5.6.4-alt1
- New version.
- Applied fixes from master branch.

* Fri Dec 16 2022 Leontiy Volodin <lvol@altlinux.org> 5.6.3-alt1
- New version.

* Fri Dec 02 2022 Leontiy Volodin <lvol@altlinux.org> 5.0.71-alt1
- New version.

* Sat Nov 19 2022 Leontiy Volodin <lvol@altlinux.org> 5.0.70-alt2.gitfc3d1f1
- Built from commit fc3d1f1a84220848c988ac85429b39a500a61d70.
- Fixed DDE startup with Qt 5.15.7.

* Thu Oct 20 2022 Leontiy Volodin <lvol@altlinux.org> 5.0.70-alt1
- New version.
- Upstream:
  + fix: lock screen interface network panel display abnormal,
  background color overlapping black shadow.
  + fix: missing QPainterPath header.
  + fix: wayland control center time zone background fuzzy problem.
  + feat(libqt5xcbqpa-dev): support Qt 5.15.5.
  + fix: update to xsettings when the home screen changes.
  + fix: cache issue not updated after screen removal.
  + chore: judging support xdg-shell-v6.
  + chore: update Licenses.
  + fix: fix to no response signal after home screen changes.
  + end the start queue when startid is not used.
  + chore: remove hook using std::bind.
  + chore: there is an extra comma when the functionCache
  data is initialized.
  + fix: supportForSplittingWindow return error.
  + fix: fix setting taskbar to follow home screen,
  switch display mode, probability taskbar is not on home
  screen problem.

* Tue Jul 12 2022 Leontiy Volodin <lvol@altlinux.org> 5.0.65-alt1
- New version.
- Upstream:
  + fix: wayland dock right key dish unit deviation.
  + chore: Optimization of problems that cannot be shown by non-tooltip
  menu.
  + chore: Update vtablehook to support lambda expression.
  + fix: The cinema has not resumed broadcasting after minimization.
  + chore: Streamline source files on which the wayland plug depends.
  + chore: Restructuring wayland-shell.
  + chore: reconstruct wayland shell manager.
  + refactor: Modify style and some code logic.
  + refactor: Mainly update the code of the dwayland part.
  + feat(libqt5xcbqpa-dev): support Qt 5.15.4.
  + fix: wayland Environmental touch is not sensitive.
  + chore: fix no-POD static warnings.
  + fix: In the high version, the plug cannot be loaded.
  + chore: Support v23 version to create xdg-shell.
  + fix: wayland switched to the work area, the window is hidden.
  + chore: Support the setting of windows through QWindowFlags to top.
  + feat: add wayland functional test.
  + chore: dde-qt5wayland-plugin running dependency plus qtwayland5.
  + fix(build): qtwayland 5.15 build error.
  + refactor: v23 shell compatibility support and process optimization.
  + chore: Qt5.11 version compatibility test reminder information.
  + fix: The failure of the community version compatibility test
  prevented the application from starting.

* Fri Apr 08 2022 Leontiy Volodin <lvol@altlinux.org> 5.0.62-alt1
- New version (5.0.62).

* Fri Feb 11 2022 Leontiy Volodin <lvol@altlinux.org> 5.0.46-alt1
- New version (5.0.46).

* Thu Aug 19 2021 Leontiy Volodin <lvol@altlinux.org> 5.0.40-alt1
- New version (5.0.40) with rpmgs script.

* Fri May 14 2021 Leontiy Volodin <lvol@altlinux.org> 5.0.23-alt1
- New version (5.0.23) with rpmgs script.

* Thu Apr 15 2021 Leontiy Volodin <lvol@altlinux.org> 5.0.21-alt4.git5b86657
- Built from git.
- Disabled parallel build.

* Fri Apr 02 2021 Leontiy Volodin <lvol@altlinux.org> 5.0.21-alt3.git76c1c3e
- Build from git.

* Thu Feb 11 2021 Leontiy Volodin <lvol@altlinux.org> 5.0.21-alt2.git9a9450f
- Built from git (Qt 5.15.2 support).

* Tue Dec 01 2020 Leontiy Volodin <lvol@altlinux.org> 5.0.21-alt1
- New version (5.0.21) with rpmgs script.

* Thu Oct 08 2020 Leontiy Volodin <lvol@altlinux.org> 5.0.18-alt1
- New version (5.0.18) with rpmgs script.

* Thu Sep 10 2020 Leontiy Volodin <lvol@altlinux.org> 5.0.16-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
