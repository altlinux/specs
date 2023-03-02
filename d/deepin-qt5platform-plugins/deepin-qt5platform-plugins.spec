%define repo qt5platform-plugins

%def_disable clang

Name: deepin-qt5platform-plugins
Version: 5.6.5
Release: alt1
Summary: Qt platform integration plugins for Deepin Desktop Environment
License: GPL-2.0+ and LGPL-3.0 and MIT
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/qt5platform-plugins
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz
Patch: 0001-chore-load-dxcb-if-XDG_CURRENT_DESKTOP-set-to-DDE.patch

%if_enabled clang
BuildRequires(pre): clang-devel
%else
BuildRequires(pre): gcc-c++
%endif
BuildRequires: git-core
BuildRequires: libqt5-core
BuildRequires: qt5-x11extras-devel
BuildRequires: libcairo-devel
BuildRequires: libglvnd-devel
BuildRequires: libXi-devel
BuildRequires: libxcb-render-util-devel
BuildRequires: libxcbutil-image-devel
BuildRequires: libxcbutil-icccm-devel
BuildRequires: libxcbutil-keysyms-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: libxkbcommon-devel
BuildRequires: libSM-devel
BuildRequires: libdbus-devel
BuildRequires: libmtdev-devel
BuildRequires: qt5-wayland-devel
BuildRequires: kf5-kwayland-devel
# for libQt5EdidSupport.a
BuildRequires: qt5-base-devel-static

%description
%repo is the
%summary.

%prep
%setup -n %repo-%version
%patch -p1
# Disable wayland for now: https://github.com/linuxdeepin/qt5platform-plugins/issues/47
sed -i '/wayland/d' qt5platform-plugins.pro
rm -r xcb/libqt5xcbqpa-dev wayland/qtwayland-dev
sed -i 's|error(Not support Qt Version: .*)|INCLUDEPATH += %_qt5_headerdir/QtXcb|' xcb/linux.pri

%build
export PATH=%_qt5_bindir:$PATH
%qmake_qt5 \
%if_enabled clang
    QMAKE_STRIP= -spec linux-clang \
%endif
    CONFIG+=nostrip \
    PREFIX=%prefix \
    unix:LIBS+="-L/%_lib -ldl"
%make

%install
%makeinstall INSTALL_ROOT=%buildroot

%files
%doc CHANGELOG.md README.md
%doc LICENSE
%_qt5_plugindir/platforms/libdxcb.so

%changelog
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
