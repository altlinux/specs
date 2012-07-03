Name: tremulous-data
Version: 1.1.0
Release: alt1

Summary: Tremulous - 3D FPS Strategic Shooter - Data files
License: GPL
Group: Games/Arcade
Url: http://tremulous.net

Packager: Timur Batyrshin <erthad@altlinux.org>

BuildArch: noarch

Source0: tremulous-data-1.1.0.tar.bz2

Requires: tremulous-common

%description
Tremulous is a free, open source game that blends a team based FPS with elements
of an RTS. Players can choose from 2 unique races, aliens and humans. Players on
both teams are able to build working structures in-game like an RTS. These
structures provide many functions, the most important being spawning. The
designated builders must ensure there are spawn structures or other players will
not be able to rejoin the game after death. Other structures provide automated
base defense (to some degree), healing functions and much more...

This package contains data files needed for Tremulous.

%install
mkdir -p %buildroot%_gamesdatadir/tremulous

tar -jxf %SOURCE0 -C %buildroot%_gamesdatadir/tremulous

%files
%_gamesdatadir/tremulous

%changelog
* Wed Sep 10 2008 Timur Batyrshin <erthad@altlinux.org> 1.1.0-alt1
- Initial build for ALT Linux

