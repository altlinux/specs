%def_disable clang
%def_with ipwatchd

%define repo dde-services

Name: deepin-services
Version: 1.0.17
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
BuildRequires: cmake dqt6-base-devel dtk6-common-devel libdtk6gui-devel libX11-devel
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
%if_without ipwatchd
  -DENABLE_PLUGIN_IPWATCHD=OFF \
%endif
#

%install
%DQ6install

%files
%doc LICENSE README.md debian/changelog
%dir %_libdir/deepin-service-manager/
%_libdir/deepin-service-manager/libplugin-qt-thememanager.so
%_libdir/deepin-service-manager/libplugin-qt-wallpaperslideshow.so
%_libdir/deepin-service-manager/libplugin-dde-xsettings.so
%dir %_datadir/deepin-service-manager/
%if_with ipwatchd
%_bindir/ipwatchd
%_libdir/deepin-service-manager/libplugin-ipwatchd.so
%_datadir/dbus-1/system.d/org.deepin.ipwatchd.conf
%dir %_datadir/deepin-service-manager/system/
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
%_datadir/dbus-1/services/org.deepin.dde.XSettings1.service
%dir %_userunitdir/dde-session-pre.target.wants/
%_userunitdir/dde-session-pre.target.wants/org.deepin.dde.XSettings1.service
%_userunitdir/org.deepin.dde.XSettings1.service
%dir %_datadir/dsg/
%dir %_datadir/dsg/configs/
%dir %_datadir/dsg/configs/org.deepin.dde.daemon/
%_datadir/dsg/configs/org.deepin.dde.daemon/org.deepin.XSettings.json

%changelog
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
