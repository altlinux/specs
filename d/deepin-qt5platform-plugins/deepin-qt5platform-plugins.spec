%define repo qt5platform-plugins

%def_without clang

Name: deepin-qt5platform-plugins
Version: 6.7.43
Release: alt1

Summary: Qt platform integration plugins for Deepin Desktop Environment

License: LGPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/qt5platform-plugins
VCS: https://github.com/linuxdeepin/qt5platform-plugins

# Source-url: %url/archive/%version/%name-%version.tar.gz
Source: %name-%version.tar
Patch0: %repo-%version-%release.patch
Patch1: deepin-qt5platform-plugins-5.6.28-alt-plugin-path.patch

# Common BuildRequires.
BuildRequires(pre): rpm-build-ninja
BuildRequires: libdbus-devel libmtdev-devel libxcb-render-util-devel libxcbutil-icccm-devel libxcbutil-image-devel libSM-devel libcairo-devel libxcbutil-keysyms-devel libxcbutil-cursor-devel libxkbcommon-x11-devel libxcbutil-devel libXevie-devel libxprintutil-devel

%if_with clang
BuildRequires: clang-devel lld-devel
%else
BuildRequires: gcc-c++
%endif

# DTK5 BuildRequires.
BuildRequires(pre): rpm-macros-dqt5
# dqt5-base-devel-static for libQt5EdidSupport.a
BuildRequires: dqt5-base-devel-static dqt5-x11extras-devel libdqt5-quickshapes libdqt5-widgets
# BuildRequires: extra-cmake-modules kf5-kwayland-devel libkf5waylandclient libkf5waylandserver dqt5-wayland-devel libwayland-cursor-devel

Requires: libdqt5-core = %_dqt5_version libdqt5-gui = %_dqt5_version libdqt5-xcbqpa = %_dqt5_version
# Requires: libdqt5-waylandclient = %%_dqt5_version

# DTK6 BuildRequires.
BuildRequires(pre): rpm-macros-dqt6
BuildRequires: dqt6-base-devel libdqt6-dbus libdqt6-gui libdqt6-widgets vulkan-headers

%description
%repo is the %summary.

%package -n deepin-qt6platform-plugins
Summary: Qt platform integration plugins for Deepin Desktop Environment
Group: Graphical desktop/Other
Requires: libdqt6-core = %_dqt6_version libdqt6-gui = %_dqt6_version libdqt6-opengl = %_dqt6_version

%description -n deepin-qt6platform-plugins
%repo is the %summary.

%prep
%setup -n %repo-%version
%patch0 -p1
%patch1 -p1
rm -r xcb/libqt5xcbqpa-dev xcb/libqt6xcbqpa-dev wayland/qtwayland-dev
# Unsupported by upstream.
sed -i '/wayland/d' CMakeLists.txt

%build
%if_with clang
%define optflags_lto -flto=thin
export CC=clang
export CXX=clang++
export LDFLAGS="-fuse-ld=lld $LDFLAGS"
%endif

echo "Start DTK6 build."
%DQ6build \
  -DDTK5=OFF \
  -DCMAKE_INSTALL_LIBDIR=%_lib \
  -DCMAKE_INSTALL_PREFIX=%_prefix \
  -DQT_XCB_PRIVATE_HEADERS=%_dqt6_headerdir/QtXcb \
  -DPLUGIN_INSTALL_DIR=%_dqt6_plugindir \
  -DDTK_VERSION=%version \
#

echo "Start DTK5 build."
export CMAKE_PREFIX_PATH=%_dqt5_libdir/cmake/Qt5:%_dqt5_libdir:$CMAKE_PREFIX_PATH
export PATH=%_dqt5_bindir:$PATH
%cmake \
  -GNinja \
  -DDTK5=ON \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCMAKE_SKIP_INSTALL_RPATH:BOOL=no \
  -DCMAKE_INSTALL_RPATH=%_dqt5_libdir \
  -DCMAKE_INSTALL_LIBDIR=%_lib \
  -DCMAKE_INSTALL_PREFIX=%_prefix \
  -DQT_XCB_PRIVATE_HEADERS=%_dqt5_headerdir/QtXcb \
  -DPLUGIN_INSTALL_DIR=%_dqt5_plugindir \
#
cmake --build %_cmake__builddir -j%__nprocs

%install
%DQ6install
%cmake_install

%files
%doc CHANGELOG.md README.md
%doc LICENSE
%_dqt5_plugindir/platforms/libdxcb.so

%files -n deepin-qt6platform-plugins
%doc CHANGELOG.md README.md
%doc LICENSE
%_dqt6_plugindir/platforms/libdxcb.so

%changelog
* Tue Jun 09 2026 Leontiy Volodin <lvol@altlinux.org> 6.7.43-alt1
- New version 6.7.43.

* Thu May 14 2026 Leontiy Volodin <lvol@altlinux.org> 6.7.41-alt1
- New version 6.7.41.

* Wed Apr 15 2026 Leontiy Volodin <lvol@altlinux.org> 6.7.39-alt1
- New version 6.7.39.

* Thu Feb 26 2026 Leontiy Volodin <lvol@altlinux.org> 6.7.33-alt1
- New version 6.7.33.

* Thu Feb 19 2026 Leontiy Volodin <lvol@altlinux.org> 6.7.32-alt2
- Fixed build on shrinked dQt buildrequires.

* Fri Jan 23 2026 Leontiy Volodin <lvol@altlinux.org> 6.7.32-alt1
- New version 6.7.32.
- Unified dtk5 and dtk6 modules.

* Wed Dec 10 2025 Leontiy Volodin <lvol@altlinux.org> 5.7.29-alt1
- New version 5.7.29.

* Fri Nov 07 2025 Leontiy Volodin <lvol@altlinux.org> 5.7.26-alt1
- New version 5.7.26.

* Fri Oct 24 2025 Leontiy Volodin <lvol@altlinux.org> 5.7.24-alt1
- New version 5.7.24.

* Wed Oct 15 2025 Leontiy Volodin <lvol@altlinux.org> 5.7.23-alt1
- New version 5.7.23.

* Tue May 06 2025 Leontiy Volodin <lvol@altlinux.org> 5.7.14-alt2
- Built without outdated dwayland.

* Wed Apr 30 2025 Leontiy Volodin <lvol@altlinux.org> 5.7.14-alt1
- New version 5.7.14.

* Thu Jan 30 2025 Leontiy Volodin <lvol@altlinux.org> 5.7.9-alt1
- New version 5.7.9.
- Added vcs tag.

* Wed Oct 23 2024 Leontiy Volodin <lvol@altlinux.org> 5.6.34-alt1
- New version 5.6.34.

* Thu May 09 2024 Leontiy Volodin <lvol@altlinux.org> 5.6.28-alt1
- New version 5.6.28.
- Built via separate qt5 instead system (ALT #48138).

* Fri Mar 29 2024 Leontiy Volodin <lvol@altlinux.org> 5.6.26-alt1
- New version 5.6.26.

* Wed Mar 20 2024 Leontiy Volodin <lvol@altlinux.org> 5.6.25-alt1
- New version 5.6.25.

* Tue Feb 06 2024 Leontiy Volodin <lvol@altlinux.org> 5.6.22-alt1
- New version 5.6.22.

* Fri Jan 19 2024 Leontiy Volodin <lvol@altlinux.org> 5.6.20-alt2
- Requires: libqt5-core = %%_qt5_version.

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
