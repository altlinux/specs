%define qdoc_found %{expand:%%(if [ -e %_qt5_bindir/qdoc ]; then echo 1; else echo 0; fi)}
%global qt_module qtnetworkauth

Name: qt5-networkauth
Version: 5.15.15
Release: alt1

Group: System/Libraries
Summary: Qt Network Authenticators
Url: http://qt.io/
License: GPLv3

Source: %qt_module-everywhere-src-%version.tar

BuildRequires(pre): rpm-macros-qt5 qt5-tools
BuildRequires: gcc-c++ glibc-devel
BuildRequires: qt5-base-devel qt5-tools

%description
Qt Network Authenticators; QtOAuth in particular.

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
Requires: qt5-base-devel rpm-build-qml
%description devel
%summary.

%package doc
Summary: Document for developing apps which will use Qt5 %qt_module
Group: Development/KDE and QT
Requires: %name-common = %EVR
%description doc
This package contains documentation for Qt5 %qt_module

%package -n libqt5-networkauth
Group: System/Libraries
Summary: Qt5 - library
Requires: %name-common = %EVR
Requires: libqt5-core = %_qt5_version
%description -n libqt5-networkauth
%summary

%prep
%setup -n %qt_module-everywhere-src-%version
syncqt.pl-qt5 -version %version

%build
%qmake_qt5
%make_build
%if %qdoc_found
%make docs
%endif

%install
%install_qt5
%if %qdoc_found
%make INSTALL_ROOT=%buildroot install_docs ||:
%endif

%files common

%files -n libqt5-networkauth
%_qt5_libdir/libQt5NetworkAuth.so.*
#%_qt5_plugindir/networkauth/
#%_qt5_qmldir/QtNetworkAuth/

%files devel
%_qt5_libdir/libQt*.so
%_qt5_libdatadir/libQt*.so
%_qt5_libdir/libQt*.prl
%_qt5_libdatadir/libQt*.prl
%_qt5_headerdir/Qt*/
%_qt5_archdatadir/mkspecs/modules/*.pr*
%_libdir/cmake/Qt*/
%_pkgconfigdir/Qt?NetworkAuth.pc

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

* Thu Mar 14 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.2-alt1
- new version

* Thu Jan 31 2019 Sergey V Turchin <zerg@altlinux.org> 5.11.3-alt1
- initial build
