%define _name flare

Name: %_name-game
Version: 1.05
Release: alt1

Summary: Fantasy action RPG using the FLARE engine
License: %gpl3plus
Group: Games/Adventure

URL: http://flarerpg.org/
# https://github.com/clintbellanger/flare-game.git
Source: %name-%version.tar
#Patch: %name-%version-%release.patch
BuildArch: noarch

BuildRequires(pre): rpm-build-licenses rpm-macros-cmake
BuildRequires: gcc-c++ cmake

Requires: %_name-engine >= %version

Obsoletes: flare < %version-%release
Provides: flare = %version-%release
Obsoletes: flare-data < %version-%release
Provides: flare-data = %version-%release

%define _unpackaged_files_terminate_build 1

%description
The Empyrean Campaign is a single-player 2D action RPG with fast-paced action
and a dark fantasy style.
It is built on the FLARE engine (Free/Libre Action Roleplaying Engine).

%prep
%setup
#patch -p1

%build
%cmake -DBINDIR=bin -DDATADIR=share/flare
cd BUILD
%make_build
cd -

%install
cd BUILD
%makeinstall_std
cd -
%find_lang %_name

%files -f %_name.lang
%_datadir/%_name/*
%_datadir/appdata/*.xml

%changelog
* Thu May 03 2018 Mikhail Efremov <sem@altlinux.org> 1.05-alt1
- Updated to 1.05.

* Wed Apr 18 2018 Mikhail Efremov <sem@altlinux.org> 1.03-alt1
- Updated to 1.03.

* Wed Mar 14 2018 Mikhail Efremov <sem@altlinux.org> 1.0-alt1
- Updated description.
- Updated URL.
- Updated to 1.0.

* Sat Aug 30 2014 Mikhail Efremov <sem@altlinux.org> 0.19-alt1
- Updated to 0.19.

* Fri Jan 06 2012 Mikhail Efremov <sem@altlinux.org> 0.15-alt1
- Initial build.

