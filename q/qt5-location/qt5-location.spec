
%global qt_module qtlocation
%def_disable bootstrap

Name: qt5-location
Version: 5.7.1
Release: alt1%ubt

Group: System/Libraries
Summary: Qt5 - QtLocation component
Url: http://qt.io/
License: LGPLv2 / GPLv3

Source: %qt_module-opensource-src-%version.tar

# Automatically added by buildreq on Fri Feb 28 2014 (-bi)
# optimized out: elfutils glib2-devel libGL-devel libcloog-isl4 libdbus-devel libdbus-glib libdbus-glib-devel libqt5-clucene libqt5-core libqt5-gui libqt5-help libqt5-network libqt5-qml libqt5-quick libqt5-sql libqt5-widgets libqt5-xml libstdc++-devel libxml2-devel pkg-config python-base qt5-base-devel qt5-declarative-devel qt5-tools ruby ruby-stdlibs
#BuildRequires: gcc-c++ glibc-devel-static libGConf-devel libgeoclue-devel libgypsy-devel qt5-script-devel qt5-tools-devel qt5-webkit-devel qt5-xmlpatterns-devel rpm-build-ruby
BuildRequires(pre): rpm-build-ubt
BuildRequires: gcc-c++ glibc-devel qt5-declarative-devel qt5-xmlpatterns-devel
BuildRequires: pkgconfig(geoclue) pkgconfig(gypsy) pkgconfig(gconf-2.0)
%if_disabled bootstrap
BuildRequires: qt5-tools
%endif

%description
The Qt Positioning API gives developers the ability to determine a position
by using a variety of possible sources, including satellite, or wifi, or
 text file, and so on. That information can then be used to for example
determine a position on a map. In addition satellite information can be
retrieved and area based monitoring can be performed.

%package common
Summary: Common package for %name
Group: System/Configuration/Other
Requires: qt5-base-common
%description common
Common package for %name

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common = %EVR
Requires: qt5-base-devel
%description devel
%summary.

%package devel-static
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common = %EVR
Requires: %name-devel
%description devel-static
%summary.

%package doc
BuildArch: noarch
Summary: Document for developing apps which will use Qt5 %qt_module
Group: Development/KDE and QT
Requires: %name-common = %EVR
%description doc
This package contains documentation for Qt5 %qt_module

%package -n libqt5-positioning
Summary: Qt5 library
Group: System/Libraries
Requires: %name-common = %EVR
%if_disabled bootstrap
Requires: qt5-quickcontrols
%endif
%description -n libqt5-positioning
%summary

%package -n libqt5-location
Summary: Qt5 library
Group: System/Libraries
Requires: %name-common = %EVR
%if_disabled bootstrap
Requires: qt5-quickcontrols
%endif
%description -n libqt5-location
%summary

%prep
%setup -n %qt_module-opensource-src-%version
syncqt.pl-qt5 -version %version -private

%build
%qmake_qt5
%make_build
%if_disabled bootstrap
%make docs
%endif

%install
%install_qt5
%if_disabled bootstrap
%make INSTALL_ROOT=%buildroot install_docs ||:
%endif

%files common
%files -n libqt5-positioning
%_qt5_libdir/libQt?Positioning.so.*
%_qt5_plugindir/position/
%_qt5_archdatadir/qml/QtPositioning/

%files -n libqt5-location
%_qt5_libdir/libQt?Location.so.*
%_qt5_plugindir/geoservices/
%_qt5_archdatadir/qml/QtLocation/

%files devel
%_qt5_headerdir/QtPositioning/
%_qt5_headerdir/QtLocation/
%_qt5_libdir/libQt*.so
%_qt5_libdatadir/libQt*.so
%_qt5_libdir/libQt*.prl
%_qt5_libdatadir/libQt*.prl
%_qt5_libdir/cmake/Qt*/
%_qt5_libdir/pkgconfig/Qt*.pc
%_qt5_archdatadir/mkspecs/modules/qt_lib_*.pri

%files doc
%if_disabled bootstrap
%_qt5_docdir/*
%endif

%changelog
* Thu Dec 15 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.1-alt1%ubt
- new version

* Sun Oct 16 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.2-alt0.M80P.1
- build for M80P

* Wed Oct 12 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.2-alt1
- new version

* Mon Jun 27 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.1-alt1
- new version

* Thu Mar 24 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.0-alt1
- new version

* Thu Oct 15 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.1-alt1
- new version

* Tue Jul 07 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.0-alt1
- new version

* Tue Jun 09 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.2-alt1
- new version

* Wed Feb 25 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.1-alt1
- new version

* Tue Dec 16 2014 Sergey V Turchin <zerg@altlinux.org> 5.4.0-alt1
- new version

* Wed Sep 17 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.2-alt1
- new version

* Fri Jun 27 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt0.M70P.1
- build for M70P

* Thu Jun 26 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt1
- new version

* Tue Jun 03 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt1
- new version

* Fri Mar 07 2014 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt0.M70P.1
- built for M70P

* Thu Feb 27 2014 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt1
- initial build
