Name: xconsole
Version: 1.0.4
Release: alt1

Summary: monitor system console messages with X
License: MIT/X11
Group: System/X11

Url: http://xorg.freedesktop.org
Source: %name-%version.tar
Patch: %name-%version-%release.patch

Packager: Valery Inozemtsev <shrek@altlinux.ru>

BuildRequires: libXaw-devel xorg-util-macros

%description
The xconsole program displays messages which are usually sent to /dev/console.

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
%_sysconfdir/X11/app-defaults/*
%_bindir/*
%_man1dir/*

%changelog
* Fri Sep 24 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.0.4-alt1
- 1.0.4

* Mon Oct 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.3-alt3
- fixed build with new glibc

* Mon Feb 25 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.3-alt2
- fixed Summary/Description (close #14610)

* Tue Aug 21 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0.3-alt1
- 1.0.3
- drop upstream patch

* Thu Oct 19 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt2
- added xconsole-1.0.2-git-openpty.patch:
  + check if openpty() is available and use it if it is.

* Thu Apr 27 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Mon Mar 20 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt2
- Avoid potential underflow if read() returns -1

* Tue Dec 27 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.3-alt1
- Xorg-7.0RC3

* Thu Nov 24 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.2-alt0.1
- initial release

