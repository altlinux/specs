%define _name flare

Name: %_name-engine
Version:0.19
Release: alt1

Summary: A simple game engine for single-player 2D action RPGs
License: %gpl3plus
Group: Games/Adventure

URL: http://clintbellanger.net/rpg/
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses rpm-macros-cmake
BuildRequires: gcc-c++ cmake libSDL-devel libSDL_image-devel libSDL_mixer-devel libSDL_ttf-devel python-devel

%description
Flare (Free Libre Action Roleplaying Engine) is a simple game engine
built to handle a very specific kind of game: single-player 2D action
RPGs. Flare is not a reimplementation of an existing game or engine.
It is a tribute to and exploration of the action RPG genre.
Rather than building a very abstract, robust game engine, the goal of
this project is to build several real games and harvest an engine from
the common, reusable code.

%prep
%setup
%patch -p1

%build
%cmake -DBINDIR=bin -DDATADIR=share/%_name
cd BUILD
%make_build
cd -

%install
cd BUILD
%makeinstall_std
cd -

%files
%_bindir/%_name
%_datadir/%_name/
%_man1dir/*

%changelog
* Sat Aug 30 2014 Mikhail Efremov <sem@altlinux.org> 0.19-alt1
- Updated from upstream git.
- Updated to 0.19.

* Fri Nov 22 2013 Mikhail Efremov <sem@altlinux.org> 0.18-alt1
- Initial build.

