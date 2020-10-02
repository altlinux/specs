Name: dtkwidget
Version: 5.2.2.3
Release: alt1
Summary: Deepin tool kit widget modules
License: LGPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dtkwidget
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz

BuildRequires: gcc-c++ qt5-linguist qt5-base-devel qt5-multimedia-devel qt5-svg-devel qt5-x11extras-devel dtk5-core-devel dtk5-gui-devel gsettings-qt-devel deepin-qt-dbus-factory-devel libudev-devel librsvg-devel libstartup-notification-devel libXi-devel libX11-devel libXext-devel libxcbutil-devel libxkbcommon-devel libXrender-devel
# libQt5Gui.so.5(Qt_5_PRIVATE_API)(64bit) needed by dtkwidget
BuildRequires: libqt5-gui

%description
DtkWidget is Deepin graphical user interface for deepin desktop development.

%package -n libdtk5-widget
Summary: Libraries for %name
Group: System/Libraries

%description -n libdtk5-widget
DtkWidget is Deepin graphical user interface for deepin desktop development.
Libraries for %name.

%package -n dtk5-widget-devel
Summary: Development package for %name
Group: Development/KDE and QT

%description -n dtk5-widget-devel
Header files and libraries for %name.

%prep
%setup
sed -i '/#include <QPainter>/a #include <QPainterPath>' src/util/dwidgetutil.cpp

%build
%qmake_qt5 \
    CONFIG+=nostrip \
    PREFIX=%_prefix
%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot

%files -n libdtk5-widget
%doc README.md LICENSE
%_libdir/lib%name.so.5*
%dir %_libdir/libdtk-5*/
%_libdir/libdtk-5*/DWidget/
%_datadir/libdtk-5*/

%files -n dtk5-widget-devel
%_includedir/libdtk-5*/
%_qt5_archdatadir/mkspecs/modules/*.pri
%_libdir/cmake/DtkWidget/
%_pkgconfigdir/%name.pc
%_libdir/lib%name.so

%changelog
* Mon Aug 17 2020 Leontiy Volodin <lvol@altlinux.org> 5.2.2.3-alt1
- Initial build for ALT Sisyphus (thanks fedora and archlinux for this spec).
