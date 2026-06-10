%define rname palapeli

%define pala_sover 0.1
%define libpala libpala%pala_sover

Name: %rname
Version: 26.04.2
Release: alt1
%K6init

Group: Games/Strategy
Summary: Jigsaw puzzle gam
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides:  kde5-palapeli = %EVR
Obsoletes: kde5-palapeli < %EVR

Source: %rname-%version.tar
Patch1: alt-lib-so-ver.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel qt6-svg-devel
BuildRequires: libssl-devel
BuildRequires: libvulkan-devel
BuildRequires: kf6-karchive-devel kf6-kcrash-devel kf6-kdoctools-devel kf6-ki18n-devel kf6-kiconthemes-devel
BuildRequires: kf6-kio-devel kf6-knotifications-devel
BuildRequires: kde6-libkdegames-devel

%description
Palapeli is a single-player jigsaw puzzle game.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
Provides:  kde5-palapeli-common = %EVR
Obsoletes: kde5-palapeli-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libpala
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libpala
%name library


%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K6build \
    -DKDE_INSTALL_INCLUDEDIR=%_K6inc \
    #

%install
%K6install
%K6install_move data palapeli kio
mv %buildroot/%_K6xdgmime/palapeli-mimetypes.xml \
    %buildroot/%_K6xdgmime/palapeli5-mimetypes.xml
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/*
%config(noreplace) %_K6xdgconf/*rc
%_K6icon/*/*/mimetypes/*palapeli*
%_K6xdgmime/*palapeli*.xml
%_datadir/qlogging-categories6/*.*categories

%files
%_K6bin/palapeli
%_K6plug/kf6/thumbcreator/*pala*.so
%_K6plug/palapelislicers/palapeli_*.so
%_K6xdgapp/*pala*.desktop
%_K6icon/*/*/apps/*palapeli*
%_K6data/palapeli/
%_K6data/kio/servicemenus/*pala*.desktop
%_K6notif/*pala*.notifyrc
%_datadir/metainfo/*.xml

%files devel
%_K6inc/Pala/
%_K6link/lib*.so
%_libdir/cmake/Pala/

%files -n %libpala
%_K6lib/libpala.so.%pala_sover
%_K6lib/libpala.so.*


%changelog
* Tue Jun 09 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.2-alt1
- new version

* Mon May 11 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.1-alt1
- new version

* Sat Feb 07 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.2-alt1
- new version

* Tue Jan 20 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.1-alt1
- new version

* Thu Oct 23 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.2-alt1
- new version

* Tue Jul 22 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.3-alt1
- new version

* Fri May 30 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.1-alt1
- new version

* Tue Feb 25 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.2-alt1
- new version

* Mon Nov 11 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.3-alt1
- initial build

