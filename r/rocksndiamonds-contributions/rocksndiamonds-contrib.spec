Name: rocksndiamonds-contributions
Version: 1.2.0
Release: alt2

Group: Games/Arcade
Summary: Extra levels for Rocks'n'Diamonds game
License: GPL
URL: http://www.artsoft.org/%name

BuildArchitectures: noarch
AutoReqProv: no

Requires: rocksndiamonds
Conflicts: rocksndiamonds <= 3.0.8

Source: Contributions-%version.7z
BuildRequires: p7zip

%description
Rocks'n'Diamonds is a nice little game with color graphics
and sound for your Unix system.

This is a package with contributed extra levels.

%prep
%setup -qcT
SEVENZIP=`which 7za ||:`
[ -n "$SEVENZIP" ] || SEVENZIP=7z
$SEVENZIP x %SOURCE0

%install
%__mkdir_p %buildroot/%_gamesdatadir/rocksndiamonds/levels
%__cp -a ./* %buildroot/%_gamesdatadir/rocksndiamonds/levels

%define _compress_method none
%define _strip_method none

%files
%_gamesdatadir/rocksndiamonds/levels/*

%changelog
* Tue Dec 25 2007 Sergey V Turchin <zerg at altlinux dot org> 1.2.0-alt2
- fix unpack sources when build

* Mon Jul 17 2006 Sergey V Turchin <zerg at altlinux dot org> 1.2.0-alt1
- new version

* Tue Oct 11 2005 Sergey V Turchin <zerg at altlinux dot org> 1.1.0-alt1
- initial spec

