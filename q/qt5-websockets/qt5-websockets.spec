
%global qt_module qtwebsockets

Name: qt5-websockets
Version: 5.4.0
Release: alt1

Group: System/Libraries
Summary: Qt5 - QtWebSockets component
Url: http://qt-project.org/
License: LGPLv2 / GPLv3

Source: %qt_module-opensource-src-%version.tar

# Automatically added by buildreq on Mon Jun 16 2014 (-bi)
# optimized out: elfutils libcloog-isl4 libqt5-clucene libqt5-core libqt5-gui libqt5-help libqt5-network libqt5-qml libqt5-sql libqt5-widgets libqt5-xml libstdc++-devel pkg-config python-base qt5-base-devel qt5-declarative-devel qt5-tools ruby ruby-stdlibs
BuildRequires: gcc-c++ glibc-devel qt5-script-devel qt5-tools-devel qt5-webkit-devel qt5-xmlpatterns-devel

%description
QtWebSockets is a pure Qt implementation of WebSockets - both client and server.

%package common
Summary: Common package for %name
Group: System/Configuration/Other
BuildArch: noarch
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

%package -n libqt5-websockets
Summary: Qt5 library
Group: System/Libraries
Requires: %name-common = %EVR
Requires: qt5-declarative-common
%description -n libqt5-websockets
%summary

%prep
%setup -qn %qt_module-opensource-src-%version
syncqt.pl-qt5 \
    -version %version \
    -private \
    -module QtWebSockets \
    #

%build
%qmake_qt5
%make_build
%make docs

%install
%install_qt5
%make INSTALL_ROOT=%buildroot install_docs ||:

%files common
%files -n libqt5-websockets
%_qt5_libdir/libQt?WebSockets.so.*
%_qt5_archdatadir/qml/Qt/WebSockets/

%files devel
%_qt5_headerdir/Qt*/
%_qt5_libdir/libQt*.so
%_qt5_libdir/libQt*.prl
%_qt5_libdir/cmake/Qt*/
%_qt5_libdir/pkgconfig/Qt*.pc
%_qt5_archdatadir/mkspecs/modules/*.pri

%files doc
%_qt5_docdir/*

%changelog
* Tue Dec 16 2014 Sergey V Turchin <zerg@altlinux.org> 5.4.0-alt1
- new version

* Wed Sep 17 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.2-alt1
- new version

* Fri Jun 27 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt0.M70P.1
- build for M70P

* Thu Jun 26 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt1
- new version

* Mon Jun 16 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt1
- initial build
