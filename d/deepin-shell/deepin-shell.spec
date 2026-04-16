%define repo dde-shell
%define sover 1

%def_without clang

Name: deepin-shell
Version: 2.0.37
Release: alt1

Summary: Plugins for DDE

License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-shell
Vcs: https://github.com/linuxdeepin/dde-shell

# Source-url: %url/archive/%version/%repo-%version.tar.gz
Source: %repo-%version.tar
Patch0: %name-%version-%release.patch
Patch1: deepin-shell-2.0.3-alt-fixes-bad-symbols.patch

BuildRequires(pre): rpm-build-ninja rpm-macros-dqt6 patchelf
BuildRequires: cmake extra-cmake-modules dqt6-base-devel dqt6-tools-devel dqt6-5compat-devel dqt6-declarative-devel dqt6-wayland-devel libdqt6-waylandcompositor dtk6-common-devel libdtk6widget-devel wayland-protocols libwayland-egl-devel libwayland-server-devel libxcbutil-icccm-devel libXtst-devel libxcbutil-devel libsystemd-devel libyaml-cpp-devel deepin-tray-loader-devel dde-dock-devel libcups-devel treeland-protocols deepin-application-manager-devel libicu-devel libgtest-devel
BuildRequires: libdqt6-qmlcompiler dqt6-sql-interbase dqt6-sql-mysql dqt6-sql-odbc dqt6-sql-postgresql libdqt6-waylandeglcompositorhwintegration vulkan-headers libdqt6-test libdqt6-quicktemplates2 libdqt6-wlshellintegration
%if_with clang
BuildRequires: clang-devel
%else
BuildRequires: gcc-c++
%endif

Requires: libdqt6-gui = %_dqt6_version
Requires: libdqt6-qml = %_dqt6_version
Requires: libdqt6-quicktemplates2 = %_dqt6_version
Requires: libdqt6-waylandclient = %_dqt6_version
Requires: libdqt6-waylandcompositor = %_dqt6_version

%description
The dde-shell project provides a plugin system that integrates
plugins developed based on this plugin system into DDE.

%package -n lib%repo%sover
Summary: Library for %name
Group: System/Libraries
Requires: libdqt6-gui = %_dqt6_version
Requires: libdqt6-quick = %_dqt6_version
Requires: libdqt6-quicktemplates2 = %_dqt6_version
Requires: libdqt6-waylandclient = %_dqt6_version

%description -n lib%repo%sover
Library for %name.

%package -n lib%repo-devel
Summary: Development package for %name
Group: Development/C++

%description -n lib%repo-devel
Header files and libraries for %name.

%package -n libds-notification-shared%sover
Summary: Library for %name
Group: System/Libraries

%description -n libds-notification-shared%sover
Library for %name.

%package -n libds-notification-shared-devel
Summary: Development package for libds-notification-shared
Group: Development/C++

%description -n libds-notification-shared-devel
Header files and libraries for libds-notification-shared.

%prep
%setup -n %repo-%version
%autopatch -p1
sed -i 's|/usr/lib/dde-dock/plugins/|%_libdir/dde-dock/plugins/|g' \
  panels/dock/loadtrayplugins.h

%build
%if_with clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
export NM="llvm-nm"
export READELF="llvm-readelf"
%endif
export CPLUS_INCLUDE_PATH=%_dqt6_headerdir/QtQuickTemplates2/%_dqt6_version:$CPLUS_INCLUDE_PATH
%DQ6build \
    -DINCLUDE_INSTALL_DIR=%_includedir/%repo \
    -DDS_BUILD_WITH_QT6:BOOL=ON \
    -DQML_INSTALL_DIR=%_lib/dqt6/qml \
#

%install
%DQ6install
%find_lang --with-qt %repo
patchelf %buildroot%_dqt6_qmldir/org/deepin/ds/notificationcenter/libnotificationcenterpanelplugin.so --add-rpath %_libdir/dde-shell

%files -f %repo.lang
%doc README.md LICENSE debian/changelog
%_bindir/%repo
%_userunitdir/%{repo}*.service
%dir %_libdir/dde-shell/
%_libdir/dde-shell/org.deepin.ds*.so
%dir %_dqt6_qmldir/org/deepin/
%dir %_dqt6_qmldir/org/deepin/ds/
%_dqt6_qmldir/org/deepin/ds/*
%dir %_datadir/dde-dock/
%dir %_datadir/dde-dock/icons/
%dir %_datadir/dde-dock/icons/dcc-setting/
%_datadir/dde-dock/icons/dcc-setting/*.dci
%dir %_datadir/%repo/
%dir %_datadir/%repo/org.deepin.ds*/
%_datadir/%repo/org.deepin.ds*/*.json
%_datadir/%repo/org.deepin.ds*/*.qml
%_datadir/%repo/org.deepin.ds*/icons/
%dir %_datadir/deepin-debug-config/
%dir %_datadir/deepin-debug-config/deepin-debug-config.d/
%_datadir/deepin-debug-config/deepin-debug-config.d/org.deepin.dde.shell.json
%dir %_datadir/deepin-log-viewer/
%dir %_datadir/deepin-log-viewer/deepin-log.conf.d/
%_datadir/deepin-log-viewer/deepin-log.conf.d/org.deepin.dde.shell.json
# the translations outside find_land
%dir %_datadir/%repo/org.deepin.ds*/translations/
%_datadir/%repo/org.deepin.ds.dock/translations/org.deepin.ds.dock.qm
%_datadir/%repo/org.deepin.ds.notificationbubble/translations/org.deepin.ds.notificationbubble.qm
%_datadir/%repo/org.deepin.ds.notificationcenter/translations/org.deepin.ds.notificationcenter.qm
%_datadir/%repo/org.deepin.ds.dock.multitaskview/translations/org.deepin.ds.dock.multitaskview.qm
%_datadir/%repo/org.deepin.ds.dock.showdesktop/translations/org.deepin.ds.dock.showdesktop.qm
%_datadir/%repo/org.deepin.ds.dock.taskmanager/translations/org.deepin.ds.dock.taskmanager.qm
%_datadir/%repo/org.deepin.ds.dock.tray/translations/org.deepin.ds.dock.tray.qm
%_datadir/%repo/org.deepin.ds.osd.default/translations/org.deepin.ds.osd.default.qm
%_datadir/%repo/org.deepin.ds.osd.displaymode/translations/org.deepin.ds.osd.displaymode.qm
%_datadir/%repo/org.deepin.ds.osd.windoweffect/translations/org.deepin.ds.osd.windoweffect.qm
# ---
%dir %_datadir/%repo/org.deepin.ds.example.applet/control/
%_datadir/%repo/org.deepin.ds.example.applet/control/TextEx.qml
%dir %_datadir/dsg/
%dir %_datadir/dsg/configs/
%dir %_datadir/dsg/configs/org.deepin.dde.shell/
%_datadir/dsg/configs/org.deepin.dde.shell/*.json
%dir %_datadir/dsg/configs/org.deepin.ds.dock/
%_datadir/dsg/configs/org.deepin.ds.dock/*.json
%dir %_datadir/dsg/configs/overrides/
%dir %_datadir/dsg/configs/overrides/org.deepin.dde.shell/
%dir %_datadir/dsg/configs/overrides/org.deepin.dde.shell/org.deepin.dtk.preference/
%_datadir/dsg/configs/overrides/org.deepin.dde.shell/org.deepin.dtk.preference/org.deepin.dtk.preference.json

%files -n lib%repo%sover
%_libdir/lib%repo.so.%{sover}*

%files -n lib%repo-devel
%_libdir/lib%repo.so
%dir %_includedir/%repo/
%_includedir/%repo/*.h
%dir %_libdir/cmake/DDEShell/
%_libdir/cmake/DDEShell/DDEShell*.cmake

%files -n libds-notification-shared%sover
%_libdir/libds-notification-shared.so.%{sover}*

%files -n libds-notification-shared-devel
%_libdir/libds-notification-shared.so

%changelog
* Thu Apr 16 2026 Leontiy Volodin <lvol@altlinux.org> 2.0.37-alt1
- New version 2.0.37.

* Thu Feb 26 2026 Leontiy Volodin <lvol@altlinux.org> 2.0.27-alt2
- Fixed build on shrinked dqt6.

* Tue Jan 27 2026 Leontiy Volodin <lvol@altlinux.org> 2.0.27-alt1
- New version 2.0.27.

* Fri Jan 16 2026 Leontiy Volodin <lvol@altlinux.org> 2.0.26-alt1
- New version 2.0.26.

* Fri Dec 26 2025 Leontiy Volodin <lvol@altlinux.org> 2.0.24-alt1
- New version 2.0.24.

* Fri Dec 19 2025 Leontiy Volodin <lvol@altlinux.org> 2.0.23-alt1
- New version 2.0.23.

* Mon Dec 15 2025 Leontiy Volodin <lvol@altlinux.org> 2.0.22-alt1
- New version 2.0.22.

* Fri Dec 05 2025 Leontiy Volodin <lvol@altlinux.org> 2.0.21-alt1
- New version 2.0.21.

* Mon Nov 24 2025 Leontiy Volodin <lvol@altlinux.org> 2.0.19-alt2
- Fixed circular dependencies.

* Tue Nov 18 2025 Leontiy Volodin <lvol@altlinux.org> 2.0.19-alt1
- New version 2.0.19.

* Fri Nov 07 2025 Leontiy Volodin <lvol@altlinux.org> 2.0.17-alt1
- New version 2.0.17.

* Thu Oct 23 2025 Leontiy Volodin <lvol@altlinux.org> 2.0.14-alt1
- New version 2.0.14.

* Fri Oct 03 2025 Leontiy Volodin <lvol@altlinux.org> 2.0.12-alt1
- New version 2.0.12.

* Tue Sep 23 2025 Leontiy Volodin <lvol@altlinux.org> 2.0.11-alt1
- New version 2.0.11.

* Mon Sep 15 2025 Leontiy Volodin <lvol@altlinux.org> 2.0.9-alt1
- New version 2.0.9.

* Tue Aug 26 2025 Leontiy Volodin <lvol@altlinux.org> 2.0.7-alt1
- New version 2.0.7.

* Fri Aug 15 2025 Leontiy Volodin <lvol@altlinux.org> 2.0.6-alt1
- New version 2.0.6.

* Thu Aug 07 2025 Leontiy Volodin <lvol@altlinux.org> 2.0.5-alt1
- New version 2.0.5.

* Fri Aug 01 2025 Leontiy Volodin <lvol@altlinux.org> 2.0.4-alt1
- New version 2.0.4.

* Tue Jul 29 2025 Leontiy Volodin <lvol@altlinux.org> 2.0.3-alt2
- Fixed dde-dock plugin detection.

* Mon Jul 21 2025 Leontiy Volodin <lvol@altlinux.org> 2.0.3-alt1
- New version 2.0.3.

* Tue Jun 24 2025 Leontiy Volodin <lvol@altlinux.org> 2.0.1-alt1
- New version 2.0.1.

* Tue Mar 04 2025 Leontiy Volodin <lvol@altlinux.org> 1.0.10-alt1
- Initial build for ALT Sisyphus (for deepin-session).
