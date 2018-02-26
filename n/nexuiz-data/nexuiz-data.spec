Name: nexuiz-data
Version: 2.5.2
Release: alt1

Summary: 3D deathmatch shooter game - data files
License: GPL
Group: Games/Arcade
Url: http://www.nexuiz.com

Packager: Igor Zubkov <icesik@altlinux.org>

BuildArch: noarch

Source0: data20091001.pk3
Source1: common-spog.pk3
Source2: data20091001havoc.pk3

%description
Nexuiz is a 3d deathmatch shooter based on a darkplaces engine.
This package contains data files needed for Nexuiz.

%install
mkdir -p %buildroot%_datadir/nexuiz/data/
mkdir -p %buildroot%_datadir/nexuiz/havoc/

install -pm644 %SOURCE0 %buildroot%_datadir/nexuiz/data/
install -pm644 %SOURCE1 %buildroot%_datadir/nexuiz/data/

install -pm644 %SOURCE2 %buildroot%_datadir/nexuiz/havoc/

%files
%dir %_datadir/nexuiz
%_datadir/nexuiz/

%changelog
* Tue Dec 08 2009 Igor Zubkov <icesik@altlinux.org> 2.5.2-alt1
- 2.5.1 -> 2.5.2

* Thu Sep 10 2009 Igor Zubkov <icesik@altlinux.org> 2.5.1-alt1
- 2.5.1

* Sun May 18 2008 Igor Zubkov <icesik@altlinux.org> 2.4.2-alt1
- 2.4 -> 2.4.2

* Sun Mar 02 2008 Igor Zubkov <icesik@altlinux.org> 2.4-alt1
- 2.3 -> 2.4

* Tue Nov 27 2007 Igor Zubkov <icesik@altlinux.org> 2.3-alt1
- 2.2.3 -> 2.3

* Thu Mar 15 2007 Igor Zubkov <icesik@altlinux.org> 2.2.3-alt1
- 2.0 -> 2.2.3

* Wed Aug 23 2006 Pavlov Konstantin <thresh@altlinux.ru> 2.0-alt1
- 2.0 release.
- some spec cleanup.

* Tue Feb 21 2006 Pavlov Konstantin <thresh@altlinux.ru> 1.5-alt1
- 1.5 release.
- noarch.

* Fri Sep 02 2005 Pavlov Konstantin <thresh@altlinux.ru> 1.2-alt1
- Initial build for Sisyphus.
- Added .pk3 file fixing "strange errors" on server side.
