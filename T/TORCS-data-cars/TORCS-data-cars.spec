Name: TORCS-data-cars
Version: 1.3.0
Release: alt1

Summary: TORCS - Extra car pack
Group: Games/Sports
License: GPL
Url: http://torcs.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source1: http://dl.sf.net/torcs/TORCS-%version-data-cars-Patwo-Design.tar.bz2
Source2: http://dl.sf.net/torcs/TORCS-%version-data-cars-VM.tar.bz2
Source4: http://dl.sf.net/torcs/TORCS-%version-data-cars-kcendra-gt.tar.bz2
Source5: http://dl.sf.net/torcs/TORCS-%version-data-cars-kcendra-roadsters.tar.bz2
Source6: http://dl.sf.net/torcs/TORCS-%version-data-cars-kcendra-sport.tar.bz2
Source7: http://dl.sf.net/torcs/TORCS-%version-data-cars-nascar.tar.bz2

BuildArch: noarch

Requires: TORCS = %version

%description
Extra car pack for TORCS

%prep
%setup -q -T -D -b 1 -c torcs-data-cars-%version
%setup -q -T -D -b 2 -c torcs-data-cars-%version
#%setup -q -T -D -b 3 -c torcs-data-cars-%version
%setup -q -T -D -b 4 -c torcs-data-cars-%version
%setup -q -T -D -b 5 -c torcs-data-cars-%version
%setup -q -T -D -b 6 -c torcs-data-cars-%version
%setup -q -T -D -b 7 -c torcs-data-cars-%version

# replace nonunicode symbols in all XMLs
find ./ -name "*.xml" -print0 | xargs -0 perl -pi -e "s|\xE9|e|g"

%build
%install
mkdir -p %buildroot%_datadir/games/torcs/
cp -r * %buildroot%_datadir/games/torcs/

%files
%_datadir/games/torcs/*

%changelog
* Thu Dec 28 2006 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt1
- new version, add TORCS to requires
- add hack for fix xml files encoding
- move mandatory cars-extra to TORCS-data package
- change packager

* Sat Oct 08 2005 Igor Zubkov <icesik@altlinux.ru> 1.2.4-alt1
- update to 1.2.4
- spec clean up

* Tue Mar 23 2004 Alexander Belov <asbel@altlinux.ru> 1.2.2-alt1
- New version
- All cars in one package
- Rename package

* Wed Apr 30 2003 Alexander Belov <asbel@altlinux.ru> 1.2.1-alt1
- New version

* Fri Apr 4 2003 Alexander Belov <asbel@mail.ru> 1.2.0-alt1
- Sisyphus first release

* Thu Jan 02 2003 Eric Espié <Eric.Espie@free.fr> 1.2.0
- car compiled
- new packaging
