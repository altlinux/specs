%define qdoc_found %{expand:%%(if [ -e %_dqt5_bindir/qdoc ]; then echo 1; else echo 0; fi)}

%global qt_module dqtwebchannel
%def_disable bootstrap

%add_findreq_skiplist %_dqt5_examplesdir/*

Name: dqt5-webchannel
Version: 5.15.13
Release: alt0.dde.1

Group: System/Libraries
Summary: Qt5 - WebChannel component
Url: http://qt.io/
License: LGPLv2 / GPLv3

Source: %qt_module-everywhere-src-%version.tar

# Automatically added by buildreq on Tue Oct 20 2015 (-bi)
# optimized out: elfutils kf5-attica-devel kf5-kjs-devel libGL-devel libdqt5-clucene libdqt5-core libdqt5-gui libdqt5-help libdqt5-network libdqt5-qml libdqt5-quick libdqt5-sql libdqt5-widgets libdqt5-xml libstdc++-devel pkg-config python-base python3 python3-base dqt5-base-devel dqt5-declarative-devel dqt5-phonon-devel dqt5-script-devel dqt5-tools dqt5-webkit-devel ruby ruby-stdlibs
#BuildRequires: gcc-c++ glibc-devel-static kde5-akonadi-calendar-devel kde5-gpgmepp-devel kde5-kalarmcal-devel kde5-kblog-devel kde5-kcalcore-devel kde5-kcalutils-devel kde5-kcontacts-devel kde5-kholidays-devel kde5-kidentitymanagement-devel kde5-kimap-devel kde5-kldap-devel kde5-kmailtransport-devel kde5-kmbox-devel kde5-kmime-devel kde5-kontactinterface-devel kde5-kpimtextedit-devel kde5-ktnef-devel kde5-pimlibs-devel kde5-syndication-devel kf5-bluez-qt-devel kf5-kactivities-devel kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcmutils-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdeclarative-devel kf5-kdesu-devel kf5-kdewebkit-devel kf5-kdnssd-devel kf5-kemoticons-devel kf5-kglobalaccel-devel kf5-kguiaddons-devel kf5-khtml-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kidletime-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kjsembed-devel kf5-knewstuff-devel kf5-knotifications-devel kf5-knotifyconfig-devel kf5-kparts-devel kf5-kpeople-devel kf5-kplotting-devel kf5-kpty-devel kf5-kross-devel kf5-krunner-devel kf5-kservice-devel kf5-ktexteditor-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwallet-devel kf5-kwayland-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-kxmlrpcclient-devel kf5-libkgapi-devel kf5-libkscreen-devel kf5-modemmanager-qt-devel kf5-networkmanager-qt-devel kf5-solid-devel kf5-sonnet-devel kf5-threadweaver-devel python-module-google dqt5-connectivity-devel dqt5-multimedia-devel dqt5-quick1-devel dqt5-sensors-devel dqt5-serialport-devel dqt5-svg-devel dqt5-tools-devel dqt5-websockets-devel dqt5-x11extras-devel dqt5-xmlpatterns-devel rpm-build-python3 rpm-build-ruby
BuildRequires(pre): rpm-build-ubt rpm-macros-dqt5
BuildRequires: gcc-c++ glibc-devel dqt5-base-devel
BuildRequires: dqt5-websockets-devel dqt5-declarative-devel
%if_disabled bootstrap
BuildRequires(pre): dqt5-tools
%endif

# find libraries
%add_findprov_lib_path %_dqt5_libdir

%description
The Qt WebChannel module provides a library for seamless integration of C++
and QML applications with HTML/JavaScript clients. Any QObject can be
published to remote clients, where its public API becomes available.

%package common
Summary: Common package for %name
Group: System/Configuration/Other
BuildArch: noarch
Requires: dqt5-base-common
%description common
Common package for %name

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common = %EVR
Requires: dqt5-base-devel
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

%package -n libdqt5-webchannel
Summary: Qt5 library
Group: System/Libraries
Requires: %name-common = %EVR
Requires: libdqt5-core = %_dqt5_version
AutoProv: no,lib
%description -n libdqt5-webchannel
%summary

%prep
%setup -qn %qt_module-everywhere-src-%version
syncqt.pl-dqt5 -version %version

%build
%qmake_dqt5
%make_build
%if_disabled bootstrap
%if %qdoc_found
export QT_HASH_SEED=0
%make docs
%endif
%endif

%install
%install_dqt5
%if_disabled bootstrap
%if %qdoc_found
%make INSTALL_ROOT=%buildroot install_docs ||:
%endif
%endif

%files common
%files -n libdqt5-webchannel
%doc LICENSE*EXCEPT*
%_dqt5_libdir/libQt?WebChannel.so.*
%_dqt5_qmldir/QtWebChannel/

%files devel
%_dqt5_headerdir/Qt*/
%_dqt5_libdir/libQt*.so
%_dqt5_libdatadir/libQt*.so
%_dqt5_libdir/libQt*.prl
%_dqt5_libdatadir/libQt*.prl
%_dqt5_libdir/cmake/Qt*/
%_dqt5_libdir/pkgconfig/Qt*.pc
%_dqt5_archdatadir/mkspecs/modules/*.pri

%files doc
%if_disabled bootstrap
%if %qdoc_found
%_dqt5_docdir/*
%endif
%endif
%_dqt5_examplesdir/*

%changelog
* Thu Jul 25 2024 Leontiy Volodin <lvol@altlinux.org> 5.15.13-alt0.dde.1
- fork qtbase for separate deepin buildings (ALT #48138)

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

* Thu Sep 30 2021 Ivan A. Melnikov <iv@altlinux.org> 5.15.2-alt2
- exclude examples from findreq to avoid node dependency

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

* Wed Mar 06 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.2-alt1
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

* Tue Oct 20 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.1-alt1
- initial build
