%define rname libkgapi

Name: kf5-%rname
Version: 5.3.1
Release: alt1
%K5init altplace

Group: Graphical desktop/KDE
Summary: Google services APIs
Url: http://www.kde.org
License: GPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Thu Sep 01 2016 (-bi)
# optimized out: cmake cmake-modules elfutils gcc-c++ kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdesignerplugin-devel kf5-kdoctools kf5-kdoctools-devel kf5-kemoticons-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kparts-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libEGL-devel libGL-devel libdbusmenu-qt52 libgpg-error libgst-plugins1.0 libical-devel libjson-c libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-opengl libqt5-positioning libqt5-printsupport libqt5-qml libqt5-quick libqt5-sensors libqt5-sql libqt5-svg libqt5-webchannel libqt5-webkit libqt5-webkitwidgets libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms perl python-base python-modules python3 python3-base qt5-base-devel rpm-build-python3 ruby ruby-stdlibs
#BuildRequires: extra-cmake-modules kde5-kcalcore-devel kde5-kcontacts-devel kf5-kdelibs4support-devel kf5-kdoctools-devel-static kf5-kio-devel python-module-google python3-dev qt5-webkit-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules  qt5-webkit-devel
BuildRequires: kde5-kcalcore-devel kde5-kcontacts-devel
BuildRequires: kf5-kdelibs4support-devel kf5-kdoctools-devel-static kf5-kio-devel

%description
LibKGAPI is a C++ library that implements APIs for various Google services.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: kf5-kcoreaddons-devel kde5-kcalcore-devel kde5-kcontacts-devel
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkf5gapidrive
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5gapidrive
KF5 library

%package -n libkf5gapilatitude
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5gapilatitude
KF5 library

%package -n libkf5gapicore
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5gapicore
KF5 library

%package -n libkf5gapicalendar
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5gapicalendar
KF5 library

%package -n libkf5gapiblogger
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5gapiblogger
KF5 library

%package -n libkf5gapimaps
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5gapimaps
KF5 library

%package -n libkf5gapicontacts
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5gapicontacts
KF5 library

%package -n libkf5gapitasks
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5gapitasks
KF5 library


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
#%find_lang %name --all-name

#files common -f %name.lang
%files common
%doc LICENSE*
%config(noreplace) %_K5xdgconf/*.categories

%files devel
%_K5inc/kgapi_version.h
%_K5inc/KGAPI/
%_K5link/lib*.so
%_K5lib/cmake/KF5GAPI/
%_K5archdata/mkspecs/modules/qt_KGAPI*.pri

%files -n libkf5gapidrive
%_K5lib/libKF5GAPIDrive.so.*
%files -n libkf5gapilatitude
%_K5lib/libKF5GAPILatitude.so.*
%files -n libkf5gapicore
%_K5lib/libKF5GAPICore.so.*
%files -n libkf5gapicalendar
%_K5lib/libKF5GAPICalendar.so.*
%files -n libkf5gapiblogger
%_K5lib/libKF5GAPIBlogger.so.*
%files -n libkf5gapimaps
%_K5lib/libKF5GAPIMaps.so.*
%files -n libkf5gapicontacts
%_K5lib/libKF5GAPIContacts.so.*
%files -n libkf5gapitasks
%_K5lib/libKF5GAPITasks.so.*

%changelog
* Wed Nov 02 2016 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt1
- new version

* Thu Sep 01 2016 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt2
- fix requires

* Thu Sep 01 2016 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt1
- new version

* Tue May 10 2016 Sergey V Turchin <zerg@altlinux.org> 5.1.0-alt2
- update from 5.1 branch

* Tue Dec 22 2015 Sergey V Turchin <zerg@altlinux.org> 5.1.0-alt1
- new version

* Fri Aug 21 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt1
- new version

* Wed Aug 12 2015 Sergey V Turchin <zerg@altlinux.org> 4.80.0-alt1
- initial build
