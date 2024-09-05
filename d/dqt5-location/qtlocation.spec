%define qdoc_found %{expand:%%(if [ -e %_dqt5_bindir/qdoc ]; then echo 1; else echo 0; fi)}

%define optflags_lto %nil
%global qt_module dqtlocation
%def_disable bootstrap

Name: dqt5-location
Version: 5.15.13
Release: alt1.0.dde.1

Group: System/Libraries
Summary: Qt5 - QtLocation component
Url: http://qt.io/
License: LGPLv2 / GPLv3

Source: %qt_module-everywhere-src-%version.tar
Patch1: gcc13-compilefix.patch

# Automatically added by buildreq on Wed Aug 23 2017 (-bi)
# optimized out: elfutils fontconfig gcc-c++ glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 kde5-kcalcore-devel kde5-kcontacts-devel kde5-kmime-devel kde5-libkleo-devel kf5-attica-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-ki18n-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kjs-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libGL-devel libdbus-devel libdbus-glib libdbus-glib-devel libgpg-error libdqt5-clucene libdqt5-core libdqt5-dbus libdqt5-gui libdqt5-help libdqt5-network libdqt5-qml libdqt5-quick libdqt5-sql libdqt5-widgets libstdc++-devel perl pkg-config python-base python-modules python3 python3-base dqt5-base-common dqt5-base-devel dqt5-declarative-devel dqt5-location-devel dqt5-script-devel dqt5-tools dqt5-webchannel-devel dqt5-webkit-devel dqt5-xmlpatterns-devel rpm-build-python3 ruby ruby-stdlibs
#BuildRequires: kde5-akonadi-calendar-devel kde5-akonadi-contacts-devel kde5-akonadi-devel kde5-akonadi-mime-devel kde5-akonadi-notes-devel kde5-calendarsupport-devel kde5-eventviews-devel kde5-grantleetheme-devel kde5-incidenceeditor-devel kde5-kalarmcal-devel kde5-kblog-devel kde5-kcalutils-devel kde5-kdav-devel kde5-kholidays-devel kde5-kidentitymanagement-devel kde5-kimap-devel kde5-kldap-devel kde5-kmailtransport-devel kde5-kmbox-devel kde5-kontactinterface-devel kde5-kpimtextedit-devel kde5-ktnef-devel kde5-libgravatar-devel kde5-libkcddb-devel kde5-libkcompactdisc-devel kde5-libkdepim-devel kde5-libksieve-devel kde5-mailcommon-devel kde5-mailimporter-devel kde5-messagelib-devel kde5-pim-apps-libs-devel kde5-pimcommon-devel kde5-syndication-devel kf5-bluez-qt-devel kf5-kactivities-devel kf5-kactivities-stats-devel kf5-karchive-devel kf5-kcmutils-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdeclarative-devel kf5-kdesu-devel kf5-kdewebkit-devel kf5-kdiagram-devel kf5-kdnssd-devel kf5-kemoticons-devel kf5-kglobalaccel-devel kf5-kguiaddons-devel kf5-khtml-devel kf5-kiconthemes-devel kf5-kidletime-devel kf5-kio-devel kf5-kirigami-devel kf5-kitemmodels-devel kf5-kjsembed-devel kf5-knewstuff-devel kf5-knotifications-devel kf5-knotifyconfig-devel kf5-kparts-devel kf5-kpeople-devel kf5-kplotting-devel kf5-kpty-devel kf5-kross-devel kf5-krunner-devel kf5-ktexteditor-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwallet-devel kf5-kwayland-devel kf5-kwindowsystem-devel kf5-kxmlrpcclient-devel kf5-libkgapi-devel kf5-libkscreen-devel kf5-modemmanager-qt-devel kf5-networkmanager-qt-devel kf5-prison-devel kf5-syntax-highlighting-devel kf5-threadweaver-devel libGConf-devel libgypsy-devel libqtav-devel python-module-google python3-dev python3-module-zope dqt5-connectivity-devel dqt5-multimedia-devel dqt5-phonon-devel dqt5-quick1-devel dqt5-quickcontrols2-devel dqt5-sensors-devel dqt5-serialport-devel dqt5-svg-devel dqt5-tools-devel dqt5-webengine-devel dqt5-websockets-devel dqt5-x11extras-devel rpm-build-ruby
BuildRequires(pre): rpm-build-ubt rpm-macros-dqt5
BuildRequires: gcc-c++ glibc-devel dqt5-declarative-devel dqt5-xmlpatterns-devel dqt5-serialport-devel
BuildRequires: pkgconfig(gconf-2.0)
BuildRequires: libicu-devel zlib-devel libssl-devel
%if_disabled bootstrap
BuildRequires(pre): dqt5-tools
%endif
# 3rdparty
BuildRequires: boost-geometry-devel

# find libraries
%add_findprov_lib_path %_dqt5_libdir

%description
The Qt Positioning API gives developers the ability to determine a position
by using a variety of possible sources, including satellite, or wifi, or
 text file, and so on. That information can then be used to for example
determine a position on a map. In addition satellite information can be
retrieved and area based monitoring can be performed.

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

%package -n libdqt5-positioning
Summary: Qt5 library
Group: System/Libraries
AutoProv: no,lib
Requires: %name-common = %EVR
Requires: libdqt5-core = %_dqt5_version
%if_disabled bootstrap
Requires: dqt5-quickcontrols
%endif
%description -n libdqt5-positioning
%summary

%package -n libdqt5-positioningquick
Summary: Qt5 library
Group: System/Libraries
Requires: %name-common = %EVR
Requires: libdqt5-core = %_dqt5_version
%if_disabled bootstrap
Requires: dqt5-quickcontrols
%endif
%description -n libdqt5-positioningquick
%summary

%package -n libdqt5-location
Summary: Qt5 library
Group: System/Libraries
AutoProv: no,lib
Requires: %name-common = %EVR
Requires: libdqt5-core = %_dqt5_version
%if_disabled bootstrap
Requires: dqt5-quickcontrols
%endif
%description -n libdqt5-location
%summary

%prep
%setup -n %qt_module-everywhere-src-%version
%patch1 -p1
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
%files -n libdqt5-positioning
%_dqt5_libdir/libQt?Positioning.so.*
%_dqt5_plugindir/position/
%_dqt5_qmldir/QtPositioning/

%files -n libdqt5-positioningquick
%_dqt5_libdir/libQt?PositioningQuick.so.*

%files -n libdqt5-location
%_dqt5_libdir/libQt?Location.so.*
%_dqt5_plugindir/geoservices/
%_dqt5_qmldir/QtLocation/
#%_dqt5_qmldir/Qt/labs/location/

%files devel
%_dqt5_headerdir/QtPositioning/
%_dqt5_headerdir/QtPositioningQuick/
%_dqt5_headerdir/QtLocation/
%_dqt5_libdir/libQt*.so
%_dqt5_libdatadir/libQt*.so
%_dqt5_libdir/libQt*.prl
%_dqt5_libdatadir/libQt*.prl
%_dqt5_libdir/cmake/Qt*/
%_dqt5_libdir/pkgconfig/Qt*.pc
%_dqt5_archdatadir/mkspecs/modules/qt_lib_*.pri

%files doc
%if_disabled bootstrap
%if %qdoc_found
%_dqt5_docdir/*
%endif
%endif
%_dqt5_examplesdir/*

%changelog
* Thu Jul 25 2024 Leontiy Volodin <lvol@altlinux.org> 5.15.13-alt1.0.dde.1
- fork qt5 for separate deepin buildings (ALT #48138)

* Mon Apr 15 2024 Michael Shigorin <mike@altlinux.org> 5.15.13-alt1.1
- spec: drop obsolete e2kv3-only hack for old lcc

* Thu Apr 04 2024 Sergey V Turchin <zerg@altlinux.org> 5.15.13-alt1
- new version

* Wed Jan 10 2024 Sergey V Turchin <zerg@altlinux.org> 5.15.12-alt1
- new version

* Wed Nov 22 2023 Sergey V Turchin <zerg@altlinux.org> 5.15.11-alt1
- new version

* Mon Jul 10 2023 Sergey V Turchin <zerg@altlinux.org> 5.15.10-alt1
- new version

* Thu Jun 01 2023 Sergey V Turchin <zerg@altlinux.org> 5.15.9-alt2
- fixed compilation with GCC 13 (thanks asheplyakov@alt) (closes: #46360)

* Wed Apr 26 2023 Sergey V Turchin <zerg@altlinux.org> 5.15.9-alt1
- new version

* Thu Jan 26 2023 Sergey V Turchin <zerg@altlinux.org> 5.15.8-alt2
- disable LTO

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

* Wed Mar 06 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.2-alt1
- new version

* Thu Dec 13 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.3-alt1
- new version

* Fri Oct 19 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.2-alt2%ubt
- update build requres

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

* Thu Aug 24 2017 Sergey V Turchin <zerg@altlinux.org> 5.7.1-alt3%ubt
- fix to build with lcc compiler

* Wed Aug 23 2017 Sergey V Turchin <zerg@altlinux.org> 5.7.1-alt2%ubt
- fix build requires

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

* Fri Mar 07 2014 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt0.M70P.1
- built for M70P

* Thu Feb 27 2014 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt1
- initial build
