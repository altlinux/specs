%define rname kpat

%define cardgame_sover 0
%define libkcardgame libkcardgame%cardgame_sover

Name: %rname
Version: 26.04.2
Release: alt1
%K6init

Group: Games/Cards
Summary: Several patience card games
Url: http://www.kde.org
License: GPL-2.0-or-later

Requires: kde-carddecks
Provides:  kde5-kpat = %EVR
Obsoletes: kde5-kpat < %EVR

Source: %rname-%version.tar
Patch1: alt-lib-so-ver.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel qt6-phonon-devel qt6-svg-devel
BuildRequires: /usr/bin/7zz
BuildRequires: libvulkan-devel
BuildRequires: freecell-solver-devel black-hole-solver-devel
BuildRequires: kf6-karchive-devel kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel
BuildRequires: kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kcrash-devel kf6-kdbusaddons-devel kf6-kdeclarative-devel
BuildRequires: kf6-kdoctools-devel
BuildRequires: kf6-kguiaddons-devel kf6-ki18n-devel kf6-kiconthemes-devel  kf6-kio-devel kf6-kitemmodels-devel
BuildRequires: kf6-kitemviews-devel kf6-kjobwidgets-devel kf6-knewstuff-devel kf6-knotifications-devel kf6-knotifyconfig-devel
BuildRequires: kf6-kpackage-devel kf6-kparts-devel kf6-kservice-devel kf6-ktextwidgets-devel kf6-kunitconversion-devel
BuildRequires: kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel kf6-kxmlgui-devel kf6-solid-devel kf6-sonnet-devel
BuildRequires: kf6-kcrash-devel kf6-kiconthemes-devel
BuildRequires: kde6-libkdegames-devel

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
Provides:  kde5-kpat-common = %EVR
Obsoletes: kde5-kpat-common < %EVR
%description common
%name common package

%package -n %libkcardgame
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n %libkcardgame
%name library

%description
%summary.

%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K6build

%install
%K6install
%K6install_move data kpat mime knsrcfiles
mkdir -p %buildroot/%_K6xdgmime
mv %buildroot/%_K6data/mime/packages/kpatience{,6}.xml
%find_lang %name --with-kde --all-name

%files common -f %name.lang

%files
%doc COPYING*
%_datadir/qlogging-categories6/*.*categories
%_K6bin/kpat
%_K6data/kpat/
%_K6data/knsrcfiles/*.knsrc
%_K6icon/*/*/apps/kpat.*
%_K6xdgapp/org.kde.kpat.desktop
%_K6cfg/kpat.kcfg
%_K6xdgmime/kpatience?.xml
%_datadir/metainfo/*.xml

%files -n %libkcardgame
%_K6lib/libkcardgame.so.%cardgame_sover
%_K6lib/libkcardgame.so.*


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
