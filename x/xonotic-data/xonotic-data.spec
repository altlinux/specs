Name: xonotic-data
Version: 0.8.5
Release: alt1

Summary: Xonotic data files (graphics, music, maps etc)
Group: Games/Arcade
License: GPLv2+
Url: http://www.xonotic.org/

Source: font-unifont-20220627.pk3
Source1: font-xolonium-20220627.pk3
Source2: xonotic-20220627-data.pk3
Source3: xonotic-20220627-maps.pk3
Source4: xonotic-20220627-music.pk3
Source5: xonotic-20220627-nexcompat.pk3

BuildArch: noarch

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
* Wed Nov 16 2022 Artyom Bystrov <arbars@altlinux.org> 0.8.5-alt1
- Updated to upstream version 0.8.5

* Fri Jun 08 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8.2-alt1
- Updated to upstream version 0.8.2.

* Thu Jun 13 2013 Igor Zubkov <icesik@altlinux.org> 0.7.0-alt1
- 0.6.0 -> 0.7.0

* Sat Oct 20 2012 Igor Zubkov <icesik@altlinux.org> 0.6.0-alt1
- build for Sisyphus

