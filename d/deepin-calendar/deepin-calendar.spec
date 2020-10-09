%global repo dde-calendar

Name: deepin-calendar
Version: 5.7.0.13
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
sed -i 's|lrelease|lrelease-qt5|g' assets/translate_generation.sh

sed -i '/<QQueue>/a #include <QMouseEvent>' src/daymonthview.cpp
sed -i '/<QStylePainter>/a #include <QMouseEvent>' src/schcedulesearchview.cpp
sed -i '/include <QJsonObject>/a #include <QMouseEvent>' src/draginfographicsview.cpp
sed -i '/include <QPainter>/a #include <QMouseEvent>' schedule-plugin/src/widget/itemwidget.h schedule-plugin/src/widget/modifyscheduleitem.h
sed -i '1i#include <QPainterPath>' schedule-plugin/src/widget/itemwidget.cpp
sed -i 's|/usr/lib|%_libdir|' schedule-plugin/CMakeLists.txt

# Not included in https://github.com/linuxdeepin/dde-calendar/pull/30 yet
sed -i '/include <QPainter>/a #include <QPainterPath>' src/schcedulesearchview.cpp src/daymonthview.cpp src/weekheadview.cpp src/customframe.cpp src/yearview.cpp
sed -i '/include <QMessageBox>/a #include <QWheelEvent>' src/yearwindow.cpp

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
%_desktopdir/%repo.desktop
%dir %_libdir/deepin-aiassistant/
%dir %_libdir/deepin-aiassistant/serivce-plugins/
%_libdir/deepin-aiassistant/serivce-plugins/libschedulex-plugin.so

%changelog
* Fri Oct 09 2020 Leontiy Volodin <lvol@altlinux.org> 5.7.0.13-alt1
- New version (5.7.0.13) with rpmgs script.

* Tue Aug 18 2020 Leontiy Volodin <lvol@altlinux.org> 5.7.0.5-alt1
- Initial build for ALT Sisyphus (thanks fedora and archlinux for this spec).
