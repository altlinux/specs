
%global qt_module qtscript

Name: qt5-%qt_module
Version: 5.1.1
Release: alt1

Group: System/Libraries
Summary: Qt5 - QtScript component
Url: http://qt-project.org/
License: LGPLv2 / GPLv3

Source: %qt_module-opensource-src-%version.tar

BuildRequires: gcc-c++ glibc-devel qt5-base-devel qt5-tools

%description
%summary.

%package common
Summary: Common package for %name
Group: System/Configuration/Other
Requires: common-licenses
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

%package -n libqt5-script
Summary: Qt5 library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n libqt5-script
%summary

%prep
%setup -qn %qt_module-opensource-src-%version
syncqt.pl-qt5 \
    -version %version \
    -private \
    -module QtScript \
    -module QtScriptTools \
    #

%build
%qmake_qt5
%make_build
%make docs

%install
%install_qt5
%make INSTALL_ROOT=%buildroot install_docs ||:

%files common
%files -n libqt5-script
%doc LGPL_EXCEPTION.txt
%_qt5_libdir/libQt5Script.so.*
%_qt5_libdir/libQt5ScriptTools.so.*

%files devel
%_qt5_headerdir/Qt*/
%_qt5_libdir/libQt5*.so
%_qt5_libdir/libQt*.prl
%_qt5_libdir/cmake/Qt*/
%_qt5_libdir/pkgconfig/Qt*.pc
%_qt5_archdatadir/mkspecs/modules/*.pri

%files doc
%_qt5_docdir/*

%changelog
* Tue Oct 29 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt1
- initial build
