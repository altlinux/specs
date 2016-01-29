%define rname plasma-pa

%define sover 0
%define libqpulseaudioprivate libqpulseaudioprivate%sover

Name: kf5-%rname
Version: 5.5.4
Release: alt1
%K5init altplace

Group: Graphical desktop/KDE
Summary: Audio Volume Plasma Applet
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Provides: kde5-volume-control
Requires: pulseaudio-daemon

Source: %rname-%version.tar
Patch1: alt-lib-sover.patch

# Automatically added by buildreq on Mon Aug 24 2015 (-bi)
# optimized out: cmake cmake-modules elfutils glib2-devel libEGL-devel libGL-devel libgpg-error libjson-c libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-qml libqt5-quick libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms pkg-config python-base python3 python3-base qt5-base-devel rpm-build-gir ruby ruby-stdlibs
#BuildRequires: extra-cmake-modules gcc-c++ kf5-kauth-devel kf5-kcodecs-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdeclarative-devel kf5-kglobalaccel-devel kf5-ki18n-devel kf5-kpackage-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-plasma-framework-devel libpulseaudio-devel python-module-google qt5-declarative-devel rpm-build-python3 rpm-build-ruby
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++ qt5-base-devel qt5-declarative-devel
BuildRequires: libpulseaudio-devel
BuildRequires: kf5-kauth-devel kf5-kcodecs-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdeclarative-devel
BuildRequires: kf5-kglobalaccel-devel kf5-ki18n-devel kf5-kpackage-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-plasma-framework-devel
BuildRequires: kf5-kdoctools kf5-kdoctools-devel kf5-kdoctools-devel-static

%description
%summary

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

%package -n %libqpulseaudioprivate
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libqpulseaudioprivate
KF5 library


%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K5build

%install
%K5install
%K5install_move data kpackage kconf_update
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc COPYING*

%files
%_K5plug/kcms/kcm_pulseaudio.so
%_K5qml/org/kde/plasma/private/volume/
%_K5data/plasma/plasmoids/org.kde.plasma.volume/
%_K5data/kpackage/kcms/kcm_pulseaudio/
%_K5cf_upd/*
%_K5srv/*.desktop

#%files devel
#%_K5inc/plasma-pa_version.h
#%_K5inc/plasma-pa/
#%_K5link/lib*.so
#%_K5lib/cmake/plasma-pa
#%_K5archdata/mkspecs/modules/qt_plasma-pa.pri

%files -n %libqpulseaudioprivate
%_K5lib/libQPulseAudioPrivate.so.%sover
%_K5lib/libQPulseAudioPrivate.so.*

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

* Wed Oct 07 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.2-alt1
- new version

* Thu Sep 10 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.1-alt1
- new version

* Fri Sep 04 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.0-alt2
- provide kde5-volume-control

* Wed Aug 26 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.0-alt1
- new version

* Mon Aug 24 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.95-alt1
- initial build
