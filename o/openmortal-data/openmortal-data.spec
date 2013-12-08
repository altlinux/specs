Name: openmortal-data
Version: 0.7.1
Release: alt1

Summary: Parody of the original fighting game "Mortal Kombat" (data files)
Group: Games/Arcade
License: GPL

Url: http://openmortal.sourceforge.net/

Source0: openmortal-0.7.tar.bz2
Source1: laurence.zip
Source2: ikari.zip

Patch0: configure.in-alt-build.patch
Patch1: Makefile.am-alt-build.patch

#AutoReq: yes, noperl

BuildArch: noarch

Packager: Igor Zubkov <icesik@altlinux.org>

# Automatically added by buildreq on Sun Dec 08 2013 (-bi)
BuildRequires: unzip

%description
OpenMortal is a spoof of the original Mortal Kombat fighting game. The
funny thing about OpenMortal is that you can play the game AS YOURSELF.
It takes some work, but if you follow the Character Creation-HOWTO at

http://openmortal.sourceforge.net/Character_HOWTO.html

This is package contains data files for openmortal

%prep
%setup -q -n openmortal-0.7
%patch0 -p0
%patch1 -p0

unzip %SOURCE1 -d data/gfx
unzip %SOURCE2 -d data/gfx

%build
%autoreconf
./configure --prefix=/usr --datadir=/usr/share
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%dir %_datadir/openmortal/
%_datadir/openmortal/

%changelog
* Sun Dec 08 2013 Igor Zubkov <icesik@altlinux.org> 0.7.1-alt1
- 0.7.1

* Sat Jan 21 2006 Igor Zubkov <icesik@altlinux.ru> 0.7-alt1
- Initial build for Sisyphus
