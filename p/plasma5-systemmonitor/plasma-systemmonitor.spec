%define rname plasma-systemmonitor

Name: plasma5-systemmonitor
Version: 5.26.3
Release: alt1
%K5init altplace no_appdata

Group: Graphical desktop/KDE
Summary: KDE Plasma 5 system resources monitor
Url: http://www.kde.org
License: GPL-2.0-or-later

Requires: lm_sensors plasma5-libksysguard plasma5-ksystemstats
Provides: plasma5-plasma-systemmonitor = %EVR
Obsoletes: plasma5-plasma-systemmonitor = %EVR
Provides: plasma5-plasma-systemmonitor-common = %EVR
Obsoletes: plasma5-plasma-systemmonitor-common = %EVR

Source: %rname-%version.tar
Patch: alt-uid-500.patch

# Automatically added by buildreq on Fri Jul 02 2021 (-bi)
# optimized out: cmake cmake-modules debugedit elfutils fontconfig gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 kf5-attica-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-common kf5-kcoreaddons-devel kf5-kitemviews-devel kf5-kjobwidgets-common kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-common kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel libctf-nobfd0 libglvnd-devel libgpg-error libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-qml libqt5-qmlmodels libqt5-quick libqt5-quickcontrols2 libqt5-svg libqt5-waylandclient libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libssl-devel libstdc++-devel libwayland-client libwayland-cursor libxcbutil-keysyms perl python-modules python2-base python3 python3-base python3-module-paste qt5-base-common qt5-base-devel qt5-declarative-devel rpm-build-python3 rpm-build-qml rpm-macros-python sh4 tzdata
#BuildRequires: appstream extra-cmake-modules kf5-kdbusaddons-devel kf5-kdeclarative-devel kf5-kglobalaccel-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel kf5-kirigami-devel kf5-kitemmodels-devel kf5-knewstuff-devel kf5-kpackage-devel libkf5plasmaquick plasma5-libksysguard-devel python-modules-compiler python3-dev python3-module-mpl_toolkits qt5-quickcontrols2-devel qt5-svg-devel qt5-translations qt5-wayland-devel
BuildRequires(pre): rpm-build-kf5
BuildRequires: qt5-base-devel qt5-quickcontrols2-devel qt5-svg-devel qt5-wayland-devel
BuildRequires: plasma5-libksysguard-devel
BuildRequires: extra-cmake-modules
BuildRequires: kf5-kdbusaddons-devel kf5-kdeclarative-devel kf5-kglobalaccel-devel kf5-ki18n-devel kf5-kiconthemes-devel
BuildRequires: kf5-kio-devel kf5-kirigami-devel kf5-kitemmodels-devel kf5-knewstuff-devel kf5-kpackage-devel

%description
%name provides an interface for monitoring system sensors,
process information and other system resources. It is built on top of the faces
system also used to provide widgets for plasma-desktop and makes use of the
ksystemstats daemon to provide sensor information. It allows extensive
customisation of pages, so it can be made to show exactly which data people
want to see.

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
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libplasma-systemmonitor
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n libplasma-systemmonitor
%name library


%prep
%setup -n %rname-%version
%patch -p1

%build
%K5build

%install
%K5install
%K5install_move data ksysguard plasma-systemmonitor knsrcfiles plasma
%find_lang %name --all-name

%files -f %name.lang
%doc LICENSES/*
%_K5bin/plasma-systemmonitor
%_K5qml/org/kde/ksysguard/*
%_K5data/ksysguard/
%_K5data/plasma-systemmonitor/
%_K5xdgapp/*systemmonitor*.desktop
%_K5cfg/*systemmonitor*
%_K5data/knsrcfiles/*systemmonitor*
%_K5data/plasma/kinfocenter/externalmodules/*systemmonitor*.desktop

#%files devel
#%_K5inc/plasma-systemmonitor_version.h
#%_K5inc/plasma-systemmonitor/
#%_K5link/lib*.so
#%_K5lib/cmake/plasma-systemmonitor
#%_K5archdata/mkspecs/modules/qt_plasma-systemmonitor.pri

#%files -n libplasma-systemmonitor
#%_K5lib/libplasma-systemmonitor.so.*

%changelog
* Tue Nov 08 2022 Sergey V Turchin <zerg@altlinux.org> 5.26.3-alt1
- new version

* Thu Oct 27 2022 Sergey V Turchin <zerg@altlinux.org> 5.26.2-alt1
- new version

* Wed Sep 07 2022 Sergey V Turchin <zerg@altlinux.org> 5.25.5-alt1
- new version

* Wed Aug 17 2022 Sergey V Turchin <zerg@altlinux.org> 5.25.4-alt1
- new version

* Mon Jul 11 2022 Sergey V Turchin <zerg@altlinux.org> 5.24.6-alt1
- new version

* Wed May 04 2022 Sergey V Turchin <zerg@altlinux.org> 5.24.5-alt1
- new version

* Wed Mar 30 2022 Sergey V Turchin <zerg@altlinux.org> 5.24.4-alt1
- new version

* Mon Jan 10 2022 Sergey V Turchin <zerg@altlinux.org> 5.23.5-alt1
- new version

* Wed Dec 01 2021 Sergey V Turchin <zerg@altlinux.org> 5.23.4-alt1
- new version

* Tue Nov 30 2021 Oleg Solovyov <mcpain@altlinux.org> 5.23.3-alt2
- Start userid from 500 (Closes: #41469)

* Wed Nov 10 2021 Sergey V Turchin <zerg@altlinux.org> 5.23.3-alt1
- new version

* Mon Nov 01 2021 Sergey V Turchin <zerg@altlinux.org> 5.23.2-alt1
- new version

* Wed Sep 01 2021 Sergey V Turchin <zerg@altlinux.org> 5.22.5-alt1
- new version

* Tue Jul 27 2021 Sergey V Turchin <zerg@altlinux.org> 5.22.4-alt1
- new version

* Wed Jul 07 2021 Sergey V Turchin <zerg@altlinux.org> 5.22.3-alt1
- new version

* Thu Jul 01 2021 Sergey V Turchin <zerg@altlinux.org> 5.22.2-alt1
- initial build
