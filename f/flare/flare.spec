Name: flare
Version:0.15
Release: alt1

Summary: Single-player 2D action RPG
License: %gpl3plus
Group: Games/Adventure

URL: http://clintbellanger.net/rpg/
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses rpm-macros-cmake
BuildRequires: gcc-c++ cmake libSDL-devel libSDL_image-devel libSDL_mixer-devel libSDL_ttf-devel

Requires: %name-data = %version-%release

%description
Flare (Free Libre Action Roleplaying Engine) is a simple game engine
built to handle a very specific kind of game: single-player 2D action
RPGs. Flare is not a reimplementation of an existing game or engine.
It is a tribute to and exploration of the action RPG genre.
Rather than building a very abstract, robust game engine, the goal of
this project is to build several real games and harvest an engine from
the common, reusable code. The first game, in progress, is a fantasy
dungeon crawl.

%package data
Summary: Data files for Flare
License: %ccbysa30
Group: Games/Adventure
BuildArch: noarch

%description data
Data files for Flare.

%prep
%setup
%patch -p1

%build
%cmake -DBINDIR=bin -DDATADIR=share/flare
cd BUILD
%make_build
cd -

%install
cd BUILD
%makeinstall_std
cd -
%find_lang %name

%files
%_bindir/%name

%files data -f %name.lang
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/*/*
%_datadir/%name

%changelog
* Fri Jan 06 2012 Mikhail Efremov <sem@altlinux.org> 0.15-alt1
- Initial build.

