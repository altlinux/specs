%define repo dde-calendar

Name: deepin-calendar
Version: 5.11.0
Release: alt1

Summary: Calendar for Deepin Desktop Environment

License: LGPL-2.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-calendar

Source: %url/archive/%version/%repo-%version.tar.gz
%ifarch aarch64 armh
Patch: deepin-calendar-5.8.27-alt-aarch64-armh.patch
%endif

Requires: icon-theme-hicolor

BuildRequires(pre): rpm-build-ninja
# Automatically added by buildreq on Mon Oct 23 2023
# optimized out: cmake-modules gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libdb4-devel libdouble-conversion3 libdtkcore-devel libdtkgui-devel libglvnd-devel libgpg-error libgsettings-qt libp11-kit libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-sql libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libssl-devel libstartup-notification libstdc++-devel pkg-config python3 python3-base qt5-base-devel qt5-tools sh5
BuildRequires: cmake deepin-qt-dbus-factory-devel libdtkwidget-devel libical-devel qt5-svg-devel qt5-tools-devel

%description
Calendar for Deepin Desktop Environment.

%prep
%setup -n %repo-%version
%ifarch aarch64 armh
%patch -p1
%endif

sed -i 's|lib/deepin-aiassistant|%_lib/deepin-aiassistant|' \
  schedule-plugin/CMakeLists.txt
sed -i 's|${CMAKE_INSTALL_FULL_LIBEXECDIR}/deepin-daemon|%_libexecdir/deepin-daemon|' \
  calendar-service/CMakeLists.txt

%build
export PATH=%_qt5_bindir:$PATH
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_INSTALL_PREFIX=%_prefix \
    -DCMAKE_INSTALL_LIBDIR=%_libdir \
    -DLIB_INSTALL_DIR=%_libdir \
    -DAPP_VERSION=%version \
    -DVERSION=%version
cmake --build "%_cmake__builddir" -j%__nprocs

%install
%cmake_install
mkdir -p %buildroot%_sysconfdir/xdg/autostart/
mv -f %buildroot%_prefix%_sysconfdir/xdg/autostart/dde-calendar-service.desktop %buildroot%_sysconfdir/xdg/autostart/

%files
%doc README.md LICENSE
%_bindir/%repo
%_datadir/%repo/
%_datadir/dbus-1/services/com.deepin.Calendar.service
%_datadir/dbus-1/services/com.deepin.dataserver.Calendar.service
%_desktopdir/%repo.desktop
%_sysconfdir/xdg/autostart/dde-calendar-service.desktop
%_libexecdir/deepin-daemon/dde-calendar-service
%dir %_libdir/deepin-aiassistant/
%dir %_libdir/deepin-aiassistant/serivce-plugins/
%_libdir/deepin-aiassistant/serivce-plugins/libuosschedulex-plugin.so
%dir %_datadir/deepin-manual/
%dir %_datadir/deepin-manual/manual-assets/
%dir %_datadir/deepin-manual/manual-assets/application/
%dir %_datadir/deepin-manual/manual-assets/application/%repo/
%_datadir/deepin-manual/manual-assets/application/%repo/calendar/
%_userunitdir/com.dde.calendarserver.calendar.service
%_userunitdir/com.dde.calendarserver.calendar.timer

%changelog
* Mon Oct 23 2023 Leontiy Volodin <lvol@altlinux.org> 5.11.0-alt1
- New version 5.11.0.
- Updated license tag.
- Cleanup spec and BRs.

* Fri Jan 20 2023 Leontiy Volodin <lvol@altlinux.org> 5.9.1-alt1
- New version (5.9.1).

* Tue Jun 14 2022 Leontiy Volodin <lvol@altlinux.org> 5.8.30-alt1
- New version (5.8.30).
- Upstream:
  + feat: minimum size optimization:
    + monthly view display;
    + focus interaction in the search box of the state column;
    + focus switching optimization in the search box of the status column.
  + feat: Modify the statistical configuration of code coverage.
  + feat: Add default size.
  + fix: After bug112880 created the schedule under the viewing chart,
  the monthly viewing information area was gray occasionally displayed.

* Tue Apr 19 2022 Leontiy Volodin <lvol@altlinux.org> 5.8.29-alt1
- New version (5.8.29).

* Thu Feb 10 2022 Leontiy Volodin <lvol@altlinux.org> 5.8.27-alt1
- New version (5.8.27).

* Thu Jul 08 2021 Leontiy Volodin <lvol@altlinux.org> 5.8.2-alt2
- Fixed build with libgmock.so.1.11.0.

* Tue May 18 2021 Leontiy Volodin <lvol@altlinux.org> 5.8.2-alt1
- New version (5.8.2) with rpmgs script.

* Fri Apr 09 2021 Leontiy Volodin <lvol@altlinux.org> 5.8.0.19-alt1
- New version (5.8.0.19) with rpmgs script.
- Fixed build with dtk 5.4.13.

* Thu Feb 25 2021 Leontiy Volodin <lvol@altlinux.org> 5.8.0.8-alt1
- New version (5.8.0.8) with rpmgs script.

* Mon Nov 30 2020 Leontiy Volodin <lvol@altlinux.org> 5.8.0.1-alt1
- New version (5.8.0.1) with rpmgs script.

* Tue Nov 17 2020 Leontiy Volodin <lvol@altlinux.org> 5.7.0.20-alt1
- New version (5.7.0.20) with rpmgs script.

* Thu Nov 05 2020 Leontiy Volodin <lvol@altlinux.org> 5.7.0.16-alt1
- New version (5.7.0.16) with rpmgs script.

* Mon Nov 02 2020 Leontiy Volodin <lvol@altlinux.org> 5.7.0.15-alt1
- New version (5.7.0.15) with rpmgs script.

* Fri Oct 09 2020 Leontiy Volodin <lvol@altlinux.org> 5.7.0.13-alt1
- New version (5.7.0.13) with rpmgs script.

* Tue Aug 18 2020 Leontiy Volodin <lvol@altlinux.org> 5.7.0.5-alt1
- Initial build for ALT Sisyphus (thanks fedora and archlinux for this spec).
