%def_disable clang
%def_with ipwatchd

%define repo dde-services

Name: deepin-services
Version: 1.0.13
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
BuildRequires: cmake dqt6-base-devel dtk6-common-devel libdtk6gui-devel
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
%_sysconfdir/xdg/autostart/oom-score-adjust.desktop
%dir %_libdir/deepin-service-manager/
%_libdir/deepin-service-manager/libOOMScoreAdjust.so
%_libdir/deepin-service-manager/libplugin-qt-thememanager.so
%_libdir/deepin-service-manager/libplugin-qt-wallpaperslideshow.so
%dir %_datadir/deepin-service-manager/
%dir %_datadir/deepin-service-manager/system/
%if_with ipwatchd
%_libdir/deepin-service-manager/libplugin-ipwatchd.so
%_datadir/dbus-1/system.d/org.deepin.ipwatchd.conf
%_datadir/deepin-service-manager/system/plugin-ipwatchd.json
%endif
%_datadir/dbus-1/system.d/org.deepin.service.OOMScoreAdjust.conf
%_datadir/dbus-1/system-services/org.deepin.OOMScoreAdjust.service
%_datadir/deepin-service-manager/system/OOM-Score-Adjust.json
%dir %_datadir/deepin-service-manager/user/
%_datadir/deepin-service-manager/user/plugin-qt-thememanager.json
%_datadir/deepin-service-manager/user/plugin-qt-wallpaperslideshow.json
%dir %_datadir/dsg/
%dir %_datadir/dsg/configs/
%dir %_datadir/dsg/configs/org.deepin.service.manager/
%_datadir/dsg/configs/org.deepin.service.manager/org.deepin.service.manager.oom-score-adjust.json

%changelog
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
