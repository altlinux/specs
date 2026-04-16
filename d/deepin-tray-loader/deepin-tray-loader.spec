%define repo dde-tray-loader
%define soverdti 2
%define _libexecdir %_prefix/libexec

Name: deepin-tray-loader
Version: 2.0.29
Release: alt1

Summary: Tray plugins that integrated into task bar for DDE

License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-tray-loader
Vcs: https://github.com/linuxdeepin/dde-tray-loader

# Source-url: %url/archive/%version/%repo-%version.tar.gz
Source: %repo-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-ninja rpm-macros-dqt6
BuildRequires: gcc-c++ extra-cmake-modules dqt6-base-devel dqt6-tools-devel dqt6-svg-devel dtk6-common-devel libdtk6widget-devel libxcbutil-image-devel libxcbutil-devel libXtst-devel libxcbutil-icccm-devel libXcursor-devel libudev-devel libcups-devel libgio-devel kf6-kwindowsystem-devel
BuildRequires: dqt6-wayland-devel libwayland-egl-devel libwayland-server-devel
BuildRequires: vulkan-headers libdqt6-concurrent

Requires: libdqt6-gui = %_dqt6_version libdqt6-waylandclient = %_dqt6_version

%description
The project provides a set of tray plugins that integrated
into task bar and the tool loader which can load the plugins.

%package -n dde-wirelesscasting-plugin
Summary: dde-wirelesscasting-plugin for dde-dock
Group: Graphical desktop/Other

%description -n dde-wirelesscasting-plugin
DDE wirelesscasting plugin for dde-dock.

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

%prep
%setup -n %repo-%version
%patch -p1
sed -i '/LIBRARY DESTINATION/s|lib/dde-dock|${LIB_DESTINATION}/dde-dock|' \
  $(find ./plugins -name '*CMakeLists.txt')

%build
%DQ6build \
  -DBUILD_SHARED_LIBS=ON \
  -DLIB_DESTINATION=%_lib \
  -DCMAKE_INSTALL_SYSCONFDIR=%_sysconfdir \
  -DCMAKE_PREFIX_PATH=%_dqt6_libdir/cmake \
  -DKDE_INSTALL_QTPLUGINDIR=%_dqt6_plugindir

%install
%DQ6install
%find_lang --with-qt dde-dock
%find_lang --with-qt dock-wirelesscasting-plugin
%find_lang --with-qt trayplugin-loader

%files -f trayplugin-loader.lang
%doc README* debian/changelog
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
%dir %_sysconfdir/dde-dock/
%dir %_sysconfdir/dde-dock/indicator/
%config(noreplace) %_sysconfdir/dde-dock/indicator/keybord_layout.json
%dir %_libdir/dde-dock/
%dir %_libdir/dde-dock/plugins/
%_libdir/dde-dock/plugins/*.so
%exclude %_libdir/dde-dock/plugins/libdock-wirelesscasting-plugin.so
%dir %_libdir/dde-dock/plugins/system-trays/
%_libdir/dde-dock/plugins/system-trays/*.so
%dir %_datadir/dde-dock/
%dir %_datadir/dde-dock/icons/
%dir %_datadir/dde-dock/icons/dcc-setting/
%_datadir/dde-dock/icons/dcc-setting/*.dci
%exclude %_datadir/dde-dock/icons/dcc-setting/dcc-wireless-casting.dci
# The translations outside find_lang
%dir %_datadir/dde-dock/translations/
%_datadir/dde-dock/translations/dde-dock.qm
%_datadir/dde-dock/translations/dde-dock_ky@Arab.qm
# ---
%dir %_datadir/dsg/
%dir %_datadir/dsg/configs/
%dir %_datadir/dsg/configs/org.deepin.dde.dock/
%_datadir/dsg/configs/org.deepin.dde.dock/*.json

%files -n dde-dock-devel
%dir %_includedir/dde-dock/
%_includedir/dde-dock/*.h
%dir %_libdir/cmake/DdeDock/
%_libdir/cmake/DdeDock/DdeDockConfig.cmake
%_pkgconfigdir/dde-dock.pc

%files -n dde-wirelesscasting-plugin -f dock-wirelesscasting-plugin.lang
# The translations outside find_lang
%dir %_datadir/dock-wirelesscasting-plugin/
%dir %_datadir/dock-wirelesscasting-plugin/translations/
%_datadir/dock-wirelesscasting-plugin/translations/dock-wirelesscasting-plugin.qm
%_datadir/dock-wirelesscasting-plugin/translations/dock-wirelesscasting-plugin_ky@Arab.qm
# ---
%dir %_libdir/dde-dock/
%dir %_libdir/dde-dock/plugins/
%_libdir/dde-dock/plugins/libdock-wirelesscasting-plugin.so
%dir %_datadir/dde-dock/
%dir %_datadir/dde-dock/icons/
%dir %_datadir/dde-dock/icons/dcc-setting/
%_datadir/dde-dock/icons/dcc-setting/dcc-wireless-casting.dci

%changelog
* Thu Apr 16 2026 Leontiy Volodin <lvol@altlinux.org> 2.0.29-alt1
- New version 2.0.29.

* Thu Feb 26 2026 Leontiy Volodin <lvol@altlinux.org> 2.0.20-alt2
- Fixed build on shrinked dqt6.

* Fri Dec 26 2025 Leontiy Volodin <lvol@altlinux.org> 2.0.20-alt1
- New version 2.0.20.

* Fri Dec 19 2025 Leontiy Volodin <lvol@altlinux.org> 2.0.19-alt1
- New version 2.0.19.

* Mon Dec 15 2025 Leontiy Volodin <lvol@altlinux.org> 2.0.18-alt1
- New version 2.0.18.

* Mon Dec 01 2025 Leontiy Volodin <lvol@altlinux.org> 2.0.17-alt1
- New version 2.0.17.

* Mon Nov 17 2025 Leontiy Volodin <lvol@altlinux.org> 2.0.16-alt1
- New version 2.0.16.

* Fri Oct 31 2025 Leontiy Volodin <lvol@altlinux.org> 2.0.15-alt1
- New version 2.0.15.

* Thu Oct 23 2025 Leontiy Volodin <lvol@altlinux.org> 2.0.13-alt1
- New version 2.0.13.

* Fri Oct 03 2025 Leontiy Volodin <lvol@altlinux.org> 2.0.12-alt1
- New version 2.0.12.

* Wed Sep 24 2025 Leontiy Volodin <lvol@altlinux.org> 2.0.11-alt1
- New version 2.0.11.
- Packaged dde-wirelesscasting-plugin separately.

* Tue Sep 16 2025 Leontiy Volodin <lvol@altlinux.org> 2.0.10-alt1
- New version 2.0.10.

* Fri Aug 01 2025 Leontiy Volodin <lvol@altlinux.org> 2.0.5-alt1
- New version 2.0.5.

* Fri Jun 20 2025 Leontiy Volodin <lvol@altlinux.org> 2.0.1-alt1
- New version 2.0.1.

* Wed Mar 05 2025 Leontiy Volodin <lvol@altlinux.org> 1.99.14-alt1
- Initial build for ALT Sisyphus (for deepin-session).
- Obsoleted deepin-dock.
