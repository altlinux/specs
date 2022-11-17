%global qt_module qtxmlpatterns
%def_enable bootstrap

Name: qt5-xmlpatterns
Version: 5.15.7
Release: alt1

Group: System/Libraries
Summary: Qt5 - QtXmlPatterns component
Url: http://qt.io/
License: LGPL-2.1 with Qt-LGPL-exception-1.1 or LGPL-3.0-only

Source: %qt_module-everywhere-src-%version.tar

BuildRequires(pre): rpm-macros-qt5
%if_disabled bootstrap
BuildRequires: qt5-tools
%endif
BuildRequires: gcc-c++ glibc-devel qt5-base-devel qt5-declarative-devel

%description
The Qt XML Patterns module provides support for XPath, XQuery, XSLT,
and XML Schema validation.

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
Summary: Document for developing apps which will use Qt5 %qt_module
Group: Development/KDE and QT
Requires: %name-common = %EVR
%description doc
This package contains documentation for Qt5 %qt_module

%package -n libqt5-xmlpatterns
Summary: Qt5 library
Group: System/Libraries
Requires: %name-common = %EVR
Requires: libqt5-core = %_qt5_version
%description -n libqt5-xmlpatterns
%summary

%prep
%setup -n %qt_module-everywhere-src-%version
syncqt.pl-qt5 -version %version

%build
%define qdoc_found %{expand:%%(if [ -e %_qt5_bindir/qdoc ]; then echo 1; else echo 0; fi)}

%qmake_qt5
%make_build
%if %qdoc_found
export QT_HASH_SEED=0
%make docs
%endif

%install
%install_qt5
%if %qdoc_found
%make INSTALL_ROOT=%buildroot install_docs ||:
%endif

%files common
%files -n libqt5-xmlpatterns
%doc LICENSE*EXCEPT*
%_qt5_libdir/libQt?XmlPatterns.so.*
%_qt5_qmldir/QtQuick/XmlListModel/

%files devel
%_qt5_bindir/xmlpatterns*
%_bindir/xmlpatterns*
%_qt5_headerdir/Qt*/
%_qt5_libdir/libQt*.so
%_qt5_libdatadir/libQt*.so
%_qt5_libdir/libQt*.prl
%_qt5_libdatadir/libQt*.prl
%_qt5_libdir/cmake/Qt*/
%_qt5_libdir/pkgconfig/Qt*.pc
%_qt5_archdatadir/mkspecs/modules/*.pri

%files doc
%if %qdoc_found
%_qt5_docdir/*
%endif
%_qt5_examplesdir/*

%changelog
* Tue Nov 15 2022 Sergey V Turchin <zerg@altlinux.org> 5.15.7-alt1
- new version

* Fri Oct 07 2022 Sergey V Turchin <zerg@altlinux.org> 5.15.6-alt1
- new version

* Tue Aug 16 2022 Sergey V Turchin <zerg@altlinux.org> 5.15.4-alt2
- build docs

* Mon Jul 04 2022 Sergey V Turchin <zerg@altlinux.org> 5.15.4-alt1
- new version

* Mon Jan 11 2021 Sergey V Turchin <zerg@altlinux.org> 5.15.2-alt1
- new version

* Thu Sep 10 2020 Sergey V Turchin <zerg@altlinux.org> 5.15.1-alt1
- new version

* Wed Jul 08 2020 Sergey V Turchin <zerg@altlinux.org> 5.15.0-alt1
- new version

* Fri Jul 03 2020 Sergey V Turchin <zerg@altlinux.org> 5.12.9-alt2
- build docs

* Mon Jun 22 2020 Sergey V Turchin <zerg@altlinux.org> 5.12.9-alt1
- new version

* Thu Apr 16 2020 Sergey V Turchin <zerg@altlinux.org> 5.12.8-alt2
- build docs

* Thu Apr 09 2020 Sergey V Turchin <zerg@altlinux.org> 5.12.8-alt1
- new version

* Wed Mar 11 2020 Sergey V Turchin <zerg@altlinux.org> 5.12.7-alt2
- build docs

* Thu Feb 13 2020 Sergey V Turchin <zerg@altlinux.org> 5.12.7-alt1
- new version

* Mon Dec 16 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.6-alt1
- new version

* Fri Oct 18 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.5-alt2
- build docs

* Mon Oct 07 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.5-alt1
- new version

* Mon Jun 24 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.4-alt1
- new version

* Thu Apr 25 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.3-alt1
- new version

* Mon Mar 04 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.2-alt1
- new version

* Thu Dec 13 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.3-alt1
- new version

* Mon Sep 24 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.2-alt1
- new version

* Thu Aug 16 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.1-alt2
- build docs

* Fri Aug 03 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.1-alt1
- new version

* Wed Jun 13 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.6-alt1
- new version

* Tue Apr 17 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.5-alt1
- new version

* Wed Mar 07 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.4-alt1.2
- build docs

* Mon Feb 12 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.4-alt1.1
- don't build docs

* Thu Jan 25 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.4-alt1
- new version

* Tue Dec 05 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.3-alt1
- new version

* Mon Oct 23 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.2-alt2
- build docs

* Fri Oct 06 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.2-alt1
- new version

* Thu Dec 15 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.1-alt1
- new version

* Sun Oct 16 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.2-alt0.M80P.1
- build for M80P

* Wed Oct 12 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.2-alt1
- new version

* Mon Jun 27 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.1-alt1
- new version

* Thu Mar 31 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.0-alt2
- build docs

* Thu Mar 24 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.0-alt1
- new version

* Thu Oct 15 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.1-alt1
- new version

* Mon Jul 06 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.0-alt1
- new version

* Fri Jun 05 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.2-alt1
- new version

* Tue Feb 24 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.1-alt1
- new version

* Fri Dec 12 2014 Sergey V Turchin <zerg@altlinux.org> 5.4.0-alt1
- new version

* Tue Sep 16 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.2-alt1
- new version

* Fri Jun 27 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt0.M70P.1
- build for M70P

* Wed Jun 25 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt1
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
