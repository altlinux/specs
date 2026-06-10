%define rname ksudoku

Name: %rname
Version: 26.04.2
Release: alt1
%K6init

Group: Games/Strategy
Summary: %rname is a logic-based symbol placement puzzle
Url: https://www.kde.org/applications/games/ksudoku
License: BSD-3-Clause

Provides:  kde5-ksudoku = %EVR
Obsoletes: kde5-ksudoku < %EVR

Source0: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules libGLU-devel
BuildRequires: /usr/bin/7zz
BuildRequires: libvulkan-devel
BuildRequires: qt6-declarative-devel qt6-svg-devel
BuildRequires: kf6-kdbusaddons-devel kf6-karchive-devel kf6-kguiaddons-devel
BuildRequires: kf6-ki18n-devel kf6-kdoctools-devel kf6-kcrash-devel
BuildRequires: kf6-kiconthemes-devel kf6-kio-devel kf6-kiconthemes-devel
BuildRequires: kde6-libkdegames-devel

%description
%rname is a logic-based symbol placement puzzle. The player has to fill a grid
so that each column, row as well as each square block on the game field contains
only one instance of each symbol.

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%K6install_move data %rname
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc COPYING*
%_K6xdgconf/%{rname}rc
%_K6bin/%rname
%_K6xdgapp/org.kde.%{rname}.desktop
%_K6icon/hicolor/*/*/%{rname}*.*
%_K6data/%{rname}/
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

