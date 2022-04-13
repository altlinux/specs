%define msxver 0.4.2
%define sfxver 1.0.3
Name: openttd-3rd-party
Version: 7.1
Release: alt3

Summary: 3rd Party data files for openttd
License: GPLv2
Group: Games/Strategy
URL: http://www.openttd.com/
Buildarch: noarch
Source: opengfx-%version.tar
Source1: openmsx-%msxver.tar
Source2: opensfx-%sfxver.tar

BuildRequires: unzip


%description
3rd Party data files for openttd

%prep
%setup -q -n opengfx-%version

%build
tar xvf %SOURCE1
tar xvf %SOURCE2

%install
mkdir -p %buildroot%_prefix/games
mkdir -p %buildroot%_datadir/games/openttd/gm
mkdir -p %buildroot%_datadir/games/openttd/data
cp *.grf *.obg opensfx-%sfxver/opensfx.* %buildroot%_datadir/games/openttd/data/
cp openmsx-%msxver/*.{mid,obm} %buildroot%_datadir/games/openttd/gm

%files
%_datadir/games/openttd/data/*
%_datadir/games/openttd/gm/*


%changelog
* Wed Apr 13 2022 Anton Farygin <rider@altlinux.ru> 7.1-alt3
- opensfx: 1.0.2 -> 1.0.3

* Fri Oct 29 2021 Anton Farygin <rider@altlinux.ru> 7.1-alt2
- openmsx: 0.4.0 -> 0.4.2
- opensfx: 1.0.1 -> 1.0.2

* Tue Sep 28 2021 Anton Farygin <rider@altlinux.ru> 7.1-alt1
- opengfx: 0.6.1 -> 7.1

* Wed Apr 07 2021 Anton Farygin <rider@altlinux.org> 0.6.1-alt1
- opengfx: 0.6.0 -> 0.6.1
- opensfx: 0.2.3 -> 1.0.1
- openmsx: 0.3.1 -> 0.4.0

* Mon Apr 06 2020 Anton Farygin <rider@altlinux.ru> 0.6.0-alt1
- new version 

* Wed Apr 03 2019 Anton Farygin <rider@altlinux.ru> 0.5.5-alt1
- new version

* Fri May 05 2017 Anton Farygin <rider@altlinux.ru> 0.5.4-alt1
- new version

* Tue Apr 07 2015 Anton Farygin <rider@altlinux.ru> 0.5.2-alt1
- updated to RC1 release for new version of openttd

* Tue Jun 24 2014 Anton Farygin <rider@altlinux.ru> 0.5.1-alt1
- new version

* Thu Apr 10 2014 Anton Farygin <rider@altlinux.ru> 0.5.0-alt1
- new version

* Tue Jun 25 2013 Anton Farygin <rider@altlinux.ru> 0.4.7-alt1
- new version

* Fri Jul 20 2012 Anton Farygin <rider@altlinux.ru> 0.4.4-alt1
- new version

* Tue Aug 31 2010 Anton Farygin <rider@altlinux.ru> 0.2.4-alt2
- updated openmsx to 0.3.1

* Thu Jun 17 2010 Anton Farygin <rider@altlinux.ru> 0.2.4-alt1
- first build for Sisyphus
