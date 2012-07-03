Name: numlock
Version: 2.0
Release: alt2.1
Serial: 1

Summary: Numlock key locker
License: GPL
Group: System/Configuration/Boot and Init
Packager: Evgenii Terechkov <evg@altlinux.org>
Source0: %name-%version.tar.bz2
Source1: %name.init
Patch: %name-alt-makefile.patch
Patch2: %name-alt-bindir.patch

Obsoletes: NumLock

# Automatically added by buildreq on Tue Jan 08 2008
BuildRequires: libX11-devel libXtst-devel libXi-devel libXext-devel

%description
NumLock enable to lock the numlock key. Only enable it at boot-time with
ntsysv or with any other SVSR like rc.d config scripts editor such as
tksysv or the ones from GNOME and KDE.
NumLock is safe for portable as it is disabled by default.

%prep
%setup
%patch -p1 -b .orig
%patch2 -p1 -b .orig

%build
%make_build X11LIBDIR=%_x11libdir

%install
%makeinstall TOP=%buildroot INITRDDIR=%_initdir
install -pm755 %SOURCE1 %buildroot%_initdir/%name
# Remove unpackaged files:
rm %buildroot%_x11mandir/fr/man?/*

%post
%post_service %name

%preun
%preun_service %name

%files
%_initdir/%name
%_sysconfdir/profile.d/%name.sh
%_x11sysconfdir/xinit.d/%name
%_bindir/*
%_man1dir/*
#remove to confirm our policy
#%lang(fr)%_x11mandir/fr/man?/*

%changelog
* Tue Dec 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:2.0-alt2.1
- NMU:
  * updated build dependencies

* Tue Jan  8 2008 Terechkov Evgenii <evg@altlinux.ru> 1:2.0-alt2
- Spec and buildrequires updated
- Patch2 added (bindir fixing)
- Packager tag added to spec
- Patch updated (--as-needed)

* Wed Feb 08 2006 Aleksandr 'Sass' Blokhin <sass@altlinux.ru> 1:2.0-alt1
- updated %%name-alt-makefile.patch

* Mon Apr 18 2005 Anton D. Kachalov <mouse@altlinux.org> 2.0-ipl10mdk.1
- multilib support

* Thu Apr  7 2005 Ivan Zakharyaschev <imz@altlinux.ru> 2.0-ipl10mdk
- requires console-tools_or_kbd (instead of console-tools)

* Wed Oct 22 2003 Aleksandr (Sass) Blokhin <sass@altlinux.ru> 2.0-ipl9mdk
- changed package requires
- specs cleanup

* Sat Nov 02 2002 Aleksandr 'Sass' Blokhin <sass@altlinux.ru> 2.0-ipl8mdk
- fixed file permissions on manual pages

* Thu Sep 19 2002 Stanislav Ievlev <inger@altlinux.ru> 2.0-ipl7mdk
- dropped french manual page: it must live in the man-pages-fr
- rebuild with gcc3

* Wed May 22 2002 Stanislav Ievlev <inger@altlinux.ru> 2.0-ipl6mdk
- removed noreplace for init-script - was problems on updates

* Tue May 22 2002 Konstantin Volckov <goldhead@altlinux.ru> 2.0-ipl5mdk
- Removed requires to glibc

* Thu Apr 11 2002 Stanislav Ievlev <inger@altlinux.ru> 2.0-ipl4mdk
- fixed post and preun scripts

* Fri Mar 29 2002 Stanislav Ievlev <inger@altlinux.ru> 2.0-ipl3mdk
- updated from MDK CVS
- cleanup spec

* Wed Jan 10 2001 AEN <aen@logic.ru>
- RE adaptations

* Tue Jan  9 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 2.0-1mdk
- really fix the xinit.d file
- reintegrate into CVS

* Thu Nov  2 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0-11mdk
- fix the xinit.d file, thanks to fcrozat
- get latest code that ensure the numlock is on even if it was already
  on, thx to fcrozat

* Mon Sep 11 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0-10mdk
- tried to really fix numlock for fredl

* Wed Aug 30 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0-9mdk
- added %_initdir
- NumLock -> numlock by request of submarine ;-)
- %config(noreplace)

* Wed Apr 26 2000 Pixel <pixel@mandrakesoft.com> 1.0-8mdk
- force non-requiring XFree86-libs

* Wed Apr 12 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.0-7mdk
- launch via /etc/X11/xinit.d

* Wed Apr  5 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.0-6mdk
- Remove the noarch since now we have enable_X11_numlock.
- Cvs import.
- Add enable_X11_numlock program (thanks gégé).

* Fri Mar 31 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0-5mdk
- new groups

* Wed Dec 22 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- fix a bug in xterm handling (reject /dev/ttya??)

* Thu Nov 18 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- fix chkconfig
- explicitely requires console-tools for touch (this would be the first
  rpm to do this !) and fileutils for setleds (which may have cause problems)

* Fri Oct 28 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- fix a typo (rpm include the %setup in the %description section !!!)
- lowercase the rpm name for Lord DarkChmou

* Fri Oct 24 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- initial spec

