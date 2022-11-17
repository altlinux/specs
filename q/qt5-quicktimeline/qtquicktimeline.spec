%define qdoc_found %{expand:%%(if [ -e %_qt5_bindir/qdoc ]; then echo 1; else echo 0; fi)}
%global qt_module qtquicktimeline

Name: qt5-quicktimeline
Version: 5.15.7
Release: alt1

Group: System/Libraries
Summary: Qt5 - Keyframe-based timeline construction
Url: http://www.kde.org
License: GPL-3.0-or-later

Requires: libqt5-core = %_qt5_version
Requires: %name-common

Source: %qt_module-everywhere-src-%version.tar

BuildRequires(pre): rpm-macros-qt5
# Automatically added by buildreq on Tue Aug 18 2020 (-bi)
# optimized out: clang10.0-libs elfutils fontconfig gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 kde5-kmime-devel kf5-attica-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcalcore-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcontacts-devel kf5-kcoreaddons-devel kf5-kfilemetadata-devel kf5-ki18n-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kjs-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libglvnd-devel libqt5-core libqt5-gui libqt5-help libqt5-network libqt5-qml libqt5-qmlmodels libqt5-quick libqt5-sql libqt5-widgets libstdc++-devel llvm10.0-libs perl python-modules python2-base python3 python3-base python3-dev qt5-base-common qt5-base-devel qt5-declarative-devel qt5-location-devel qt5-svg-devel qt5-tools qt5-webchannel-devel rpm-build-python3 rpm-build-qml sh4 tzdata
#BuildRequires: branding-alt-server-release kde5-akonadi-calendar-devel kde5-akonadi-contacts-devel kde5-akonadi-devel kde5-akonadi-mime-devel kde5-akonadi-notes-devel kde5-calendarsupport-devel kde5-eventviews-devel kde5-grantleetheme-devel kde5-incidenceeditor-devel kde5-kalarmcal-devel kde5-kcalutils-devel kde5-kdav-devel kde5-kdb-devel kde5-kidentitymanagement-devel kde5-kimap-devel kde5-kldap-devel kde5-kmailtransport-devel kde5-kmbox-devel kde5-kontactinterface-devel kde5-kpimtextedit-devel kde5-ktnef-devel kde5-libgravatar-devel kde5-libkcddb-devel kde5-libkcompactdisc-devel kde5-libkdepim-devel kde5-libkgapi-devel kde5-libkleo-devel kde5-libksieve-devel kde5-mailimporter-devel kde5-marble-devel kde5-pim-apps-libs-devel kde5-pimcommon-devel kf5-baloo-devel kf5-bluez-qt-devel kf5-kactivities-devel kf5-kactivities-stats-devel kf5-karchive-devel kf5-kcmutils-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdeclarative-devel kf5-kdesu-devel kf5-kdiagram-devel kf5-kdnssd-devel kf5-kemoticons-devel kf5-kglobalaccel-devel kf5-kguiaddons-devel kf5-kholidays-devel kf5-khtml-devel kf5-kiconthemes-devel kf5-kidletime-devel kf5-kio-devel kf5-kirigami-devel kf5-kitemmodels-devel kf5-kjsembed-devel kf5-knewstuff-devel kf5-knotifications-devel kf5-knotifyconfig-devel kf5-kparts-devel kf5-kpeople-devel kf5-kplotting-devel kf5-kpty-devel kf5-kreport-devel kf5-kross-devel kf5-krunner-devel kf5-ktexteditor-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwallet-devel kf5-kwayland-devel kf5-kxmlrpcclient-devel kf5-prison-devel kf5-syndication-devel kf5-syntax-highlighting-devel kf5-threadweaver-devel libqtav-devel plasma5-libkscreen-devel python-modules-compiler python3-module-mpl_toolkits qt5-3d-devel qt5-base-doc qt5-charts-devel qt5-connectivity-devel qt5-datavis3d-devel qt5-doc qt5-multimedia-devel qt5-networkauth-devel qt5-phonon-devel qt5-quickcontrols2-devel qt5-remoteobjects-devel qt5-script-devel qt5-scxml-devel qt5-sensors-devel qt5-serialport-devel qt5-speech-devel qt5-sql-sqlite3 qt5-tools-devel qt5-translations qt5-wayland-devel qt5-webengine-devel qt5-websockets-devel qt5-x11extras-devel qt5-xmlpatterns-devel tbb-devel
BuildRequires: qt5-base-devel qt5-declarative-devel

%description
Module for keyframe-based timeline construction.

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
Requires: %name-common
Requires: qt5-base-devel rpm-build-qml
%description devel
%summary.

%package doc
Summary: Document for developing apps which will use Qt5 %qt_module
Group: Development/KDE and QT
Requires: %name-common
%description doc
This package contains documentation for Qt5 %qt_module

%package -n libqt5-quicktimeline
Group: System/Libraries
Summary: Qt5 - library
Requires: %name-common
Requires: libqt5-core = %_qt5_version
%description -n libqt5-quicktimeline
%summary


%prep
%setup -n %qt_module-everywhere-src-%version
#syncqt.pl-qt5 -version %version

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

%files
%_qt5_qmldir/QtQuick/Timeline/

%files doc
%if %qdoc_found
%_qt5_docdir/*
%endif
#%_qt5_examplesdir/*

%changelog
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

* Tue Aug 18 2020 Sergey V Turchin <zerg@altlinux.org> 5.15.0-alt1
- initial build
