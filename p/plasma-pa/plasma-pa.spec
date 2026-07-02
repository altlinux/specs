%define rname plasma-pa

%define sover 6
%define libplasma_volume libplasma-volume%sover


Name: %rname
Version: 6.7.2
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: Audio Volume Plasma Applet
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides: plasma5-pa = %EVR
Obsoletes: plasma5-pa < %EVR

Requires: libkf6itemmodels kf6-kirigami kf6-kirigami-addons

Source: %rname-%version.tar
Patch1: alt-i18n.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-base-devel qt6-declarative-devel
BuildRequires: libvulkan-devel
BuildRequires: libpulseaudio-devel pulseaudio-qt6-devel
BuildRequires: libGConf-devel libcanberra-devel glib2-devel libgio-devel
BuildRequires: kf6-kauth-devel kf6-kcodecs-devel kf6-kconfig-devel kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kdeclarative-devel
BuildRequires: kf6-kglobalaccel-devel kf6-ki18n-devel kf6-kpackage-devel kf6-kservice-devel kf6-kwidgetsaddons-devel
BuildRequires: kf6-kdoctools kf6-kdoctools-devel kf6-kdoctools-devel kf6-knotifications-devel kf6-kirigami-devel
BuildRequires: kf6-kcmutils-devel kf6-ksvg-devel kf6-kstatusnotifieritem-devel
BuildRequires: plasma6-lib-devel

%description
%summary

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
Provides: plasma5-pa-common = %EVR
Obsoletes: plasma5-pa-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Conflicts: plasma5-pa-devel < %EVR
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libplasma_volume
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libplasma_volume
%name library

%package -n plasma5-pa
Group: System/Configuration/Other
Summary: Compatibility package
Requires: plasma-pa >= %version-%release
%description -n plasma5-pa
Compatibility package.

%prep
%setup -n %rname-%version
#%patch1 -p1

%build
%K6build

%install
%K6install
%K6install_move data kpackage kconf_update
%find_lang %name --with-kde --all-name


%files -n plasma5-pa

%files common -f %name.lang
%doc LICENSES/*

%files
%_K6plug/plasma/kcms/systemsettings/*pulse*.so
%_K6plug/kf6/kded/*audio*.so
%_K6plug/plasma/applets/*volume*.so
%_K6qml/org/kde/plasma/private/volume/
%_K6xdgapp/*pulse*.desktop
%_datadir/qlogging-categories6/*.*categories

%files -n %libplasma_volume
%_K6lib/libplasma-volume.so.%sover
%_K6lib/libplasma-volume.so.*

%changelog
* Wed Jul 01 2026 Sergey V Turchin <zerg@altlinux.org> 6.7.2-alt1
- new version

* Mon Jun 29 2026 Sergey V Turchin <zerg@altlinux.org> 6.7.1-alt1
- new version

* Tue May 12 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.5-alt1
- new version

* Thu Apr 09 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.4-alt1
- new version

* Mon Mar 30 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.3-alt1
- new version

* Wed Mar 11 2026 Sergey V Turchin <zerg@altlinux.org> 6.5.6-alt1
- new version

* Thu Jan 15 2026 Sergey V Turchin <zerg@altlinux.org> 6.5.5-alt1
- new version

* Wed Dec 10 2025 Sergey V Turchin <zerg@altlinux.org> 6.5.4-alt1
- new version

* Tue Nov 18 2025 Sergey V Turchin <zerg@altlinux.org> 6.5.3-alt1
- new version

* Thu Nov 13 2025 Sergey V Turchin <zerg@altlinux.org> 6.5.2-alt1
- new version

* Wed Nov 12 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.6-alt1
- new version

* Tue Sep 16 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.5-alt1
- new version

* Fri Aug 22 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.4-alt1
- new version

* Tue Jul 15 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.3-alt1
- new version

* Tue Jul 08 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.2-alt1
- new version

* Wed May 07 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.5-alt1
- new version

* Wed Apr 02 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.4-alt1
- new version

* Wed Mar 12 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.3-alt1
- new version

* Wed Feb 26 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.2-alt1
- new version

* Wed Feb 19 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.1-alt1
- new version

* Fri Feb 14 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.0-alt1
- new version

* Thu Jan 09 2025 Sergey V Turchin <zerg@altlinux.org> 6.2.5-alt1
- new version

* Tue Nov 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.4-alt1
- new version

* Wed Nov 06 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.3-alt1
- new version

* Mon Oct 28 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.2-alt1
- new version

* Tue Sep 10 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.5-alt1
- new version

* Tue Sep 10 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.4-alt2
- fix provides (closes: 51150)

* Thu Aug 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.4-alt1
- new version

* Thu Jul 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.2-alt1
- new version

* Wed Jun 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.1-alt1
- new version

* Tue Jun 25 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- initial build

