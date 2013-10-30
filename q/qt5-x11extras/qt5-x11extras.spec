
%global qt_module qtx11extras

Name: qt5-x11extras
Version: 5.1.1
Release: alt1

Group: System/Libraries
Summary: Qt5 - X11 support library
Url: http://qt-project.org/
License: LGPLv2 / GPLv3

Source: %qt_module-opensource-src-%version.tar

BuildRequires: gcc-c++ glibc-devel qt5-base-devel qt5-tools

%description
The X11 Extras module provides features specific to platforms using X11, e.g.
Linux and UNIX-like systems including embedded Linux systems that use the X
Window System.

%package common
Summary: Common package for %name
Group: System/Configuration/Other
Requires: common-licenses
BuildArch: noarch
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

%package -n libqt5-x11extras
Summary: Qt5 library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n libqt5-x11extras
%summary

%prep
%setup -n %qt_module-opensource-src-%version
syncqt.pl-qt5 \
    -version %version \
    -private \
    -module QtX11Extras \
    #

%build
%qmake_qt5
%make_build
%make docs

%install
%install_qt5
%make INSTALL_ROOT=%buildroot install_docs ||:

%files common
%files -n libqt5-x11extras
%doc LGPL_EXCEPTION.txt
%_qt5_libdir/libQt?X11Extras.so.*

%files doc
%_qt5_docdir/*

%files devel
%_qt5_headerdir/QtX11Extras/
%_qt5_libdir/libQt*.so
%_qt5_libdir/libQt*.prl
%_qt5_libdir/cmake/Qt*/
%_qt5_libdir/pkgconfig/Qt*.pc
%_qt5_archdatadir/mkspecs/modules/qt_*.pri

%changelog
* Wed Oct 30 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt1
- initial build
