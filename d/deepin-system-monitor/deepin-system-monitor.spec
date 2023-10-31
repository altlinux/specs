%def_disable clang

Name: deepin-system-monitor
Version: 6.0.4
Release: alt2
Summary: A more user-friendly system monitor
License: GPL-3.0+
Group: Monitoring
Url: https://github.com/linuxdeepin/deepin-system-monitor
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz
%ifarch aarch64 armh
Patch: deepin-system-monitor-5.9.4-alt-aarch64-armh.patch
%endif
Patch1: deepin-system-monitor-6.0.4-fix-unknown-DockPart.patch
Patch2: deepin-system-monitor-6.0.4-fix-build-procps0.patch
Patch3: deepin-system-monitor-6.0.4-fix-build-procps1.patch

BuildRequires(pre): rpm-build-ninja rpm-build-xdg desktop-file-utils
# Automatically added by buildreq on Tue Oct 31 2023
# optimized out: cmake-modules gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 icu-utils libXext-devel libdouble-conversion3 libdtk5-widget libdtkcore-devel libdtkgui-devel libglvnd-devel libgpg-error libgsettings-qt libicu-devel libp11-kit libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libssl-devel libstartup-notification libstdc++-devel libudev-devel libwayland-client libwayland-server libxcb-devel libxcbutil-icccm perl perl-Config-Tiny perl-Encode perl-XML-LibXML perl-parent pkg-config python3 python3-base python3-dev python3-module-setuptools qt5-base-devel qt5-tools sh5 wayland-devel
BuildRequires: cmake deepin-dock-devel deepin-gettext-tools deepin-qt-dbus-factory-devel dtk5-widget-devel dwayland-devel gsettings-qt-devel libnl-devel libpcap-devel libwayland-client-devel libxcbutil-icccm-devel qt5-svg-devel qt5-tools-devel qt5-x11extras-devel

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
%ifarch aarch64 armh
%patch -p1
%endif
%patch1 -p1
%patch2 -p1
%patch3 -p1
sed -i 's|lib/dde-dock/plugins|%_lib/dde-dock/plugins|' \
    deepin-system-monitor-plugin/CMakeLists.txt
sed -i '/include_directories(${DtkCore_INCLUDE_DIRS})/a include_directories(${DtkWidget_INCLUDE_DIRS})' \
    deepin-system-monitor-plugin-popup/CMakeLists.txt \
    deepin-system-monitor-main/CMakeLists.txt \
    deepin-system-monitor-plugin/CMakeLists.txt
sed -i 's|DGuiApplicationHelper::|Dtk::Gui::DGuiApplicationHelper::|g' \
    deepin-system-monitor-plugin/gui/monitor_plugin.h

%build
%if_enabled clang
%define optflags_lto -flto=thin
export CC=clang
export CXX=clang++
export LDFLAGS="-fuse-ld=lld $LDFLAGS"
%endif
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DLIB_INSTALL_DIR=%_libdir \
    -DCMAKE_INSTALL_SYSCONFDIR=%_sysconfdir \
    -DUSE_DEEPIN_WAYLAND=ON \
    -DAPP_VERSION=%version \
    -DVERSION=%version
cmake --build "%_cmake__builddir" -j%__nprocs

%install
%cmake_install
%find_lang %name

%check
desktop-file-validate %buildroot%_desktopdir/%name.desktop ||:

%files -f %name.lang
%doc README.md
%doc LICENSE
%_bindir/%name
%_bindir/%name-daemon
%_bindir/%name-plugin-popup
%_datadir/polkit-1/actions/com.deepin.pkexec.deepin-system-monitor.policy
%_desktopdir/%name.desktop
%_xdgconfigdir/autostart/deepin-system-monitor-daemon.desktop
%_libdir/dde-dock/plugins/libdeepin-system-monitor-plugin.so
%_datadir/dbus-1/services/com.deepin.SystemMonitor.Daemon.service
%_datadir/dbus-1/services/com.deepin.SystemMonitorPluginPopup.service
%_datadir/%name/
%_datadir/%name-daemon/
%_datadir/%name-plugin-popup/
%_datadir/%name-plugin/
%_datadir/glib-2.0/schemas/com.deepin.dde.dock.module.system-monitor.gschema.xml
%_datadir/glib-2.0/schemas/com.deepin.system.monitor.plugin.gschema.xml
%_datadir/deepin-manual/manual-assets/application/%name/system-monitor/

%changelog
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
