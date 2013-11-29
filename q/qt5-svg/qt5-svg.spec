
%global qt_module qtsvg

Name: qt5-svg
Version: 5.1.1
Release: alt1

Group: System/Libraries
Summary: Qt5 - Support for rendering and displaying SVG
License: LGPLv2 / GPLv3

Source: %qt_module-opensource-src-%version.tar

BuildRequires: gcc-c++ glibc-devel qt5-base-devel pkgconfig(zlib) qt5-tools

%description
Scalable Vector Graphics (SVG) is an XML-based language for describing
two-dimensional vector graphics. Qt provides classes for rendering and
displaying SVG drawings in widgets and on other paint devices.

%package common
Summary: Common package for %name
Group: System/Configuration/Other
Requires: common-licenses
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

%package -n libqt5-svg
Summary: Qt5 library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n libqt5-svg
%summary

%prep
%setup -n %qt_module-opensource-src-%version
syncqt.pl-qt5 \
    -version %version \
    -private \
    -module QtSvg \
    #

%build
%qmake_qt5
%make_build
%make docs

%install
%install_qt5
%make INSTALL_ROOT=%buildroot install_docs ||:

%files common
%files -n libqt5-svg
%doc LGPL_EXCEPTION.txt
%_qt5_libdir/libQt?Svg.so.*
%_qt5_plugindir/iconengines/libqsvgicon.so
%_qt5_plugindir/imageformats/libqsvg.so

%files devel
%_qt5_headerdir/QtSvg/
%_qt5_libdir/lib*.so
%_qt5_libdir/lib*.prl
%_qt5_libdir/cmake/Qt?Svg/
%_qt5_libdir/pkgconfig/Qt?Svg.pc
%_qt5_archdatadir/mkspecs/modules/qt_lib_svg.pri

%files doc
%_qt5_docdir/qtsvg.qch
%_qt5_docdir/qtsvg/

%changelog
* Fri Nov 29 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt1
- initial build
