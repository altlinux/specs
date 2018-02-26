%set_verify_elf_method none
%set_compress_method none

Name: rocksndiamonds-emc
Version: 2.0.0
Release: alt3
Serial:1

Summary: Extra levels for Rocks'n'Diamonds game
Group: Games/Arcade
License: GPL
URL: http://www.artsoft.org/%name

BuildArch: noarch
AutoReqProv: no
Requires: rocksndiamonds

Source: Emerald_Mine_Club-%version.7z
BuildRequires: p7zip

%description
Rocks'n'Diamonds is a nice little game with color graphics
and sound for your Unix system.

This is a package with "Emerald Mine" extra levels.

%prep
%setup -cT
SEVENZIP=`which 7za ||:`
[ -n "$SEVENZIP" ] || SEVENZIP=7z
$SEVENZIP x %SOURCE0

%build

%install
mkdir -p %buildroot/%_gamesdatadir/rocksndiamonds/levels
cp -ar * %buildroot/%_gamesdatadir/rocksndiamonds/levels/


%files
%_gamesdatadir/rocksndiamonds/levels/*

%changelog
* Tue Dec 06 2011 Sergey V Turchin <zerg@altlinux.org> 1:2.0.0-alt3
- fix to build

* Tue Dec 25 2007 Sergey V Turchin <zerg at altlinux dot org> 1:2.0.0-alt2
- fix unpack sources when build

* Fri Jan 26 2007 Sergey V Turchin <zerg at altlinux dot org> 1:2.0.0-alt1
- new version

* Wed May 05 2004 Sergey V Turchin <zerg at altlinux dot org> 1:1.0-alt1
- bump %%serial to change %%release

* Sun Jan 14 2001 Dmitry V. Levin <ldv@fandra.org> 1.0-ipl1
- Initial revision.
