%define repo dde-calendar

Name: deepin-calendar
Version: 6.5.40
Release: alt1

Summary: Calendar for Deepin Desktop Environment

License: LGPL-3.0-or-later
# ./3rdparty/kcalendarcore/src/ contains license(s) LGPL-2.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-calendar
VCS: https://github.com/linuxdeepin/dde-calendar

# Source-url: https://github.com/linuxdeepin/dde-calendar/archive/%version/%repo-%version.tar.gz
Source: %repo-%version.tar
Patch0: %name-%version-%release.patch
Patch1: deepin-calendar-6.5.39-alt-fix-GNUInstallDirs.patch

Requires: icon-theme-hicolor

BuildRequires(pre): rpm-build-ninja rpm-macros-dqt6
BuildRequires: cmake dtk6-common-devel libdtk6widget-devel libical-devel dqt6-svg-devel dqt6-tools-devel libcups-devel libwayland-client-devel libdqt6-concurrent
BuildRequires: dqt6-sql-interbase dqt6-sql-mysql dqt6-sql-odbc dqt6-sql-postgresql vulkan-headers

%description
Calendar for Deepin Desktop Environment.

%prep
%setup -n %repo-%version
%patch0 -p1
%patch1 -p2

%build
%DQ6build \
  -DLIB_DESTINATION=%_lib \
  -DCMAKE_INSTALL_LIBDIR=%_libdir \
  -DSERVICE_INSTALL_DIR=%_libexecdir/deepin-daemon \
  -DCMAKE_INSTALL_SYSCONFDIR=%_sysconfdir \
  -DVERSION=%version

%install
%DQ6install
%find_lang --with-qt %repo

%files -f %repo.lang
%doc README.md LICENSE debian/changelog
%_bindir/%repo
%dir %_datadir/%repo/
%dir %_datadir/%repo/translations/
%_datadir/%repo/translations/dde-calendar-service.qm
%_datadir/%repo/translations/dde-calendar.qm
%dir %_datadir/%repo/data/
%_datadir/%repo/data/huangli.db
%_datadir/dbus-1/services/com.deepin.Calendar.service
%_datadir/dbus-1/services/com.deepin.dataserver.Calendar.service
%_datadir/metainfo/org.deepin.calendar.metainfo.xml
%_desktopdir/%repo.desktop
%_sysconfdir/xdg/autostart/dde-calendar-service.desktop
%dir %_libexecdir/deepin-daemon/
%_libexecdir/deepin-daemon/dde-calendar-service
%dir %_libdir/deepin-aiassistant/
%dir %_libdir/deepin-aiassistant/serivce-plugins/
%_libdir/deepin-aiassistant/serivce-plugins/libuosschedulex-plugin.so
%dir %_datadir/deepin-manual/
%dir %_datadir/deepin-manual/manual-assets/
%dir %_datadir/deepin-manual/manual-assets/application/
%dir %_datadir/deepin-manual/manual-assets/application/%repo/
%_datadir/deepin-manual/manual-assets/application/%repo/calendar/
%dir %_datadir/deepin-log-viewer/
%dir %_datadir/deepin-log-viewer/deepin-log.conf.d/
%_datadir/deepin-log-viewer/deepin-log.conf.d/dde-calendar.json
%_userunitdir/com.dde.calendarserver.calendar.service
%_userunitdir/com.dde.calendarserver.calendar.timer
%_userunitdir/%repo.service
%dir %_datadir/dsg/
%dir %_datadir/dsg/configs/
%dir %_datadir/dsg/configs/org.deepin.dde.calendar/
%_datadir/dsg/configs/org.deepin.dde.calendar/org.deepin.dde.calendar*.json
%dir %_datadir/deepin-debug-config/
%dir %_datadir/deepin-debug-config/deepin-debug-config.d/
%_datadir/deepin-debug-config/deepin-debug-config.d/org.deepin.dde.calendar.json

%changelog
* Fri Jun 26 2026 Leontiy Volodin <lvol@altlinux.org> 6.5.40-alt1
- New version 6.5.40.

* Wed May 06 2026 Leontiy Volodin <lvol@altlinux.org> 6.5.39-alt1
- New version 6.5.39.

* Fri Apr 03 2026 Leontiy Volodin <lvol@altlinux.org> 6.5.37-alt1
- New version 6.5.37.
- Built on dqt6 again (by upstream).

* Mon Jan 26 2026 Leontiy Volodin <lvol@altlinux.org> 6.5.32-alt1
- New version 6.5.32.
- Built on dqt5 again (by upstream).
- Fixed build on dtk 6.7.31.

* Fri Dec 12 2025 Leontiy Volodin <lvol@altlinux.org> 6.5.31-alt1
- New version 6.5.31.

* Thu Nov 27 2025 Leontiy Volodin <lvol@altlinux.org> 6.5.29-alt1
- New version 6.5.29.

* Thu Nov 20 2025 Leontiy Volodin <lvol@altlinux.org> 6.5.28-alt1
- New version 6.5.28.

* Fri Oct 31 2025 Leontiy Volodin <lvol@altlinux.org> 6.5.27-alt1
- New version 6.5.27.

* Tue Oct 28 2025 Leontiy Volodin <lvol@altlinux.org> 6.5.26-alt1
- New version 6.5.26.

* Fri Aug 08 2025 Leontiy Volodin <lvol@altlinux.org> 6.5.18-alt1
- New version 6.5.18.

* Thu Feb 13 2025 Leontiy Volodin <lvol@altlinux.org> 6.5.1-alt1
- New version 6.5.1.

* Tue Jan 21 2025 Leontiy Volodin <lvol@altlinux.org> 6.5.0-alt1
- New version 6.5.0.
- Added vcs tag.
- Switched to dqt6.

* Thu May 30 2024 Leontiy Volodin <lvol@altlinux.org> 5.13.1-alt1
- New version 5.13.1.
- Built via separate qt5 instead system (ALT #48138).

* Wed Apr 10 2024 Leontiy Volodin <lvol@altlinux.org> 5.13.0-alt1
- New version 5.13.0.

* Mon Mar 25 2024 Leontiy Volodin <lvol@altlinux.org> 5.12.2-alt1
- New version 5.12.2.

* Fri Jan 19 2024 Leontiy Volodin <lvol@altlinux.org> 5.12.1-alt1
- New version 5.12.1.

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
