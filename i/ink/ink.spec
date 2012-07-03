Name: ink
Version: 0.5.1
Release: alt1

Summary: A command line tool which displays the ink level of your printer.
License: GPL
Group: Monitoring
Url: http://ink.sf.net/
Packager: Ilya Mashkin <oddity@altlinux.ru>
Source: %name-%version.tar.gz
Source1: %name.watch
Patch: ink-0.4.1-alt-makefile.patch

BuildPreReq: libinklevel-devel >= 0.6

%description
Command line tool for displaying ink level of your printer using libinklevel.

%prep
%setup 
#patch -p1

%build
./configure --prefix=/usr
%make_build OPTFLAGS="%optflags"

%install
%make_install install DESTDIR=%buildroot

%files
%_bindir/*
%_man1dir/*

%changelog
* Thu Sep 30 2010 Ilya Mashkin <oddity@altlinux.ru> 0.5.1-alt1
- 0.5.1

* Sun Jan 06 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.4.1-alt1
- new version
- return from orphaned
- add watch file

* Sun Oct 10 2004 Andrey Rahmatullin <wrar@altlinux.ru> 0.3-alt2
- set OPTFLAGS when building
- spec fixes
- Url changed

* Thu Dec 04 2003 Andrey Rahmatullin <wrar@altlinux.ru> 0.3-alt1
- new version

* Tue Nov 11 2003 Andrey Rahmatullin <wrar@altlinux.ru> 0.2-alt2.1
- minor spec fixes, Group changed again

* Thu Oct 23 2003 Andrey Rahmatullin <wrar@altlinux.ru> 0.2-alt2
- Group fixed

* Fri Oct 10 2003 Andrey Rahmatullin <wrar@altlinux.ru> 0.2-alt1
- built for Sisyphus
