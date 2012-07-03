Name: sessreg
Version: 1.0.7
Release: alt1
Summary: manage utmp/wtmp entries for non-init clients
License: MIT/X11
Group: System/X11
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: xorg-xproto-devel xorg-util-macros

%description
Sessreg is a simple program for managing utmp/wtmp entries for xdm sessions

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure

%make_build

%install
%make DESTDIR=%buildroot install

%files
%_bindir/*
%_man1dir/*

%changelog
* Fri Mar 23 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.0.7-alt1
- 1.0.7

* Fri Jun 04 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.0.6-alt1
- 1.0.6

* Tue Oct 13 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.5-alt1
- 1.0.5

* Fri Jun 13 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.4-alt1
- 1.0.4

* Sat Aug 18 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Thu Nov 30 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Thu Nov 09 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Mon Jan 09 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt2
- added hughuid patch

* Tue Dec 27 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.2-alt1
- Xorg-7.0RC3

* Thu Nov 24 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.1-alt0.1
- initial release

