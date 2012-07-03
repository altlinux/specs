%define msxver 0.3.1
%define sfxver 0.2.3
Name: openttd-3rd-party
Version: 0.2.4
Release: alt2

Summary: 3rd Party data files for openttd
License: GPLv2
Group: Games/Strategy
URL: http://www.openttd.com/
Requires: openttd-data >= 1.0.1
Packager: Anton Farygin <rider@altlinux.com>
Buildarch: noarch

Source: opengfx-%version.tar
Source1: openmsx-%msxver.zip
Source2: opensfx-%sfxver.zip

BuildRequires: unzip


%description
3rd Party data files for openttd

%prep
%setup -q -n opengfx-%version

%build
unzip %SOURCE1
unzip %SOURCE2

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
* Tue Aug 31 2010 Anton Farygin <rider@altlinux.ru> 0.2.4-alt2
- updated openmsx to 0.3.1

* Thu Jun 17 2010 Anton Farygin <rider@altlinux.ru> 0.2.4-alt1
- first build for Sisyphus
