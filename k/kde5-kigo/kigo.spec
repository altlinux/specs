%define rname kigo

Name: kde5-%rname
Version: 17.08.3
Release: alt1%ubt
%K5init

Summary: %rname is an open-source implementation of the popular Go game
License: %gpl2only
Group: Games/Boards
Url: https://www.kde.org/applications/games/kigo
Source0: %rname-%version.tar
Requires: gnugo
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt rpm-build-licenses 
BuildRequires: extra-cmake-modules
BuildRequires: qt5-declarative-devel qt5-svg-devel
#Tier 1
BuildRequires: kf5-kdbusaddons-devel
#Tier 2
BuildRequires: kf5-kcrash-devel kf5-kdoctools-devel
#Tier 3
BuildRequires: kf5-knewstuff-devel kf5-kio-devel kf5-ktextwidgets-devel
#KDE apps
BuildRequires: kde5-libkdegames-devel

%description
%rname is an open-source implementation of the popular Go game. Go is a
strategic board game for two players. It is also known as igo (Japanese), weiqi
or wei ch'i (Chinese) or baduk (Korean). Go is noted for being rich in strategic
complexity despite its simple rules. The game is played by two players who
alternately place black and white stones (playing pieces, now usually made of
glass or plastic) on the vacant intersections of a grid of 19x19 lines (9x9 or
13x13 for easier games).

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
%_K5bin/%rname
%_K5xdgapp/org.kde.%{rname}.desktop
%_K5icon/hicolor/*/*/%{rname}*.*
%_K5xmlgui/%{rname}/
%_K5data/%{rname}/
%_K5cfg/%{rname}.kcfg
%_K5xdgconf/%{rname}-games.knsrc
%_K5xdgconf/%{rname}.knsrc

%changelog
* Fri Nov 17 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.3-alt1%ubt
- new version

* Mon Aug 28 2017 Stanislav Levin <slev@altlinux.org> 17.08.0-alt1%ubt
- Initial build

