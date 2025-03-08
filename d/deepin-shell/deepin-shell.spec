%define repo dde-shell
%define sover 0

%def_without clang

Name: deepin-shell
Version: 1.0.10
Release: alt1

Summary: Plugins for DDE

License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-shell
Vcs: git://github.com/linuxdeepin/dde-shell.git

Source: %url/archive/%version/%repo-%version.tar.gz
Patch: deepin-shell-1.0.10-alt-fixes-override.patch

BuildRequires(pre): rpm-build-ninja rpm-macros-dqt6 patchelf
BuildRequires: cmake extra-cmake-modules dqt6-base-devel dqt6-tools-devel dqt6-5compat-devel dqt6-declarative-devel dqt6-wayland-devel libdqt6-waylandcompositor dtk6-common-devel libdtk6widget-devel wayland-protocols libwayland-egl-devel libwayland-server-devel libxcbutil-icccm-devel libXtst-devel libxcbutil-devel libsystemd-devel libyaml-cpp-devel deepin-tray-loader-devel dde-dock-devel libcups-devel treeland-protocols deepin-application-manager-devel
BuildRequires: libdqt6-qmlcompiler
%if_with clang
BuildRequires: clang-devel
%else
BuildRequires: gcc-c++
%endif

Requires: libdqt6-gui = %_dqt6_version libdqt6-waylandclient = %_dqt6_version

%description
The dde-shell project provides a plugin system that integrates
plugins developed based on this plugin system into DDE.

%package -n lib%repo%sover
Summary: Library for %name
Group: System/Libraries
Requires: libdqt6-gui = %_dqt6_version libdqt6-waylandclient = %_dqt6_version

%description -n lib%repo%sover
Library for %name.

%package -n lib%repo-devel
Summary: Development package for %name
Group: Development/C++

%description -n lib%repo-devel
Header files and libraries for %name.

%prep
%setup -n %repo-%version
%autopatch -p1

%build
%if_with clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
export NM="llvm-nm"
export READELF="llvm-readelf"
%endif
%DQ6build \
    -DINCLUDE_INSTALL_DIR=%_includedir/%repo \
    -DDS_BUILD_WITH_QT6:BOOL=ON \
    -DQML_INSTALL_DIR=%_lib/dqt6/qml \
#

%install
%DQ6install
%find_lang --with-qt %repo
patchelf %buildroot%_dqt6_qmldir/org/deepin/ds/dock/libdock-plugin.so --add-rpath %_libdir/dde-shell

%files -f %repo.lang
%doc README.md LICENSE
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
%_datadir/dde-dock/icons/dcc-setting/*.svg
%dir %_datadir/%repo/
%dir %_datadir/%repo/org.deepin.ds*/
%_datadir/%repo/org.deepin.ds*/*.json
%_datadir/%repo/org.deepin.ds*/*.qml
%_datadir/%repo/org.deepin.ds*/icons/
# the translations outside find_land
%dir %_datadir/%repo/org.deepin.ds*/translations/
%_datadir/%repo/org.deepin.ds.dock/translations/org.deepin.ds.dock.qm
%_datadir/%repo/org.deepin.ds.notification/translations/org.deepin.ds.notification.qm
%_datadir/%repo/org.deepin.ds.dock.clipboarditem/translations/org.deepin.ds.dock.clipboarditem.qm
%_datadir/%repo/org.deepin.ds.dock.launcheritem/translations/org.deepin.ds.dock.launcheritem.qm
%_datadir/%repo/org.deepin.ds.dock.multitaskview/translations/org.deepin.ds.dock.multitaskview.qm
%_datadir/%repo/org.deepin.ds.dock.searchitem/translations/org.deepin.ds.dock.searchitem.qm
%_datadir/%repo/org.deepin.ds.dock.showdesktop/translations/org.deepin.ds.dock.showdesktop.qm
%_datadir/%repo/org.deepin.ds.dock.taskmanager/translations/org.deepin.ds.dock.taskmanager.qm
%_datadir/%repo/org.deepin.ds.dock.tray/translations/org.deepin.ds.dock.tray.qm
%_datadir/%repo/org.deepin.ds.dock.workspaceitem/translations/org.deepin.ds.dock.workspaceitem.qm
%_datadir/%repo/org.deepin.ds.osd.default/translations/org.deepin.ds.osd.default.qm
%_datadir/%repo/org.deepin.ds.osd.displaymode/translations/org.deepin.ds.osd.displaymode.qm
# ---
%dir %_datadir/%repo/org.deepin.ds.example.applet/control/
%_datadir/%repo/org.deepin.ds.example.applet/control/TextEx.qml
%dir %_datadir/dsg/
%dir %_datadir/dsg/configs/
%dir %_datadir/dsg/configs/org.deepin.dde.shell/
%_datadir/dsg/configs/org.deepin.dde.shell/*.json
%dir %_datadir/dsg/configs/org.deepin.ds.dock/
%_datadir/dsg/configs/org.deepin.ds.dock/*.json

%files -n lib%repo%sover
%_libdir/lib%repo.so.%{sover}*

%files -n lib%repo-devel
%_libdir/lib%repo.so
%dir %_includedir/%repo/
%_includedir/%repo/*.h
%dir %_libdir/cmake/DDEShell/
%_libdir/cmake/DDEShell/DDEShell*.cmake

%changelog
* Tue Mar 04 2025 Leontiy Volodin <lvol@altlinux.org> 1.0.10-alt1
- Initial build for ALT Sisyphus (for deepin-session).
