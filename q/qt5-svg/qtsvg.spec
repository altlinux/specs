%define qdoc_found %{expand:%%(if [ -e %_qt5_bindir/qdoc ]; then echo 1; else echo 0; fi)}
%global qt_module qtsvg

Name: qt5-svg
Version: 5.15.15
Release: alt1

Group: System/Libraries
Summary: Qt5 - Support for rendering and displaying SVG
Url: http://qt.io/
License: LGPLv2 / GPLv3

Source: %qt_module-everywhere-src-%version.tar

BuildRequires(pre): rpm-build-ubt rpm-macros-qt5 qt5-tools
BuildRequires: gcc-c++ glibc-devel qt5-base-devel > 5.5.0-alt3 pkgconfig(zlib)

%description
Scalable Vector Graphics (SVG) is an XML-based language for describing
two-dimensional vector graphics. Qt provides classes for rendering and
displaying SVG drawings in widgets and on other paint devices.

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

%package -n libqt5-svg
Summary: Qt5 library
Group: System/Libraries
Requires: %name-common = %EVR
Requires: libqt5-core = %_qt5_version
Provides: %name = %EVR
%description -n libqt5-svg
%summary

%prep
%setup -n %qt_module-everywhere-src-%version
syncqt.pl-qt5 -version %version

%build
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
%files -n libqt5-svg
%doc LICENSE*EXCEPT*
%_qt5_libdir/libQt?Svg.so.*
%_qt5_plugindir/iconengines/libqsvgicon.so
%_qt5_plugindir/imageformats/libqsvg.so

%files devel
%_qt5_headerdir/QtSvg/
%_qt5_libdir/lib*.so
%_qt5_libdir/lib*.prl
%_qt5_libdatadir/lib*.so
%_qt5_libdatadir/lib*.prl
%_qt5_libdir/cmake/Qt?Svg/
%_qt5_libdir/cmake/Qt?Gui/*Svg*.cmake
%_qt5_libdir/pkgconfig/Qt5Svg.pc
%_qt5_archdatadir/mkspecs/modules/qt_lib_svg*.pri

%files doc
%if %qdoc_found
%_qt5_docdir/*
%endif
%_qt5_examplesdir/*

%changelog
* Wed Sep 11 2024 Sergey V Turchin <zerg@altlinux.org> 5.15.15-alt1
- new version

* Thu Apr 04 2024 Sergey V Turchin <zerg@altlinux.org> 5.15.13-alt1
- new version

* Wed Jan 10 2024 Sergey V Turchin <zerg@altlinux.org> 5.15.12-alt1
- new version

* Wed Nov 22 2023 Sergey V Turchin <zerg@altlinux.org> 5.15.11-alt1
- new version

* Mon Jul 10 2023 Sergey V Turchin <zerg@altlinux.org> 5.15.10-alt1
- new version

* Wed Apr 26 2023 Sergey V Turchin <zerg@altlinux.org> 5.15.9-alt1
- new version

* Wed Jan 18 2023 Sergey V Turchin <zerg@altlinux.org> 5.15.8-alt1
- new version

* Tue Nov 15 2022 Sergey V Turchin <zerg@altlinux.org> 5.15.7-alt1
- new version

* Fri Oct 07 2022 Sergey V Turchin <zerg@altlinux.org> 5.15.6-alt1
- new version

* Mon Jul 04 2022 Sergey V Turchin <zerg@altlinux.org> 5.15.4-alt1
- new version

* Mon Jan 11 2021 Sergey V Turchin <zerg@altlinux.org> 5.15.2-alt1
- new version

* Thu Sep 10 2020 Sergey V Turchin <zerg@altlinux.org> 5.15.1-alt1
- new version

* Fri Jul 10 2020 Sergey V Turchin <zerg@altlinux.org> 5.15.0-alt1
- new version

* Mon Jun 22 2020 Sergey V Turchin <zerg@altlinux.org> 5.12.9-alt1
- new version

* Thu Apr 09 2020 Sergey V Turchin <zerg@altlinux.org> 5.12.8-alt1
- new version

* Thu Feb 13 2020 Sergey V Turchin <zerg@altlinux.org> 5.12.7-alt1
- new version

* Mon Dec 16 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.6-alt1
- new version

* Mon Oct 07 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.5-alt1
- new version

* Mon Jun 24 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.4-alt1
- new version

* Thu Apr 25 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.3-alt1
- new version

* Thu Mar 07 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.2-alt1
- new version

* Thu Dec 13 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.3-alt1
- new version

* Mon Sep 24 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.2-alt1%ubt
- new version

* Fri Aug 03 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.1-alt1%ubt
- new version

* Wed Jun 13 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.6-alt1%ubt
- new version

* Tue Apr 17 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.5-alt1%ubt
- new version

* Thu Jan 25 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.4-alt1%ubt
- new version

* Tue Dec 05 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.3-alt1%ubt
- new version

* Fri Oct 06 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.2-alt1%ubt
- new version

* Thu Aug 17 2017 Sergey V Turchin <zerg@altlinux.org> 5.7.1-alt2%ubt
- provides qt5-svg

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

* Tue Jul 28 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.0-alt2
- install libs into qt prefix

* Tue Jul 07 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.0-alt1
- new version

* Tue Jun 09 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.2-alt1
- new version

* Wed Feb 25 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.1-alt1
- new version

* Tue Dec 16 2014 Sergey V Turchin <zerg@altlinux.org> 5.4.0-alt1
- new version

* Fri Jun 27 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt0.M70P.1
- build for M70P

* Thu Jun 26 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt1
- new version

* Tue Jun 03 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt1
- new version

* Thu Feb 27 2014 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt0.M70P.1
- built for M70P

* Tue Feb 18 2014 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt1
- new version

* Thu Dec 12 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt0.M70P.1
- built for M70P

* Fri Nov 29 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt1
- initial build
