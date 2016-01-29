%define rname plasma-mediacenter

%define sover 5
%define libplasmamediacenter libplasmamediacenter%sover

Name: kf5-%rname
Version: 5.5.4
Release: alt1
%K5init altplace

Group: Graphical desktop/KDE
Summary: KDE Workspace 5 Media Center
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Requires: libqt5-multimedia kf5-baloo

Source: %rname-%version.tar

# Automatically added by buildreq on Wed Oct 14 2015 (-bi)
# optimized out: cmake cmake-modules elfutils gtk-update-icon-cache libEGL-devel libGL-devel libqt5-core libqt5-dbus libqt5-gui libqt5-multimedia libqt5-network libqt5-qml libqt5-quick libqt5-svg libqt5-test libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms python-base python3 python3-base qt5-base-devel qt5-declarative-devel rpm-build-gir ruby ruby-stdlibs
#BuildRequires: extra-cmake-modules gcc-c++ kf5-baloo-devel kf5-kactivities-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdeclarative-devel kf5-kfilemetadata-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kpackage-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-plasma-framework-devel kf5-solid-devel liblmdb-devel libtag-devel python-module-google qt5-multimedia-devel rpm-build-python3 rpm-build-ruby
BuildRequires(pre): rpm-build-kf5
BuildRequires: liblmdb-devel libtag-devel
BuildRequires: extra-cmake-modules gcc-c++ qt5-base-devel qt5-multimedia-devel
BuildRequires: kf5-baloo-devel kf5-kactivities-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel
BuildRequires: kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdeclarative-devel kf5-kfilemetadata-devel
BuildRequires: kf5-kguiaddons-devel kf5-ki18n-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kpackage-devel
BuildRequires: kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-plasma-framework-devel kf5-solid-devel

%description
Plasma Media Center is designed to provide an easy and comfortable way to watch your videos,
browse your photo collection and listen to your music, all in one place.

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

%package -n %libplasmamediacenter
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libplasmamediacenter
KF5 library


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%find_lang %name --all-name

%files common -f %name.lang
%doc COPYING*

%files
%_K5plug/plasma/mediacenter/
%_K5qml/org/kde/plasma/mediacenter/
%_K5xdgapp/plasma-mediacenter.desktop
%_K5data/plasma/shells/org.kde.plasma.mediacenter/
%_K5icon/*/*/actions/pmc-*.*
%_K5srv/plasma*mediacenter.desktop
%_K5srvtyp/pmc_*.desktop

#%files devel
#%_K5inc/plasma-mediacenter_version.h
#%_K5inc/plasma-mediacenter/
#%_K5link/lib*.so
#%_K5lib/cmake/plasma-mediacenter
#%_K5archdata/mkspecs/modules/qt_plasma-mediacenter.pri

%files -n %libplasmamediacenter
%_K5lib/libplasmamediacenter.so.%sover
%_K5lib/libplasmamediacenter.so.*

%changelog
* Thu Jan 28 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.4-alt1
- new version

* Thu Jan 14 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.3-alt1
- new version

* Tue Dec 29 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.2-alt1
- new version

* Thu Dec 17 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.1-alt1
- new version

* Wed Dec 09 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.0-alt1
- new version

* Thu Nov 19 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.3-alt3
- rebuild

* Wed Nov 11 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.3-alt1
- new version

* Wed Oct 14 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.2-alt1
- initial build
