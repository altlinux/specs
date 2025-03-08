%define repo dde-tray-loader
%define soverdti 0
%define _libexecdir %_prefix/libexec

Name: deepin-tray-loader
Version: 1.99.14
Release: alt1

Summary: Tray plugins that integrated into task bar for DDE

License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-tray-loader
Vcs: git://github.com/linuxdeepin/dde-tray-loader.git

Source: %url/archive/%version/%repo-%version.tar.gz

BuildRequires(pre): rpm-build-ninja rpm-macros-dqt6
BuildRequires: gcc-c++ extra-cmake-modules dqt6-base-devel dqt6-tools-devel dqt6-svg-devel dtk6-common-devel libdtk6widget-devel libxcbutil-image-devel libxcbutil-devel libXtst-devel libxcbutil-icccm-devel libXcursor-devel libudev-devel libcups-devel kf6-networkmanager-qt-devel
BuildRequires: dqt6-wayland-devel libwayland-egl-devel

Requires: libdqt6-gui = %_dqt6_version libdqt6-waylandclient = %_dqt6_version

%description
The project provides a set of tray plugins that integrated
into task bar and the tool loader which can load the plugins.

%package -n libdde-trayplugin-interface%soverdti
Summary: Library for %name
Group: System/Libraries

%description -n libdde-trayplugin-interface%soverdti
Library for %name.

%package -n libdde-trayplugin-interface-devel
Summary: Development package for dde-trayplugin-interface library
Group: Development/C++

%description -n libdde-trayplugin-interface-devel
Header files and libraries for dde-trayplugin-interface library.

%package -n dde-dock
Summary: Deepin desktop-environment - Dock module
Group: Graphical desktop/Other
Provides: deepin-dock
Obsoletes: deepin-dock

%description -n dde-dock
Deepin desktop-environment - Dock module.

%package -n dde-dock-devel
Summary: Development package for dde-dock
Group: Development/C++
Provides: deepin-dock-devel
Obsoletes: deepin-dock-devel

%description -n dde-dock-devel
Header files and libraries for dde-dock.

%package devel
Summary: Development package for %name
Group: Development/C++

%description devel
Header files and libraries for %name.

%package -n libdde-tray-network-core-devel
Summary: Development package for dde-tray-network-core plugin
Group: Development/C++

%description -n libdde-tray-network-core-devel
Header files and libraries for dde-tray-network-core plugin.

%prep
%setup -n %repo-%version
%autopatch -p1
sed -i '/LIBRARY DESTINATION/s|lib/dde-dock|${LIB_DESTINATION}/dde-dock|' \
  $(find ./plugins -name '*CMakeLists.txt')

%build
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
export LC_ALL=C.UTF-8
%DQ6build \
  -DBUILD_SHARED_LIBS=ON \
  -DLIB_DESTINATION=%_lib \
  -DCMAKE_INSTALL_SYSCONFDIR=%_sysconfdir \
  -DCMAKE_PREFIX_PATH=%_prefix \
  -DKF6_QT_LIBRARIES=%_libdir/kf6/devel \
  -DKDE_INSTALL_QTPLUGINDIR=%_dqt6_plugindir

%install
%DQ6install
%find_lang --with-qt --output=dde-dock.lang dde-dock dde-tray-network-core dock-tray-network-plugin dock-wirelesscasting-plugin
%find_lang --with-qt trayplugin-loader

%files -f trayplugin-loader.lang
%doc README*
%_libexecdir/trayplugin-loader
%_dqt6_plugindir/wayland-shell-integration/libplugin-shell.so
%dir %_datadir/dsg/
%dir %_datadir/dsg/configs/
%dir %_datadir/dsg/configs/org.deepin.dde.tray-loader/
%_datadir/dsg/configs/org.deepin.dde.tray-loader/*.json
%dir %_datadir/trayplugin-loader/
%dir %_datadir/trayplugin-loader/translations/
%_datadir/trayplugin-loader/translations/trayplugin-loader.qm

%files devel
%dir %_includedir/%repo/
%dir %_includedir/%repo/protocol/
%_includedir/%repo/protocol/plugin-manager-v1.xml
%dir %_libdir/cmake/DdeTrayLoader/
%_libdir/cmake/DdeTrayLoader/DdeTrayLoaderConfig.cmake
%_pkgconfigdir/dde-tray-loader.pc

%files -n libdde-trayplugin-interface%soverdti
%_libdir/libdde-trayplugin-interface.so.%{soverdti}*

%files -n libdde-trayplugin-interface-devel
%_libdir/libdde-trayplugin-interface.so

%files -n dde-dock -f dde-dock.lang
%config(noreplace) %_sysconfdir/dde-dock/indicator/keybord_layout.json
%dir %_libdir/dde-dock/
%dir %_libdir/dde-dock/plugins/
%_libdir/dde-dock/plugins/*.so
%dir %_libdir/dde-dock/plugins/system-trays/
%_libdir/dde-dock/plugins/system-trays/*.so
%dir %_datadir/dde-dock/
%dir %_datadir/dde-dock/icons/
%dir %_datadir/dde-dock/icons/dcc-setting/
%_datadir/dde-dock/icons/dcc-setting/*.dci
# The translations outside find_lang
%dir %_datadir/dde-dock/translations/
%_datadir/dde-dock/translations/dde-dock.qm
%_datadir/dde-dock/translations/dde-dock_es_419.qm
%_datadir/dde-dock/translations/dde-dock_ky@Arab.qm
%dir %_datadir/dock-wirelesscasting-plugin/
%dir %_datadir/dock-wirelesscasting-plugin/translations/
%_datadir/dock-wirelesscasting-plugin/translations/dock-wirelesscasting-plugin.qm
%_datadir/dock-wirelesscasting-plugin/translations/dock-wirelesscasting-plugin_ky@Arab.qm
%dir %_datadir/dde-tray-network-core/
%dir %_datadir/dde-tray-network-core/translations/
%_datadir/dde-tray-network-core/translations/dde-network-core.qm
%_datadir/dde-tray-network-core/translations/dde-network-core_es_419.qm
%_datadir/dde-tray-network-core/translations/dde-network-core_ky@Arab.qm
%dir %_datadir/dock-tray-network-plugin/
%dir %_datadir/dock-tray-network-plugin/translations/
%_datadir/dock-tray-network-plugin/translations/dock-network-plugin.qm
%_datadir/dock-tray-network-plugin/translations/dock-network-plugin_es_419.qm
%_datadir/dock-tray-network-plugin/translations/dock-network-plugin_ky@Arab.qm
# ---
%dir %_datadir/dsg/
%dir %_datadir/dsg/configs/
%dir %_datadir/dsg/configs/org.deepin.dde.dock/
%_datadir/dsg/configs/org.deepin.dde.dock/*.json
%dir %_datadir/dsg/configs/org.deepin.dde.tray.network/
%_datadir/dsg/configs/org.deepin.dde.tray.network/org.deepin.dde.network.json

%files -n dde-dock-devel
%dir %_includedir/dde-dock/
%_includedir/dde-dock/*.h
%dir %_libdir/cmake/DdeDock/
%_libdir/cmake/DdeDock/DdeDockConfig.cmake
%_pkgconfigdir/dde-dock.pc

%files -n libdde-tray-network-core-devel
%_libdir/libdde-tray-network-core.a
%_includedir/libddetraynetworkcore/
%_pkgconfigdir/dde-tray-network-core.pc

%changelog
* Wed Mar 05 2025 Leontiy Volodin <lvol@altlinux.org> 1.99.14-alt1
- Initial build for ALT Sisyphus (for deepin-session).
- Obsoleted deepin-dock.
