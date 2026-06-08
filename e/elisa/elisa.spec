%define rname elisa

%define sover 0
%define libelisalib libelisalib%sover

Name: %rname
Version: 26.04.2
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: Music player
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides:  kde5-elisa = %EVR
Obsoletes: kde5-elisa < %EVR

Requires: kf6-kirigami kf6-kirigami-addons

Source: %rname-%version.tar
Patch1: alt-install.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules
BuildRequires: libvlc-devel
#BuildRequires: https://gitlab.com/homeautomationqt/upnp-player-qt
BuildRequires: qt6-declarative-devel qt6-multimedia-devel qt6-declarative-devel qt6-svg-devel qt6-wayland-devel
BuildRequires: kf6-kcmutils-devel kf6-kcrash-devel kf6-kdbusaddons-devel kf6-kdeclarative-devel
BuildRequires: kf6-kdoctools-devel kf6-kfilemetadata-devel kf6-ki18n-devel kf6-kio-devel
BuildRequires: kf6-kirigami-devel kf6-kpackage-devel kf6-kiconthemes-devel
BuildRequires: kf6-baloo-devel kf6-qqc2-desktop-style-devel
BuildRequires: kf6-kirigami-addons-devel


%description
Elisa is a simple music player aiming to provide a nice experience for its users.
You can build and play your own playlist.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
Provides:  kde5-elisa-common = %EVR
Obsoletes: kde5-elisa-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libelisalib
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n %libelisalib
%name library

%prep
%setup -n %rname-%version
%patch1 -p1
#sed -i '/find_package.*LIBVLC/s|LIBVLC|LIBVLC_disabled|' CMakeLists.txt
#sed -i '/find_package.*KF6Baloo/s|KF6Baloo|KF6Baloo_disabled|' CMakeLists.txt
sed -i '/find_package.*UPNPQT/s|UPNPQT|UPNPQT_disabled|' CMakeLists.txt

%build
%K6build

%install
%K6install
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/*
%_datadir/qlogging-categories6/*.*categories

%files
%_K6bin/elisa
#%_K6qml/org/kde/elisa/
%_K6xdgapp/*elisa*.desktop
%_K6icon/*/*/apps/elisa.*
%_K6dbus_srv/org.kde.elisa.service
%_datadir/metainfo/*.xml

#%files devel
#%_K6inc/elisa_version.h
#%_K6inc/elisa/
#%_K6link/lib*.so
#%_K6lib/cmake/elisa

%files -n %libelisalib
%_K6lib/libelisaLib.so.%sover
%_K6lib/libelisaLib.so.*


%changelog
* Fri Jun 05 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.2-alt1
- new version

* Sun May 10 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.1-alt1
- new version

* Fri Mar 06 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.3-alt1
- new version

* Fri Feb 06 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.2-alt1
- new version

* Mon Jan 19 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.1-alt1
- new version

* Wed Nov 19 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.3-alt1
- new version

* Mon Oct 13 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.2-alt1
- new version

* Tue Sep 23 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.1-alt1
- new version

* Fri Jul 25 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.3-alt1
- new version

* Wed Jun 11 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.2-alt1
- new version

* Wed May 14 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.1-alt1
- new version

* Thu Apr 17 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.3-alt2
- update build requires

* Tue Mar 11 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.3-alt1
- new version

* Thu Mar 06 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.2-alt1
- new version

* Wed Jan 29 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.1-alt1
- new version

* Mon Nov 18 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.3-alt1
- new version

* Thu Oct 17 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build

