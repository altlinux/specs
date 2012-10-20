Name: xonotic-data
Version: 0.6.0
Release: alt1

Summary: Xonotic data files (graphics, music, maps etc)
Group: Games/Arcade
License: GPLv2+
Url: http://www.xonotic.org/

Source0: font-nimbussansl-20120308.pk3
Source1: font-xolonium-20120308.pk3
Source2: xonotic-20120308-data.pk3
Source3: xonotic-20120308-maps.pk3
Source4: xonotic-20120308-music.pk3
Source5: xonotic-20120308-nexcompat.pk3

Requires: xonotic = %version

BuildArch: noarch

Packager: Igor Zubkov <icesik@altlinux.org>

%description
Data files used to play Xonotic.

%install
mkdir -p  %buildroot%_datadir/xonotic/data

install -pm644 %SOURCE0 %buildroot%_datadir/xonotic/data/
install -pm644 %SOURCE1 %buildroot%_datadir/xonotic/data/
install -pm644 %SOURCE2 %buildroot%_datadir/xonotic/data/
install -pm644 %SOURCE3 %buildroot%_datadir/xonotic/data/
install -pm644 %SOURCE4 %buildroot%_datadir/xonotic/data/
install -pm644 %SOURCE5 %buildroot%_datadir/xonotic/data/

%files
%dir %_datadir/xonotic
%_datadir/xonotic/

%changelog
* Sat Oct 20 2012 Igor Zubkov <icesik@altlinux.org> 0.6.0-alt1
- build for Sisyphus

