%global repo dde-calendar

Name: deepin-calendar
Version: 5.7.0.5
Release: alt1
Summary: Calendar for Deepin Desktop Environment
License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-calendar
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz

BuildRequires(pre): rpm-build-ninja desktop-file-utils
BuildRequires: gcc-c++ cmake deepin-gettext-tools qt5-linguist dtk5-widget-devel qt5-base-devel qt5-svg-devel deepin-qt-dbus-factory-devel
Requires: icon-theme-hicolor

%description
Calendar for Deepin Desktop Environment.

%prep
%setup -n %repo-%version
%__subst 's|lrelease|lrelease-qt5|g' assets/translate_generation.sh

%__subst '/<QQueue>/a #include <QMouseEvent>' src/daymonthview.cpp
%__subst '/<QStylePainter>/a #include <QMouseEvent>' src/schcedulesearchview.cpp
%__subst '/include <QJsonObject>/a #include <QMouseEvent>' src/draginfographicsview.cpp

# Not included in https://github.com/linuxdeepin/dde-calendar/pull/30 yet
%__subst '/include <QPainter>/a #include <QPainterPath>' src/schcedulesearchview.cpp src/daymonthview.cpp src/weekheadview.cpp src/customframe.cpp
%__subst '/include <QMessageBox>/a #include <QWheelEvent>' src/yearwindow.cpp

%build
%cmake \
-GNinja \
-DCMAKE_INSTALL_PREFIX=%_prefix \
-DCMAKE_BUILD_TYPE=Release
%ninja_build -C BUILD

%install
%ninja_install -C BUILD
%find_lang %repo

%check
desktop-file-validate %buildroot%_desktopdir/%repo.desktop

%files -f %repo.lang
%doc README.md
%doc LICENSE
%_bindir/%repo
%_datadir/%repo/
%_datadir/dbus-1/services/com.deepin.Calendar.service
%_desktopdir/%repo.desktop

%changelog
* Tue Aug 18 2020 Leontiy Volodin <lvol@altlinux.org> 5.7.0.5-alt1
- Initial build for ALT Sisyphus (thanks fedora and archlinux for this spec).
