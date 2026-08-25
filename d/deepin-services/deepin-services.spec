%def_disable clang
%def_without ipwatchd

%define repo dde-services
%define _libexecdir %_prefix/libexec

Name: deepin-services
Version: 1.0.41
Release: alt1

Summary: Manage DBus service on DDE

License: LGPL-3.0-or-later
Group: System/Configuration/Other
Url: https://github.com/linuxdeepin/dde-services
VCS: https://github.com/linuxdeepin/dde-services

# Source-url: https://github.com/linuxdeepin/dde-services/archive/%version/%repo-%version.tar.gz
Source: %repo-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-dqt6
BuildRequires: cmake rpm-build-python3 dqt6-base-devel dqt6-tools-devel dtk6-common-devel libdtk6gui-devel libX11-devel libwayland-client-devel libwayland-server-devel libwayland-egl-devel wayland-protocols wlr-protocols treeland-protocols libxcbutil-keysyms-devel libXtst-devel libdqt6-test vulkan-headers
%if_with ipwatchd
BuildRequires: libsystemd-devel glib2-devel libpcap-devel libnet2-devel
%endif
%if_enabled clang
BuildRequires: clang-devel
%else
BuildRequires: gcc-c++
%endif

%description
%summary.


%prep
%setup -n %repo-%version
%autopatch -p1

%build
%if_enabled clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
%endif
%DQ6build \
  -DCMAKE_INSTALL_SYSCONFDIR=%_sysconfdir \
  -DLIB_DESTINATION=%_lib \
%if_with ipwatchd
  -DENABLE_PLUGIN_IPWATCHD=ON \
%else
  -DENABLE_PLUGIN_IPWATCHD=OFF \
%endif
#

%install
%DQ6install
%find_lang --with-qt --output=dservices.lang org.deepin.dde.keybinding org.deepin.dde.shortcut.dde-app plugin-power-session

%files -f dservices.lang
%doc LICENSE README.md debian/changelog
%_bindir/dde-shortcut-tool
%_bindir/extract_shortcuts_i18n
%dir %_libexecdir/dde-services/
%dir %_libexecdir/dde-services/keybinding/
%_libexecdir/dde-services/keybinding/camera-switch
%_libexecdir/dde-services/keybinding/toggle-grand-search
%dir %_libdir/deepin-service-manager/
%_libdir/deepin-service-manager/libplugin-qt-thememanager.so
%_libdir/deepin-service-manager/libplugin-qt-wallpaperslideshow.so
%_libdir/deepin-service-manager/libplugin-dde-xsettings.so
%_libdir/deepin-service-manager/libplugin-dde-shortcut.so
%_libdir/deepin-service-manager/libplugin-power-session.so
%_libdir/deepin-service-manager/libplugin-qt-wallpapercache.so
%_libdir/deepin-service-manager/libplugin-ambient-brightness.so
%dir %_datadir/deepin-service-manager/
%dir %_datadir/deepin-service-manager/system/
%_datadir/deepin-service-manager/system/plugin-qt-wallpapercache.json

%if_with ipwatchd
%_bindir/ipwatchd
%_libdir/deepin-service-manager/libplugin-ipwatchd.so
%_datadir/dbus-1/system.d/org.deepin.ipwatchd.conf
%_datadir/deepin-service-manager/system/plugin-ipwatchd.json
%dir %_unitdir/deepin-service-group@deepin-daemon.service.d/
%_unitdir/deepin-service-group@deepin-daemon.service.d/ipwatchd-override.conf
%dir %_localstatedir/ipwatchd/
%_localstatedir/ipwatchd/ipwatchd.conf
%endif

%dir %_datadir/deepin-service-manager/user/
%_datadir/deepin-service-manager/user/plugin-qt-thememanager.json
%_datadir/deepin-service-manager/user/plugin-qt-wallpaperslideshow.json
%_datadir/deepin-service-manager/user/plugin-dde-xsettings.json
%_datadir/deepin-service-manager/user/plugin-dde-shortcut.json
%_datadir/deepin-service-manager/user/plugin-power-session.json
%_datadir/deepin-service-manager/user/plugin-ambient-brightness.json
%_datadir/dbus-1/services/org.deepin.dde.XSettings1.service
%_datadir/dbus-1/services/org.deepin.dde.Power1.service
%_datadir/dbus-1/system-services/org.deepin.dde.ImageBlur1.service
%_datadir/dbus-1/system-services/org.deepin.dde.ImageEffect1.service
%_datadir/dbus-1/system-services/org.deepin.dde.WallpaperCache.service
%_datadir/dbus-1/system.d/org.deepin.dde.ImageBlur1.conf
%_datadir/dbus-1/system.d/org.deepin.dde.ImageEffect1.conf
%_datadir/dbus-1/system.d/org.deepin.dde.WallpaperCache.conf
%dir %_unitdir/deepin-service-plugin@org.deepin.dde.WallpaperCache.service.d/
%_unitdir/deepin-service-plugin@org.deepin.dde.WallpaperCache.service.d/override.conf
%dir %_userunitdir/dde-session-pre.target.wants/
%_userunitdir/dde-session-pre.target.wants/org.deepin.dde.XSettings1.service
%_userunitdir/org.deepin.dde.XSettings1.service
%dir %_datadir/deepin/
%dir %_datadir/deepin/org.deepin.dde.keybinding/
%_datadir/deepin/org.deepin.dde.keybinding/org.deepin.dde.keybinding.ini
%_datadir/deepin/org.deepin.dde.keybinding/org.deepin.dde.shortcut.dde-app.ini
%dir %_datadir/deepin/org.deepin.dde.keybinding/translations/
%dir %_datadir/deepin/org.deepin.dde.keybinding/translations/org.deepin.dde.keybinding/
%_datadir/deepin/org.deepin.dde.keybinding/translations/org.deepin.dde.keybinding/org.deepin.dde.keybinding.qm
%dir %_datadir/deepin/org.deepin.dde.keybinding/translations/org.deepin.dde.shortcut.dde-app/
%dir %_datadir/dsg/
%dir %_datadir/dsg/configs/
%dir %_datadir/dsg/configs/org.deepin.dde.daemon/
%_datadir/dsg/configs/org.deepin.dde.daemon/org.deepin.XSettings.json
%_datadir/dsg/configs/org.deepin.dde.daemon/org.deepin.dde.daemon.ambient-brightness.json
%dir %_datadir/dsg/configs/org.deepin.dde.keybinding/
%_datadir/dsg/configs/org.deepin.dde.keybinding/org.deepin.shortcut.json
%_datadir/dsg/configs/org.deepin.dde.keybinding/org.deepin.dde.keybinding*/
%dir %_libdir/cmake/DdeShortcutI18n/
%_libdir/cmake/DdeShortcutI18n/DdeShortcutI18nConfig.cmake

%changelog
* Tue Aug 25 2026 Leontiy Volodin <lvol@altlinux.org> 1.0.41-alt1
- New version 1.0.41.

* Fri Aug 14 2026 Leontiy Volodin <lvol@altlinux.org> 1.0.39-alt1
- New version 1.0.39.

* Tue Aug 11 2026 Leontiy Volodin <lvol@altlinux.org> 1.0.38-alt1
- New version 1.0.38.

* Tue Jul 28 2026 Leontiy Volodin <lvol@altlinux.org> 1.0.36-alt1
- New version 1.0.36.

* Tue Jan 27 2026 Leontiy Volodin <lvol@altlinux.org> 1.0.19-alt2
- Fixed build on dtk 6.7.31.

* Wed Jan 21 2026 Leontiy Volodin <lvol@altlinux.org> 1.0.19-alt1
- New version 1.0.19.
- Disabled ipwatchd plugin (by upstream).

* Mon Dec 22 2025 Leontiy Volodin <lvol@altlinux.org> 1.0.17-alt1
- New version 1.0.17.

* Tue Dec 09 2025 Leontiy Volodin <lvol@altlinux.org> 1.0.15-alt1
- New version 1.0.15.

* Fri Dec 05 2025 Leontiy Volodin <lvol@altlinux.org> 1.0.14-alt1
- New version 1.0.14.

* Tue Dec 02 2025 Leontiy Volodin <lvol@altlinux.org> 1.0.13-alt1
- New version 1.0.13.

* Thu Nov 20 2025 Leontiy Volodin <lvol@altlinux.org> 1.0.12-alt2
- Built with ipwatchd plugin.

* Tue Nov 18 2025 Leontiy Volodin <lvol@altlinux.org> 1.0.12-alt1
- New version 1.0.12.

* Wed Oct 29 2025 Leontiy Volodin <lvol@altlinux.org> 1.0.10-alt1
- New version 1.0.10.

* Fri Sep 12 2025 Leontiy Volodin <lvol@altlinux.org> 1.0.9-alt1
- New version 1.0.9.

* Thu Jul 31 2025 Leontiy Volodin <lvol@altlinux.org> 1.0.8-alt1
- Initial build for ALT Sisyphus.
