%define _libexecdir %_prefix/libexec

Name: deepin-screensaver
Version: 5.0.20.0.2.522b
Release: alt1
Summary: Screensaver Tool
License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/deepin-screensaver
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz

BuildRequires: gcc-c++ dqt5-base-devel dqt5-tools dqt5-x11extras-devel dqt5-declarative-devel libXScrnSaver-devel libdtkwidget-devel deepin-qt-dbus-factory-devel deepin-desktop-base
# BuildRequires: xscreensaver-modules xscreensaver-modules-gl

%description
Deepin screensaver viewer and tools.

%package modules
Summary: Screensaver modules
Group: Graphical desktop/Other
# BuildArch: noarch
AutoReq: no
Requires: xscreensaver-modules xscreensaver-modules-gl

%description modules
Extra modules for Deepin Screensaver.

%prep
%setup
sed -i 's|/lib/|/libexec/|' \
  common.pri \
  xscreensaver/xscreensaver.pro
sed -i 's|/usr/lib|%_libexecdir|' \
  common.pri \
  tools/preview/main.cpp \
  customscreensaver/deepin-custom-screensaver/deepin-custom-screensaver.pro
sed -i 's|/etc/os-version|/etc/uos-version|' \
  common.pri

%build
export QMAKE=qmake-dqt5
export PATH=%_dqt5_bindir:$PATH
%qmake_dqt5 \
    DEFINES+="VERSION=%version" \
    VERSION=%version \
    CONFIG+=nostrip \
    PREFIX=%_prefix \
    XSCREENSAVER_DATA_PATH=%_libexecdir/xscreensaver \
    MODULE_PATH=%_libexecdir/%name/modules \
    QMAKE_RPATHDIR=%_dqt5_libdir \
#
%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot

%files
%doc CHANGELOG.md
%_bindir/%name
%_datadir/dbus-1/services/*
%_datadir/dbus-1/interfaces/*
%_datadir/%name/
%_datadir/deepin-custom-screensaver/
%dir %_sysconfdir/%name/
%dir %_sysconfdir/%name/deepin-custom-screensaver/
%_sysconfdir/%name/deepin-custom-screensaver/deepin-custom-screensaver*
%dir %_datadir/dsg/
%dir %_datadir/dsg/configs/
%dir %_datadir/dsg/configs/org.deepin.screensaver/
%_datadir/dsg/configs/org.deepin.screensaver/*.json

%files modules
%dir %_libexecdir/%name/
%_libexecdir/%name/modules/

%changelog
* Wed Sep 25 2024 Leontiy Volodin <lvol@altlinux.org> 5.0.20.0.2.522b-alt1
- New version 5.0.20-2-g522bb08.
- Built via separate qt5 instead system (ALT #48138).

* Tue Apr 25 2023 Leontiy Volodin <lvol@altlinux.org> 5.0.16-alt1
- New version 5.0.16.

* Mon Jun 20 2022 Leontiy Volodin <lvol@altlinux.org> 5.0.10-alt1
- New version.
- Upstream:
  + chore: Optimize the construction-based dependence and add man manual.
  + feat: Add the function of defining pictures as screen guarantees.
  + fix: bug6339: In the state of screen guarantee, insert behind the extended
  screen, the extended screen does not display the screen guarantee.
  + fix: The screen preservation window of the preview will take away the focus
  of the desktop screen protection setting window when activating.

* Fri Jun 18 2021 Leontiy Volodin <lvol@altlinux.org> 5.0.5-alt1
- New version (5.0.5).

* Fri Sep 11 2020 Leontiy Volodin <lvol@altlinux.org> 5.0.4-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
