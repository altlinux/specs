%define rname ksirk

%define iris_ksirk_sover 0
%define libiris_ksirk libiris_ksirk%iris_ksirk_sover

Name: %rname
Version: 26.04.2
Release: alt1
%K6init

Group: Games/Strategy
Summary: World Domination Strategy Game
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides:  kde5-ksirk = %EVR
Obsoletes: kde5-ksirk < %EVR
Provides:  kde5-ksirk-common = %EVR
Obsoletes: kde5-ksirk-common < %EVR
Obsoletes: libiris_ksirk0 < %EVR

Source: %rname-%version.tar
Patch1: alt-libiris-so-version.patch
Patch2: alt-config-help-btn.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel qt6-svg-devel qt6-multimedia-devel qt6-5compat-devel
BuildRequires: libvulkan-devel
BuildRequires: qt6-phonon-devel
BuildRequires: libqca-qt6-devel libssl-devel zlib-devel
BuildRequires: kf6-kcrash-devel  kf6-kdoctools-devel kf6-ki18n-devel kf6-kiconthemes-devel
BuildRequires: kf6-kio-devel kf6-knewstuff-devel kf6-kwallet-devel
BuildRequires: kde6-libkdegames-devel

%description
The goal of the game is simply to conquer the World... It is done by attacking your neighbors
with your armies.

%prep
%setup -n %rname-%version
#%patch1 -p1
%patch2 -p1

%build
%K6build

%install
%K6install
%K6install_move data ksirk ksirkskineditor knsrcfiles
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc COPYING*
%_datadir/qlogging-categories6/*.*categories
%_K6bin/ksirk*
%_K6xdgapp/org.kde.ksirk*.desktop
%_K6data/ksirk/
%_K6data/ksirkskineditor/
%_K6icon/*/*/apps/ksirk.*
%_K6cfg/ksirk*.kcfg
%_K6data/knsrcfiles/*ksirk*.*
%_datadir/metainfo/*.xml


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

