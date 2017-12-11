
%global qt_module qtquick1
%def_disable qtwebkit

Name: qt5-quick1
Version: 5.9.3
Release: alt1%ubt

Group: System/Libraries
Summary: A declarative language for describing user interfaces in Qt5
License: LGPLv2 / GPLv3
Url: http://qt.io/

Source: %qt_module-opensource-src-%version.tar

BuildRequires(pre): rpm-build-ubt
BuildRequires: rpm-build-qml
BuildRequires: gcc-c++ glibc-devel
BuildRequires: qt5-base-devel qt5-script-devel qt5-declarative-devel qt5-xmlpatterns-devel qt5-tools qt5-tools-devel
%if_enabled qtwebkit
BuildRequires: qt5-webkit-devel
%endif

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

%package -n libqt5-declarative
Summary: Qt5 library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n libqt5-declarative
%summary

%prep
%setup -qn %qt_module-opensource-src-%version
syncqt.pl-qt5 -version %version -private

# fix version
sed -i 's|^MODULE_VERSION[[:space:]]*=.*|MODULE_VERSION = %version|' .qmake.conf


%build
%qmake_qt5
%make_build
#export QT_HASH_SEED=0
#%make docs

%install
%install_qt5
#%make INSTALL_ROOT=%buildroot install_docs ||:

%files common
%dir %_qt5_importdir/Qt/
%dir %_qt5_importdir/Qt/labs/

%files -n libqt5-declarative
%doc LGPL_EXCEPTION.txt
%_qt5_libdir/libQt?Declarative.so.*
%_qt5_bindir/qml*
%_bindir/qml*
%_qt5_importdir/Qt/labs/*
%if_enabled qtwebkit
%_qt5_importdir/QtWebKit/
%endif
%_qt5_importdir/builtins.qmltypes

%files devel
%_qt5_plugindir/designer/*.so
%_qt5_plugindir/qml1tooling/
%_qt5_headerdir/QtDeclarative/
%_qt5_libdir/libQt5Declarative.so
%_qt5_libdatadir/libQt5Declarative.so
%_qt5_libdir/libQt5Declarative.prl
%_qt5_libdatadir/libQt5Declarative.prl
%_qt5_libdir/cmake/Qt5Declarative/
%_qt5_libdir/pkgconfig/Qt5Declarative.pc
%_qt5_archdatadir/mkspecs/modules/qt_lib_declarative*.pri
%_libdir/cmake/Qt5Designer/Qt5Designer_QDeclarativeViewPlugin.cmake

#%files doc
#%_qt5_docdir/*

%changelog
* Tue Dec 05 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.3-alt1%ubt
- new version

* Fri Oct 06 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.2-alt1%ubt
- new version

* Thu Aug 24 2017 Sergey V Turchin <zerg@altlinux.org> 5.7.1-alt2%ubt
- build without qtwebkit

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

* Thu Nov 26 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.1-alt2
- clean build requires

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

* Thu Feb 27 2014 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt0.M70P.1
- built for M70P

* Mon Feb 17 2014 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt1
- new version

* Thu Dec 12 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt0.M70P.1
- built for M70P

* Tue Oct 29 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt1
- initial build
