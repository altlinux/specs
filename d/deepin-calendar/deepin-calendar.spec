%global repo dde-calendar

Name: deepin-calendar
Version: 5.8.0.8
Release: alt1
Summary: Calendar for Deepin Desktop Environment
License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-calendar
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz

BuildRequires(pre): rpm-build-ninja desktop-file-utils
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: deepin-gettext-tools
BuildRequires: qt5-linguist
BuildRequires: dtk5-widget-devel
BuildRequires: qt5-base-devel
BuildRequires: qt5-svg-devel
BuildRequires: deepin-qt-dbus-factory-devel
BuildRequires: libgtest-devel
BuildRequires: qt5-tools-devel
Requires: icon-theme-hicolor

%description
Calendar for Deepin Desktop Environment.

%prep
%setup -n %repo-%version
sed -i 's|/usr/lib/deepin-aiassistant|%_libdir/deepin-aiassistant|' schedule-plugin/CMakeLists.txt
sed -i 's|lib/deepin-daemon/|libexec/deepin-daemon/|' \
    calendar-service/CMakeLists.txt \
    calendar-service/assets/dde-calendar-service.desktop \
    calendar-service/assets/data/com.deepin.dataserver.Calendar.service

%build
%cmake_insource \
    -GNinja \
    -DCMAKE_INSTALL_PREFIX=%_prefix \
    -DCMAKE_BUILD_TYPE=Release
%ninja_build

%install
%ninja_install
%find_lang %repo

%check
desktop-file-validate %buildroot%_desktopdir/%repo.desktop

%files -f %repo.lang
%doc README.md
%doc LICENSE
%_bindir/%repo
%_datadir/%repo/
%_datadir/dbus-1/services/com.deepin.Calendar.service
%_datadir/dbus-1/services/com.deepin.dataserver.Calendar.service
%_desktopdir/%repo.desktop
%_sysconfdir/xdg/autostart/dde-calendar-service.desktop
%_prefix/libexec/deepin-daemon/dde-calendar-service
%dir %_libdir/deepin-aiassistant/
%dir %_libdir/deepin-aiassistant/serivce-plugins/
%_libdir/deepin-aiassistant/serivce-plugins/libuosschedulex-plugin.so

%changelog
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
