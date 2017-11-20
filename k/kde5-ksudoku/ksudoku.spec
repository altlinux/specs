%define rname ksudoku

Name: kde5-%rname
Version: 17.08.3
Release: alt1%ubt
%K5init

Summary: %rname is a logic-based symbol placement puzzle
License: %gpl2only
Group: Games/Strategy
Url: https://www.kde.org/applications/games/ksudoku
Source0: %rname-%version.tar
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt rpm-build-licenses 
BuildRequires: extra-cmake-modules libGLU-devel
BuildRequires: qt5-declarative-devel qt5-svg-devel
#Tier 1
BuildRequires: kf5-kdbusaddons-devel kf5-karchive-devel kf5-kguiaddons-devel
BuildRequires: kf5-ki18n-devel
#Tier 2
BuildRequires: kf5-kdoctools-devel kf5-kcrash-devel
#Tier 3
BuildRequires: kf5-kiconthemes-devel kf5-kio-devel
#KDE apps
BuildRequires: kde5-libkdegames-devel

%description
%rname is a logic-based symbol placement puzzle. The player has to fill a grid
so that each column, row as well as each square block on the game field contains
only one instance of each symbol.

%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%K5install_move data %rname
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc COPYING*
%_K5xdgconf/%{rname}rc
%_K5bin/%rname
%_K5xdgapp/org.kde.%{rname}.desktop
%_K5icon/hicolor/*/*/%{rname}*.*
%_K5data/%{rname}/
%_K5xmlgui/%{rname}/

%changelog
* Fri Nov 17 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.3-alt1%ubt
- new version

* Mon Aug 28 2017 Stanislav Levin <slev@altlinux.org> 17.08.0-alt1%ubt
- Initial build

