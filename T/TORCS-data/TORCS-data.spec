Name: TORCS-data
Version: 1.3.0
Release: alt0.1

Summary: The Open Racing Car Simulator - DATA
Group: Games/Sports
License: GPL
Url: http://torcs.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://dl.sf.net/torcs/TORCS-%version-data.tar.bz2
Source1: http://dl.sf.net/torcs/TORCS-%version-data-cars-extra.tar.bz2
Source2: http://dl.sf.net/torcs/TORCS-%version-data-tracks-road.tar.bz2

Provides: TORCS-data-cars-extra TORCS-data-tracks-base = 1.2.1
Obsoletes: TORCS-data-cars-extra TORCS-data-tracks-base

BuildArch: noarch

Requires: TORCS = %version

%description
Mandatory data (images, fonts, menus, cars, tracks...) for TORCS

%prep
%setup -c -q
%setup -q -T -D -b 1 -c torcs-data-cars-%version
%setup -q -T -D -b 2 -c torcs-data-tracks-%version

# replace nonunicode symbols in all XMLs
find ./ -name "*.xml" -print0 | xargs -0 perl -pi -e "s|\xE9|e|g"

%build
%install
mkdir -p %buildroot%_datadir/games/torcs
cp -r * %buildroot%_datadir/games/torcs

%files
%_datadir/games/torcs/*

%changelog
* Sun Dec 31 2006 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt0.1
- new version, add TORCS to requires
- change packager
- add hack for fix xml files encoding
- move mandatory car-extra, tracks-road package to here

* Sat Oct 08 2005 Igor Zubkov <icesik@altlinux.ru> 1.2.4-alt1
- update to 1.2.4
- spec clean up

* Tue Mar 23 2004 Alexander Belov <asbel@altlinux.ru> 1.2.2-alt1
- New version

* Wed Apr 30 2003 Alexander Belov <asbel@altlinux.ru> 1.2.1-alt1
- New version

* Fri Apr 4 2003 Alexander Belov <asbel@mail.ru> 1.2.0-alt1
- Sisyphus first release

* Mon Mar 24 2003 Eric Espié <Eric.Espie@free.fr> 1.2.0
- new version

* Mon Jul 15 2002 Eric Espié <Eric.Espie@free.fr> 1.1.0-2
- improved specfile

* Sat Jul 13 2002 Eric Espié <Eric.Espie@free.fr> 1.1.0
- initial RPM
