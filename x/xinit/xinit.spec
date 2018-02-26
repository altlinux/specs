Name: xinit
Version: 1.3.2
Release: alt1
Summary: X Window System initializer
License: MIT/X11
Group: System/X11
Url: http://xorg.freedesktop.org

Source: %name-%version.tar
Patch: %name-%version-%release.patch

Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires: xinitrc > 2.4.23-alt1

BuildRequires: libConsoleKit-devel libX11-devel xorg-util-macros

%description
The  xinit  program  is  used to start the X Window System server and a
first client program on systems  that  cannot  start  X  directly  from
/etc/X11/init  or  in  environments that use multiple window systems.  When
this first client exits, xinit will kill the X server and  then  termi-
nate.

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--with-xinitdir=%_sysconfdir/X11/xinit
%make_build

%install
%make DESTDIR=%buildroot install

%files
%ghost %dir %_sysconfdir/X11/xinit
%_bindir/*
%_man1dir/*

%changelog
* Fri Mar 23 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.3.2-alt1
- 1.3.2

* Sun Oct 31 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.3.0-alt1
- 1.3.0

* Sun Aug 22 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Fri Feb 05 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Fri Aug 07 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.1.1-alt2
- added ck-xinit-session

* Thu Dec 18 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.1.1-alt1
- 1.1.1

* Fri Jun 13 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Thu May 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.9-alt1
- 1.0.9

* Fri Mar 07 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.8-alt1
- 1.0.8

* Thu Sep 20 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0.7-alt1
- 1.0.7

* Thu Sep 06 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0.5-alt1
- 1.0.5

* Tue May 22 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0.4-alt1
- 1.0.4

* Wed Nov 08 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.3-alt3
- added: return xinit errorlevel (fixes #10245)

* Sat Oct 14 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.3-alt2
- 1.0.3

* Fri Jun 30 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt2
- added xinit-1.0.2-setuid.patch

* Mon Apr 03 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Tue Dec 27 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.4-alt1
- Xorg-7.0RC3

* Wed Nov 23 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.3-alt0.1
- initial release

