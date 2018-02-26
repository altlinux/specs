Name: rocksndiamonds-dx
Version: 1.0
Release: alt1
Serial:1

Summary: Extra levels for Rocks'n'Diamonds game
Group: Games/Arcade
License: GPL
URL: http://www.artsoft.org/%name
BuildArchitectures: noarch
AutoReqProv: no
Requires: rocksndiamonds

Source: rockslevels-dx-%version.tar.bz2

%description
Rocks'n'Diamonds is a nice little game with color graphics
and sound for your Unix system.

This is a package with "DX Boulderdash" extra levels.

%prep
%setup -qc

%install
mkdir -p $RPM_BUILD_ROOT%_gamesdatadir/rocksndiamonds
cp -a levels $RPM_BUILD_ROOT%_gamesdatadir/rocksndiamonds

%define _compress_method none
%define _strip_method none

%files
%_gamesdatadir/rocksndiamonds/levels/*

%changelog
* Wed May 05 2004 Sergey V Turchin <zerg at altlinux dot org> 1:1.0-alt1
- bump %%serial to change %%release

* Sun Jan 14 2001 Dmitry V. Levin <ldv@fandra.org> 1.0-ipl1
- Initial revision.
