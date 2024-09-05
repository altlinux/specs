%define _libexecdir %_prefix/lib
%define _unitdir %_prefix/lib/systemd/system

%def_disable clang

Name: deepin-system-monitor
Version: 6.0.20
Release: alt1

Summary: A more user-friendly system monitor

License: GPL-3.0+
Group: Monitoring
Url: https://github.com/linuxdeepin/deepin-system-monitor

Source: %url/archive/%version/%name-%version.tar.gz
Patch: %name-%version-%release.patch
Patch1: deepin-system-monitor-6.0.12-alt-fix-GNUInstallDirs.patch
Patch2: deepin-system-monitor-6.0.12-alt-fix-build-gcc13.patch
Patch3: deepin-system-monitor-6.0.12-alt-fix-build-ppc64le.patch

BuildRequires(pre): rpm-build-ninja rpm-build-xdg desktop-file-utils rpm-macros-dqt5
# Automatically added by buildreq on Tue Oct 31 2023
# optimized out: cmake-modules gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 icu-utils libXext-devel libdouble-conversion3 libdtk5-widget libdtkcore-devel libdtkgui-devel libglvnd-devel libgpg-error libgsettings-qt libicu-devel libp11-kit libdqt5-concurrent libdqt5-core libdqt5-dbus libdqt5-gui libdqt5-network libdqt5-printsupport libdqt5-svg libdqt5-widgets libdqt5-x11extras libdqt5-xml libsasl2-3 libssl-devel libstartup-notification libstdc++-devel libudev-devel libwayland-client libwayland-server libxcb-devel libxcbutil-icccm perl perl-Config-Tiny perl-Encode perl-XML-LibXML perl-parent pkg-config python3 python3-base python3-dev python3-module-setuptools dqt5-base-devel dqt5-tools sh5 wayland-devel
BuildRequires: cmake deepin-dock-devel deepin-gettext-tools deepin-qt-dbus-factory-devel dtk5-widget-devel dwayland-devel gsettings-qt-devel libnl-devel libpcap-devel libwayland-client-devel libxcbutil-icccm-devel dqt5-svg-devel dqt5-tools-devel dqt5-x11extras-devel dtk6-common-devel libpolkitqt5-qt5-devel
BuildRequires: kf5-kwayland-devel

%if_enabled clang
BuildRequires: clang-devel
BuildRequires: lld-devel
%else
BuildRequires: gcc-c++
%endif

%description
%summary.

%prep
%setup
%autopatch -p1

%build
%if_enabled clang
%define optflags_lto -flto=thin
export CC=clang
export CXX=clang++
export LDFLAGS="-fuse-ld=lld $LDFLAGS"
%endif
export CMAKE_PREFIX_PATH=%_dqt5_libdir/cmake:$CMAKE_PREFIX_PATH
export PKG_CONFIG_PATH=%_dqt5_libdir/pkgconfig:$PKG_CONFIG_PATH
export CPLUS_INCLUDE_PATH=%_includedir/qt5:$CPLUS_INCLUDE_PATH
export PATH=%_dqt5_bindir:$PATH
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=no \
    -DCMAKE_INSTALL_RPATH=%_dqt5_libdir \
    -DLIB_INSTALL_DIR=%_libdir \
    -DCMAKE_INSTALL_SYSCONFDIR=%_sysconfdir \
    -DUSE_DEEPIN_WAYLAND=ON \
    -DVERSION=%version
cmake --build "%_cmake__builddir" -j%__nprocs

%install
%cmake_install
%find_lang --with-qt --output=%name.lang %name %{name}-plugin %{name}-plugin-popup

%check
desktop-file-validate %buildroot%_desktopdir/%name.desktop ||:

%files -f %name.lang
%doc README.md
%doc LICENSE
%_bindir/%name
%_bindir/%name-server
%_bindir/%name-plugin-popup
%_datadir/polkit-1/actions/com.deepin.pkexec.deepin-system-monitor.policy
%_datadir/polkit-1/actions/org.deepin.deepin-system-monitor-system-server.policy
%_desktopdir/%name.desktop
%dir %_libdir/dde-dock/
%dir %_libdir/dde-dock/plugins/
%_libdir/dde-dock/plugins/libdeepin-system-monitor-plugin.so
%dir %_libdir/deepin-service-manager/
%_libdir/deepin-service-manager/libdeepin-system-monitor-daemon.so
%_datadir/dbus-1/services/com.deepin.SystemMonitorPluginPopup.service
%_datadir/dbus-1/services/com.deepin.SystemMonitorServer.service
%_datadir/dbus-1/system-services/org.deepin.SystemMonitorSystemServer.service
%_datadir/dbus-1/system.d/org.deepin.SystemMonitorSystemServer.conf
# package translations outside %%find_lang
%dir %_datadir/%name/
%dir %_datadir/%name/translations/
%_datadir/%name/translations/%name.qm
%dir %_datadir/%name-plugin/
%dir %_datadir/%name-plugin/translations/
%dir %_datadir/%name-plugin-popup/
%dir %_datadir/%name-plugin-popup/translations/
# ---
%_datadir/glib-2.0/schemas/com.deepin.dde.dock.module.system-monitor.gschema.xml
%dir %_datadir/deepin-service-manager/
%dir %_datadir/deepin-service-manager/user/
%_datadir/deepin-service-manager/user/deepin-system-monitor-daemon.json
%dir %_datadir/deepin-service-manager/other/
%_datadir/deepin-service-manager/other/deepin-system-monitor-system-server.json
%dir %_datadir/dsg/
%dir %_datadir/dsg/configs/
%dir %_datadir/dsg/configs/org.deepin.system-monitor/
%_datadir/dsg/configs/org.deepin.system-monitor/org.deepin.system-monitor.main.json
%_datadir/dsg/configs/org.deepin.system-monitor/org.deepin.system-monitor.daemon.json
%_datadir/dsg/configs/org.deepin.system-monitor/org.deepin.system-monitor.json
%_datadir/dsg/configs/org.deepin.system-monitor/org.deepin.system-monitor.plugin.json
%_datadir/dsg/configs/org.deepin.system-monitor/org.deepin.system-monitor.plugin.popup.json
%_datadir/dsg/configs/org.deepin.system-monitor/org.deepin.system-monitor.server.json
%dir %_datadir/deepin-manual/
%dir %_datadir/deepin-manual/manual-assets/
%dir %_datadir/deepin-manual/manual-assets/application/
%dir %_datadir/deepin-manual/manual-assets/application/%name/
%_datadir/deepin-manual/manual-assets/application/%name/system-monitor/
%dir %_libexecdir/deepin-daemon/
%_libexecdir/deepin-daemon/deepin-system-monitor-system-server
%_unitdir/deepin-system-monitor-system-server.service
%dir %_datadir/deepin-log-viewer/
%dir %_datadir/deepin-log-viewer/deepin-log.conf.d/
%_datadir/deepin-log-viewer/deepin-log.conf.d/org.deepin.system-monitor.json

%changelog
* Thu May 30 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.20-alt1
- New version 6.0.20.
- Built via separate qt5 instead system (ALT #48138).

* Thu Mar 21 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.16.0.2.2e9c-alt1
- New version 6.0.16-2-g2e9c86bc.

* Mon Jan 29 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.12.0.3.63f2-alt1
- New version 6.0.12-3-g63f26873.

* Tue Oct 31 2023 Leontiy Volodin <lvol@altlinux.org> 6.0.4-alt2
- Fixed build with procps.
- Cleanup BRs.

* Sat Feb 04 2023 Leontiy Volodin <lvol@altlinux.org> 6.0.4-alt1
- New version (6.0.4).
- Removed old patches.
- Fixed build with dtkcore and dtkgui 5.6.4.
- Enabled dwayland support.

* Mon Jan 09 2023 Leontiy Volodin <lvol@altlinux.org> 6.0.3-alt1
- New version (6.0.3).
- Upstream:
  + feat: The insertion in the task column does not show by default.
- Patches:
  + revert: The service start method cannot be modified.
  + revert: Fix build without dwayland.

* Thu Dec 15 2022 Leontiy Volodin <lvol@altlinux.org> 5.9.32-alt1
- New version (5.9.32).

* Thu Feb 10 2022 Leontiy Volodin <lvol@altlinux.org> 5.9.4-alt1
- New version (5.9.4).

* Wed Jun 30 2021 Leontiy Volodin <lvol@altlinux.org> 5.8.8-alt1
- New version (5.8.8).

* Wed May 19 2021 Arseny Maslennikov <arseny@altlinux.org> 5.8.6-alt1.1
- NMU: spec: adapted to new cmake macros.

* Tue May 18 2021 Leontiy Volodin <lvol@altlinux.org> 5.8.6-alt1
- New version (5.8.6) with rpmgs script.

* Thu Apr 08 2021 Leontiy Volodin <lvol@altlinux.org> 5.8.0.27-alt1
- New version (5.8.0.27) with rpmgs script.

* Tue Mar 09 2021 Leontiy Volodin <lvol@altlinux.org> 5.8.0.9-alt1
- New version (5.8.0.9) with rpmgs script.

* Fri Dec 04 2020 Leontiy Volodin <lvol@altlinux.org> 5.8.0.7-alt1
- New version (5.8.0.7) with rpmgs script.
- Fixed build with gcc10.

* Tue Nov 17 2020 Leontiy Volodin <lvol@altlinux.org> 5.8.0.4-alt1
- New version (5.8.0.4) with rpmgs script.

* Fri Oct 09 2020 Leontiy Volodin <lvol@altlinux.org> 5.8.0.1-alt1
- New version (5.8.0.1) with rpmgs script.

* Fri Jul 31 2020 Leontiy Volodin <lvol@altlinux.org> 5.6.12-alt1
- Initial build for ALT Sisyphus (thanks fedora and archlinux for this spec).
