%define _prefix	/usr

Name: apetag
Version: 1.12
Release: alt1.1

Summary: A command line ape 2.0 tagger
Summary(ru_RU.UTF-8): Консольный редактор тэгов ape 2.0
License: GPL
Group: Sound
Url: http://www.muth.org/Robert/Apetag/

Packager: Maxim Zhukov <mzhukov@altlinux.org>

Source: %name-%version.tar.gz
Patch: apetag-gcc43.patch

BuildRequires: gcc-c++

#Requires: glibc-pthread libstdc++-devel

%description
Apetag is command line tagging tool for music files such as Monkey's
Audio and Musepack using the APE 2.0 standard.

Apetag comes with a python script, tagdir.py which will tag all
tracks belonging to a given album based on the freedb record. (A
simple tool for retrieved such records is freedbtool.) tagdir.py
will invoke the appropriate tagging tool depending on the music
files present. Currently supported are apetag for mpc files and
metaflac for flac files. Also included is a simple script
rmid3tag.py which removes id3v1 tags from arbitrary files.

Author: Robert Muth <robert@muth.org>


%prep
#setup -n Apetag
%setup
%patch -p1

%build
%__make

%install
install -dm 755  %buildroot%prefix/bin
install -m 755 %name \
	%buildroot%prefix/bin
install -m 755 *.py \
	%buildroot%prefix/bin

%files
%doc 00copying 00readme index.html
%_bindir/%name
%_bindir/*.py

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.12-alt1.1
- Rebuild with Python-2.7

* Tue Jun 01 2010 Maxim Zhukov <mzhukov@altlinux.org> 1.12-alt1
- initial build for ALT Linux Sisyphus

* Sun May 03 2009 - Toni Graffy <toni@links2linux.de> 1.12-0.pm.1
- update to 1.12
* Wed Jul 02 2008 - Toni Graffy <toni@links2linux.de> 1.11-0.pm.1
- update to 1.11
* Sat Jan 12 2008 - Toni Graffy <toni@links2linux.de> 1.10-0.pm.1
- update to 1.10
* Thu Aug 30 2007 - Toni Graffy <toni@links2linux.de> 1.8-0.pm.3
- added debug_package
* Mon Sep 18 2006 - Herbert Graeber <herbert@links2linux.de> 1.8-0.pm.2
- make it work with y2pmbuild
- make it 64-bit compatible
* Sat Sep 16 2006 - Toni Graffy <toni@links2linux.de> 1.8-0.pm.1
- rebuild for packman
* Sun Jul 16 2006 - oc2pus@arcor.de 1.8-0.oc2pus.1
- update to 1.8
* Sun Dec 04 2005 - oc2pus@arcor.de 1.7-0.oc2pus.1
- first version 1.7
