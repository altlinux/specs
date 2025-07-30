%define _libexecdir %_prefix/libexec

Name: deepin-screensaver
Version: 6.5.2
Release: alt1
Summary: Screensaver Tool
License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/deepin-screensaver
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-dqt6
# Automatically added by buildreq on Wed Jul 30 2025
# optimized out: cmake cmake-modules dqt6-base-devel dqt6-tools gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libX11-devel libdouble-conversion3 libdqt6-core libdqt6-core5compat libdqt6-dbus libdqt6-gui libdqt6-network libdqt6-opengl libdqt6-printsupport libdqt6-qml libdqt6-qmlmeta libdqt6-qmlmodels libdqt6-qmlworkerscript libdqt6-quick libdqt6-waylandclient libdqt6-widgets libdqt6-xml libdtk6core-devel libdtk6gui-devel libdtk6log-devel libglvnd-devel libgpg-error libp11-kit libsasl2-3 libssl-devel libstartup-notification libstdc++-devel libwayland-client libwayland-cursor libxcb-devel libxkbcommon-devel ninja-build pkg-config python3 python3-base sh5 vulkan-headers xorg-proto-devel
BuildRequires: gcc-c++ dqt6-5compat-devel dqt6-declarative-devel dqt6-tools-devel dtk6-common-devel libXScrnSaver-devel libXext-devel libcups-devel libdtk6widget-devel
# BuildRequires: xscreensaver-modules xscreensaver-modules-gl

Requires: libdqt6-gui = %_dqt6_version

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
%autopatch -p1
sed -i 's|/lib/|/libexec/|' \
  common.pri \
  xscreensaver/xscreensaver.pro \
  CMakeLists.txt \
  customscreensaver/deepin-custom-screensaver/CMakeLists.txt \
  customscreensaver/deepin-custom-screensaver/data/deepin-custom-screensaver.desktop \
  customscreensaver/deepin-custom-screensaver/deepin-custom-screensaver.pro \
  customscreensaver/saverpic/CMakeLists.txt \
  tools/preview/main.cpp \
  xscreensaver/CMakeLists.txt
sed -i 's|/etc/os-version|/etc/uos-version|' \
  common.pri
sed -i '/QT_LRELEASE/s|/lib/qt${QT_VERSION_MAJOR}/bin/lrelease|%_dqt6_bindir/lrelease|' \
  cmake/translation-generate.cmake

%build
%DQ6build \
    -DXSCREENSAVER_DATA_PATH=%_libexecdir/xscreensaver \
    -DMODULE_PATH=%_libexecdir/%name/modules \
#

%install
%DQ6install

%files
%doc CHANGELOG.md
%_bindir/%{name}*
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
%dir %_datadir/dconfig/
%dir %_datadir/dconfig/overrides/
%dir %_datadir/dconfig/overrides/org.deepin.screensaver/
%_datadir/dconfig/overrides/org.deepin.screensaver/org.deepin.customscreensaver.json

%files modules
%dir %_libexecdir/%name/
%_libexecdir/%name/modules/

%changelog
* Wed Jul 30 2025 Leontiy Volodin <lvol@altlinux.org> 6.5.2-alt1
- New version 6.5.2.
- Switched to Qt 6.

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
