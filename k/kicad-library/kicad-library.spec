Summary: Library for kicad (creation of electronic schematic diagrams)
Summary(ru_RU.UTF-8): Библиотеки для kicad (разработка печатных плат)
Name: kicad-library
Version: 4.0.5
Epoch: 1
Release: alt1
Source: %name-%version.tar
Source1: pretty-%version.tar
License: GPLv2+
Group: Sciences/Computer science
Url: https://code.launchpad.net/kicad
#Url: 	  http://bazaar.launchpad.net/~kicad-product-committers/kicad/library
#Url: 	  https://github.com/KiCad/kicad-library

Packager: Anton Midyukov <antohami@altlinux.org>
BuildArch: noarch
BuildRequires(pre): cmake rpm-macros-cmake gcc-c++
Requires: kicad-data = %version

%description
Kicad is an open source (GPL) software for the creation of electronic
schematic diagrams and printed circuit board artwork.

Kicad-library is a set of library needed by kicad.

%description -l ru_RU.UTF-8
Kicad - это программное обеспечение с открытым исходным кодом для
проектирования электронных схем и получения на их основе печатных плат.

Kicad-library содержит в себе библиотеки для kicad.

%prep
%setup

%build
%cmake \
    -DKICAD_STABLE_VERSION:BOOL=ON \
    -DCMAKE_BUILD_TYPE=Release
%make_build -C BUILD

%install
%makeinstall_std -C BUILD

# Footprints
tar xf %SOURCE1 --strip-components=1 -C %buildroot%_datadir/kicad/modules/
ln -f %buildroot%_datadir/kicad/template/fp-lib-table{.for-pretty,}

%files
%_datadir/kicad/library
%_datadir/kicad/modules
%_datadir/kicad/template

%changelog
* Sat Dec 10 2016 Anton Midyukov <antohami@altlinux.org> 1:4.0.5-alt1
- New version 4.0.5

* Wed Aug 31 2016 Anton Midyukov <antohami@altlinux.org> 1:4.0.4-alt1
- New version 4.0.4
- Added script for update pretty.

* Sat Jul 23 2016 Anton Midyukov <antohami@altlinux.org> 1:4.0.0-alt2
- Added pretty.

* Sat Dec 05 2015 Anton Midyukov <antohami@altlinux.org> 1:4.0.0-alt1
- New version.

* Sat Nov 29 2014 barssc <barssc@altlinux.ru> r240-alt1
- new version

* Tue Jun 07 2011 Denis Klimov <zver@altlinux.org> 1.0-alt2.20101208
- add BuildArch

* Tue Jun 07 2011 Denis Klimov <zver@altlinux.org> 1.0-alt1.20101208
- new version
- remove needless -q option for setup macro

* Fri Feb 13 2009 Alexey Shentzev <ashen@altlinux.ru> 1.0-alt0.1
- first build for ALT Linux
