
%global qt_module qtquick1

Name: qt5-quick1
Version: 5.1.1
Release: alt1

Group: System/Libraries
Summary: A declarative language for describing user interfaces in Qt5
License: LGPLv2 / GPLv3
Url: http://qt-project.org/

Source: %qt_module-opensource-src-%version.tar

BuildRequires: gcc-c++ glibc-devel
BuildRequires: qt5-base-devel qt5-script-devel qt5-webkit-devel qt5-xmlpatterns-devel qt5-tools qt5-tools-devel

%description
Qt Quick is a collection of technologies that are designed to help
developers create the kind of intuitive, modern, fluid user interfaces
that are increasingly used on mobile phones, media players, set-top
boxes and other portable devices.

Qt Quick consists of a rich set of user interface elements, a declarative
language for describing user interfaces and a language runtime. A
collection of C++ APIs is used to integrate these high level features
with classic Qt applications.

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

%package -n libqt5-declarative
Summary: Qt5 library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n libqt5-declarative
%summary

%prep
%setup -qn %qt_module-opensource-src-%version
syncqt.pl-qt5 \
    -version %version \
    -private \
    -module QtDeclarative \
    #

%build
%qmake_qt5
%make_build
#%make docs

%install
%install_qt5
#%make INSTALL_ROOT=%buildroot install_docs ||:

%files common
%files -n libqt5-declarative
%doc LGPL_EXCEPTION.txt
%_qt5_libdir/libQt?Declarative.so.*
%_qt5_bindir/qml*
%_bindir/qml*
%_qt5_importdir/Qt/labs/*
%_qt5_importdir/QtWebKit/
%_qt5_importdir/builtins.qmltypes

%files devel
%_qt5_plugindir/designer/*.so
%_qt5_plugindir/qml1tooling/
%_qt5_headerdir/QtDeclarative/
%_qt5_libdir/libQt5Declarative.so
%_qt5_libdir/libQt5Declarative.prl
%_qt5_libdir/cmake/Qt5Declarative/
%_qt5_libdir/pkgconfig/Qt5Declarative.pc
%_qt5_archdatadir/mkspecs/modules/qt_lib_declarative.pri

#%files doc
#%_qt5_docdir/*

%changelog
* Tue Oct 29 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt1
- initial build
