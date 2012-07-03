Name: TORCS-data-tracks
Version: 1.3.0
Release: alt0.1

Summary: TORCS - Extra Track Pack
Group: Games/Sports
License: GPL
Url: http://torcs.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source1: http://dl.sf.net/torcs/TORCS-%version-data-tracks-dirt.tar.bz2
Source2: http://dl.sf.net/torcs/TORCS-%version-data-tracks-oval.tar.bz2

BuildArch: noarch

Requires: TORCS = %version

%description
Tracks Pack for TORCS

%prep
%setup -q -T -D -b 1 -c torcs-data-tracks-%version
%setup -q -T -D -b 2 -c torcs-data-tracks-%version
#%setup -q -T -D -b 3 -c torcs-data-tracks-%version

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
- add hack for fix xml files encoding
- move mandatory tracks-road to TORCS-data package
- change packager

* Sat Oct 08 2005 Igor Zubkov <icesik@altlinux.ru> 1.2.4-alt1
- update to 1.2.4
- spec clean up

* Tue Mar 23 2004 Alexander Belov <asbel@altlinux.ru> 1.2.2-alt1
- New version
- All tracks in one package
- Rename package

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
